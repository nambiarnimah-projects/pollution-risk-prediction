# AQI Prediction and Air Pollution Risk Analysis

## Project Overview

Air pollution is one of the most serious environmental and public health challenges in modern cities. Understanding how pollutants and weather conditions affect the Air Quality Index (AQI) helps in predicting pollution levels and supporting better environmental decision-making.

This project analyzes air pollution and weather data to identify key factors affecting AQI and builds a machine learning model that predicts AQI based on real-world environmental conditions.

The project also includes a Streamlit web application where users can enter pollution and weather values to predict AQI in real time.

---

## Problem Statement

Air quality is influenced by multiple environmental and atmospheric factors such as:

- PM2.5 and PM10
- gases like NO2, SO2, CO, and O3
- temperature
- precipitation
- wind conditions

It is often difficult to understand:

- which pollutants impact AQI the most
- how weather conditions influence air pollution
- how AQI can be predicted using environmental data

This project addresses these challenges by analyzing pollution data, identifying important factors, building predictive models, and developing an interactive AQI prediction application.

---

## Key Objectives

- Perform data cleaning and merging
- Conduct exploratory data analysis (EDA)
- Understand pollutant and AQI relationships
- Identify the most influential features
- Build machine learning models
- Compare model performance
- Develop a Streamlit AQI prediction application
- Structure the project in a reproducible and professional manner

---

## Dataset

The dataset contains air pollution and weather data combined with AQI values.

### Features Used

- PM2.5
- PM10
- NO2
- SO2
- CO
- O3
- Temperature (minimum)
- Precipitation
- Wind gust

Total rows: 13,979  
No missing values after cleaning and preprocessing.

---

## Exploratory Data Analysis

EDA was performed to understand pollution patterns and relationships between variables.

### Analysis Performed

- correlation matrix
- scatter plots
- distribution analysis
- pollutant vs AQI analysis
- weather vs AQI analysis
- heatmap visualization

This helped identify patterns and relationships that guided model building.

---

## Key Insights

### PM2.5 strongly affects AQI

Higher PM2.5 levels consistently lead to higher AQI values, confirming that PM2.5 is one of the most critical pollutants affecting air quality.

### CO has a strong influence on AQI

CO showed a significant impact in the machine learning model, indicating that industrial and traffic emissions contribute heavily to air pollution.

### Weather affects AQI

Temperature and wind showed noticeable relationships with AQI. Higher wind speeds generally reduce AQI, suggesting that wind helps disperse pollutants.

### Pollutants are correlated

NO, NO2, and NOx showed strong correlations, indicating that they originate from similar emission sources such as vehicles and industrial activity.

---

## Machine Learning Models

Three machine learning models were built and compared.

### Linear Regression

MAE: 33.52  
MSE: 4003.73  
R²: 0.83  

This model provided a strong baseline with good interpretability.

---

### Decision Tree

MAE: 32.41  
MSE: 5334.34  
R²: 0.77  

This model captured non-linear relationships but performed worse than linear regression.

---

### Random Forest (Best Model)

MAE: 23.05  
MSE: 2813.21  
R²: 0.88  

This model achieved the best performance and was selected for deployment.

---

## Final Model

Random Forest Regressor was selected because it:

- produced the lowest prediction error
- achieved the highest R² score
- handled complex relationships between pollutants and weather
- provided stable and reliable predictions

---

## Streamlit AQI Prediction Application

An interactive web application was developed using Streamlit.

### Features

- user input for pollution and weather values
- automatic pollutant unit standardization
- real-time AQI prediction
- AQI category classification
- simple and clean interface

The application allows users to simulate environmental conditions and predict AQI instantly.

---

## Example Prediction

Input values:

PM2.5: 41 
PM10: 50  
NO2: 17  
SO2: 10.44  
CO: 238 ppb  
O3: 35 
Temperature: 23  
Precipitation: 0  
Wind: 7.1  

Output:

Predicted AQI: 112  
Category: Moderate
Actual AQI (on the day of testing): 111

The prediction closely matches real-world AQI values, showing model reliability.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---


## Skills Demonstrated

- data cleaning and preprocessing
- exploratory data analysis
- correlation analysis
- data visualization
- feature selection
- machine learning fundamentals
- model evaluation and comparison
- Streamlit deployment

---

## Project Impact

This project demonstrates the ability to move from raw environmental data to meaningful insights and deploy a predictive model in a real-world application.

It highlights:

- analytical thinking
- structured problem solving
- machine learning understanding
- end-to-end project execution
- practical deployment skills

The workflow follows a complete data pipeline:

raw data → analysis → insights → model → application

which reflects real-world data analytics and machine learning practices.

---

## Future Improvements

- real-time AQI API integration
- city-based AQI prediction
- time-series AQI forecasting
- dashboard visualization
- model optimization
- cloud deployment

---

