import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Load model
# ----------------------------

model = joblib.load("../model/customer_churn_model.pkl")
features = joblib.load("../model/features.pkl")

# ----------------------------
# Header
# ----------------------------

st.title("📊 Customer Churn Prediction System")

st.write(
    "Predict whether a customer is likely to churn using Machine Learning."
)

# ----------------------------
# KPI Cards
# ----------------------------

col1,col2,col3 = st.columns(3)

col1.metric("Model","Random Forest")
col2.metric("Accuracy","79.46%")
col3.metric("Customers","7032")

st.divider()

st.subheader("👤 Customer Information")

c1,c2 = st.columns(2)

gender = c1.selectbox(
    "Gender",
    ["Male","Female"]
)

senior = c2.selectbox(
    "Senior Citizen",
    ["No","Yes"]
)

partner = c1.selectbox(
    "Partner",
    ["No","Yes"]
)

dependents = c2.selectbox(
    "Dependents",
    ["No","Yes"]
)

tenure = st.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

st.divider()

st.subheader("📡 Services")

c1,c2 = st.columns(2)

phone = c1.selectbox(
    "Phone Service",
    ["Yes","No"]
)

multiple = c2.selectbox(
    "Multiple Lines",
    ["No","Yes","No phone service"]
)

internet = c1.selectbox(
    "Internet Service",
    ["DSL","Fiber optic","No"]
)

security = c2.selectbox(
    "Online Security",
    ["No","Yes","No internet service"]
)

backup = c1.selectbox(
    "Online Backup",
    ["No","Yes","No internet service"]
)

device = c2.selectbox(
    "Device Protection",
    ["No","Yes","No internet service"]
)

support = c1.selectbox(
    "Tech Support",
    ["No","Yes","No internet service"]
)

tv = c2.selectbox(
    "Streaming TV",
    ["No","Yes","No internet service"]
)

movies = c1.selectbox(
    "Streaming Movies",
    ["No","Yes","No internet service"]
)

st.divider()

st.subheader("💳 Billing")

c1,c2 = st.columns(2)

contract = c1.selectbox(
    "Contract",
    ["Month-to-month","One year","Two year"]
)

paperless = c2.selectbox(
    "Paperless Billing",
    ["Yes","No"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly = st.slider(
    "Monthly Charges",
    18.0,
    120.0,
    70.0
)

total = st.number_input(
    "Total Charges",
    value=1000.0
)

input_data = {feature: 0 for feature in features}

# Numerical Features
input_data["SeniorCitizen"] = 1 if senior == "Yes" else 0
input_data["tenure"] = tenure
input_data["MonthlyCharges"] = monthly
input_data["TotalCharges"] = total

if "gender_Male" in input_data:
    input_data["gender_Male"] = 1 if gender == "Male" else 0

if "Partner_Yes" in input_data:
    input_data["Partner_Yes"] = 1 if partner == "Yes" else 0

if "Dependents_Yes" in input_data:
    input_data["Dependents_Yes"] = 1 if dependents == "Yes" else 0

if "PhoneService_Yes" in input_data:
    input_data["PhoneService_Yes"] = 1 if phone == "Yes" else 0

if "MultipleLines_No phone service" in input_data:
    input_data["MultipleLines_No phone service"] = (
        1 if multiple == "No phone service" else 0
    )

if "MultipleLines_Yes" in input_data:
    input_data["MultipleLines_Yes"] = (
        1 if multiple == "Yes" else 0
    )

if "InternetService_Fiber optic" in input_data:
    input_data["InternetService_Fiber optic"] = (
        1 if internet == "Fiber optic" else 0
    )

if "InternetService_No" in input_data:
    input_data["InternetService_No"] = (
        1 if internet == "No" else 0
    )

if "OnlineSecurity_No internet service" in input_data:
    input_data["OnlineSecurity_No internet service"] = (
        1 if security == "No internet service" else 0
    )

if "OnlineSecurity_Yes" in input_data:
    input_data["OnlineSecurity_Yes"] = (
        1 if security == "Yes" else 0
    )

if "OnlineBackup_No internet service" in input_data:
    input_data["OnlineBackup_No internet service"] = (
        1 if backup == "No internet service" else 0
    )

if "OnlineBackup_Yes" in input_data:
    input_data["OnlineBackup_Yes"] = (
        1 if backup == "Yes" else 0
    )

if "DeviceProtection_No internet service" in input_data:
    input_data["DeviceProtection_No internet service"] = (
        1 if device == "No internet service" else 0
    )

if "DeviceProtection_Yes" in input_data:
    input_data["DeviceProtection_Yes"] = (
        1 if device == "Yes" else 0
    )

if "TechSupport_No internet service" in input_data:
    input_data["TechSupport_No internet service"] = (
        1 if support == "No internet service" else 0
    )

if "TechSupport_Yes" in input_data:
    input_data["TechSupport_Yes"] = (
        1 if support == "Yes" else 0
    )

if "StreamingTV_No internet service" in input_data:
    input_data["StreamingTV_No internet service"] = (
        1 if tv == "No internet service" else 0
    )

if "StreamingTV_Yes" in input_data:
    input_data["StreamingTV_Yes"] = (
        1 if tv == "Yes" else 0
    )

if "StreamingMovies_No internet service" in input_data:
    input_data["StreamingMovies_No internet service"] = (
        1 if movies == "No internet service" else 0
    )

if "StreamingMovies_Yes" in input_data:
    input_data["StreamingMovies_Yes"] = (
        1 if movies == "Yes" else 0
    )

if "Contract_One year" in input_data:
    input_data["Contract_One year"] = (
        1 if contract == "One year" else 0
    )

if "Contract_Two year" in input_data:
    input_data["Contract_Two year"] = (
        1 if contract == "Two year" else 0
    )

if "PaperlessBilling_Yes" in input_data:
    input_data["PaperlessBilling_Yes"] = (
        1 if paperless == "Yes" else 0
    )

if "PaymentMethod_Credit card (automatic)" in input_data:
    input_data["PaymentMethod_Credit card (automatic)"] = (
        1 if payment == "Credit card (automatic)" else 0
    )

if "PaymentMethod_Electronic check" in input_data:
    input_data["PaymentMethod_Electronic check"] = (
        1 if payment == "Electronic check" else 0
    )

if "PaymentMethod_Mailed check" in input_data:
    input_data["PaymentMethod_Mailed check"] = (
        1 if payment == "Mailed check" else 0
    )



st.divider()

st.divider()

if st.button("🔍 Predict Churn", use_container_width=True):

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🔴 Customer is likely to Churn")
    else:
        st.success("🟢 Customer is likely to Stay")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    if probability < 0.30:
        st.success("🟢 Risk Level : LOW")

    elif probability < 0.70:
        st.warning("🟡 Risk Level : MEDIUM")

    else:
        st.error("🔴 Risk Level : HIGH")

    st.subheader("Business Recommendation")

    if prediction == 1:

        st.write("• Offer loyalty discount")

        st.write("• Encourage annual contract")

        st.write("• Assign dedicated customer support")

        st.write("• Follow up with the customer")

    else:

        st.write("• Customer is likely to stay.")

        st.write("• Continue providing good service.")

        st.write("• Maintain customer engagement.")