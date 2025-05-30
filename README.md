# Mental Health in Tech: Predictive Risk Factors & Insights

This project analyzes mental health trends in the tech industry using survey data. It explores the relationships between demographic factors, work environments, and treatment-seeking behavior. The goal is to uncover patterns that can help HR leaders and mental health advocates better support employees in high-stress industries.

---

## Project Goals
- Identify key risk factors associated with seeking or avoiding mental health treatment.
- Understand how variables like **remote work**, **company size**, and **benefits** impact mental wellness.
- Build a simple **predictive model** to estimate likelihood of treatment-seeking.
- Visualize patterns to make data accessible to HR decision-makers and policy builders.

---

## Dataset
Source: [OSMI Mental Health in Tech Survey (Kaggle)](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)

- 1,400+ responses
- Key features include: Gender, remote work, company size, support benefits, and treatment-seeking history

---

## Methods
- **Data Cleaning & Normalization** (pandas)
- **Exploratory Data Analysis** (seaborn, matplotlib)
- **Classification Model**: Random Forest (scikit-learn)
- **Feature Encoding** and SHAP-style interpretation
- **Data Visualization** for stakeholder insights

---

## Key Insights
- Employees with access to mental health **benefits** are significantly more likely to seek treatment.
- **Remote workers** report lower treatment rates, suggesting possible underutilization of resources.
- Company **culture and size** play a large role in mental health outcomes.

---

## Files in this Repo
| File | Description |
|------|-------------|
| `01_eda_cleaning.ipynb` | Data cleaning, gender normalization, and EDA |
| `02_modeling.ipynb` | Predictive modeling to classify treatment behavior |
| `survey.csv` | Raw dataset |
| `visuals/` | Charts for portfolio or dashboards |
| `README.md` | Project summary and explanation |

---

## Contact
Created by **Jeff Charles**  
[LinkedIn](https://www.linkedin.com/in/charlesjeff) | [Email](mailto:jeffcharles1@yahoo.com)

