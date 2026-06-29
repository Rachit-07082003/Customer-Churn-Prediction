import streamlit as st
from src.predict import predict

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")

st.write("""
Predict whether a customer is likely to churn using a trained
Random Forest Machine Learning model.
""")

st.markdown("---")
st.subheader("Customer Information")

# -----------------------------
# Customer Input
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    phone = st.selectbox("Phone Service", ["No", "Yes"])
    multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])

with col2:
    protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["No", "Yes"])

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0
    )

# -----------------------------
# Convert Inputs to Numbers
# -----------------------------

gender = 1 if gender == "Male" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0
phone = 1 if phone == "Yes" else 0
paperless = 1 if paperless == "Yes" else 0

multiple = {
    "No": 0,
    "Yes": 1,
    "No phone service": 2
}[multiple]

internet = {
    "DSL": 0,
    "Fiber optic": 1,
    "No": 2
}[internet]

security = {
    "No": 0,
    "Yes": 1,
    "No internet service": 2
}[security]

backup = {
    "No": 0,
    "Yes": 1,
    "No internet service": 2
}[backup]

protection = {
    "No": 0,
    "Yes": 1,
    "No internet service": 2
}[protection]

support = {
    "No": 0,
    "Yes": 1,
    "No internet service": 2
}[support]

streaming_tv = {
    "No": 0,
    "Yes": 1,
    "No internet service": 2
}[streaming_tv]

streaming_movies = {
    "No": 0,
    "Yes": 1,
    "No internet service": 2
}[streaming_movies]

contract = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}[contract]

payment = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3
}[payment]

monthly = float(monthly)
total = float(total)

# -----------------------------
# Customer Data
# -----------------------------
customer = {
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone,
    "MultipleLines": multiple,
    "InternetService": internet,
    "OnlineSecurity": security,
    "OnlineBackup": backup,
    "DeviceProtection": protection,
    "TechSupport": support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless,
    "PaymentMethod": payment,
    "MonthlyCharges": monthly,
    "TotalCharges": total
}

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Churn"):

    prediction = predict(customer)

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")