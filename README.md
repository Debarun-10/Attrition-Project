# Attrition-Project
Machine Learning project to predict employee attrition using Random Forest and Streamlit
# Employee Attrition Prediction

## Project Overview

Employee Attrition Prediction is a Machine Learning project that aims to predict whether an employee is likely to leave an organization.

The project analyses different employee-related factors such as age, job role, monthly income, job satisfaction, overtime, work experience and other workplace attributes to identify patterns associated with employee attrition.

The main objective is to explore employee data, understand the factors associated with attrition and build a machine learning model that can make predictions based on employee details.

## Dataset

- **Dataset Name:** IBM HR Analytics Employee Attrition & Performance
- **Total Records:** 1,470 employees
- **Original Features:** 31 columns
- **Target Variable:** Attrition (Yes/No)

## Technologies and Libraries Used

- Python
- Pandas – Data manipulation and analysis
- NumPy – Numerical operations
- Matplotlib – Data visualization
- Seaborn – Statistical visualization
- Scikit-learn – Machine Learning and model evaluation
- Streamlit – Web application development
- Joblib – Saving and loading the trained model

## Project Workflow

### 1. Data Collection
Loaded the IBM HR Analytics Employee Attrition dataset for analysis.

### 2. Data Cleaning
Checked for missing values, duplicate records, data types and unnecessary columns.

### 3. Exploratory Data Analysis (EDA)
Used graphs and statistical analysis to explore attrition patterns based on factors such as overtime, department, job satisfaction, age, monthly income and distance from home.

### 4. Data Preprocessing
Separated numerical and categorical features and applied suitable preprocessing techniques, including missing-value imputation and one-hot encoding.

### 5. Model Training
Trained and evaluated machine learning models, including:
- Logistic Regression
- Random Forest Classifier

### 6. Model Evaluation
Evaluated model performance using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### 7. Deployment
Developed an interactive web application using Streamlit to allow users to enter employee details and receive attrition predictions.

## Machine Learning Model

The final saved model uses a **Random Forest Classifier** integrated with a Scikit-learn preprocessing pipeline.

The pipeline handles numerical and categorical data before making predictions.

## Project Structure


Attrition-Project/
│
├── app.py
├── employee attrition.ipynb
├── employee_attrition_model.pkl
├── employee_attrition.csv
├── requirements.txt
└── README.md


## How to Run the Project Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/Debarun-10/Attrition-Project.git
```

### Step 2: Open the project folder

```bash
cd Attrition-Project
```

### Step 3: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit application

```bash
streamlit run app.py
```

## Live Demo

https://attrition-project-ezmgkwcpvpuunp6adzy3yq.streamlit.app/

## Disclaimer

This project is developed for educational purposes as part of a Machine Learning project. The predictions are based on the available dataset and should not be considered definitive decisions about employees.
