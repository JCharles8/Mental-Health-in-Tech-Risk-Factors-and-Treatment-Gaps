#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)


# In[3]:


df = pd.read_csv('survey.csv')


df.head()
df.info()
df.describe(include='all')


# In[4]:


# Data Cleaning

df.isnull().sum()


df = df.drop(columns=['comments', 'state', 'Timestamp'])

df['Gender'] = df['Gender'].str.lower().str.strip()
df['Gender'] = df['Gender'].replace({
    'male-ish': 'male', 'm': 'male', 'man': 'male',
    'f': 'female', 'woman': 'female', 'female-ish': 'female',
    'cis male': 'male', 'cis female': 'female'
})

df['Gender'] = df['Gender'].apply(lambda x: x if x in ['male', 'female'] else 'other')


# In[5]:


#Mental Health Treatment by Gender

sns.countplot(x='Gender', hue='treatment', data=df)
plt.title('Treatment Seeking by Gender')
plt.show()


# In[6]:


# Mental Health Support by Company Size

sns.countplot(y='no_employees', hue='treatment', data=df)
plt.title('Treatment Seeking by Company Size')
plt.show()


# In[7]:


#Remote Work & Treatment

sns.countplot(x='remote_work', hue='treatment', data=df)
plt.title('Remote Work vs Mental Health Treatment')
plt.show()


# In[9]:


#Predict if someone is likely to seek treatment

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Encode categorical variables
df_encoded = pd.get_dummies(df[['Gender', 'remote_work', 'tech_company', 'benefits', 'care_options', 'wellness_program']], drop_first=True)
df_encoded['treatment'] = df['treatment'].map({'Yes': 1, 'No': 0})

# Train/test split
X = df_encoded.drop('treatment', axis=1)
y = df_encoded['treatment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

