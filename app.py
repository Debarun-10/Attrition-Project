
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("employee_attrition_model.pkl")

# Load dataset for input options
df = pd.read_csv("employee_attrition.csv")

# Get feature columns from the trained pipeline
preprocessor = model.named_steps["preprocessor"]

num_cols = list(preprocessor.transformers_[0][2])
cat_cols = list(preprocessor.transformers_[1][2])

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("Employee Attrition Prediction")
st.write(
    "Enter employee details below to predict the possibility of attrition."
)

input_data = {}

st.subheader("Employee Details")

col1, col2 = st.columns(2)

for i, feature in enumerate(num_cols):
    with (col1 if i % 2 == 0 else col2):
        minimum = float(df[feature].min())
        maximum = float(df[feature].max())
        default = float(df[feature].median())

        input_data[feature] = st.number_input(
            feature,
            min_value=minimum,
            max_value=maximum,
            value=default
        )

st.subheader("Workplace Details")

col3, col4 = st.columns(2)

for i, feature in enumerate(cat_cols):
    with (col3 if i % 2 == 0 else col4):
        options = sorted(df[feature].dropna().unique().tolist(),
                         key=str)

        input_data[feature] = st.selectbox(
            feature,
            options
        )

if st.button("Predict Attrition"):
    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("The employee is likely to leave the company.")
    else:
        st.success("The employee is likely to stay in the company.")

    st.write(
        f"Attrition Probability: {probability * 100:.2f}%"
    )
