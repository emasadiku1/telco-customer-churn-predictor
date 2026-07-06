import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Page layout configuration
st.set_page_config(page_title="Telco Customer Churn Predictor", page_icon="📊", layout="centered")

st.title("📊 Telco Customer Churn Prediction App")
st.markdown("Enter customer details below to predict the probability of them leaving the service.")

# 2. Load the trained model and scaler artifacts
@st.cache_resource
def load_artifacts():
    model = joblib.load('models/winning_churn_model.pkl')
    scaler = joblib.load('models/scaler.pkl')
    features = joblib.load('models/model_features.pkl')
    return model, scaler, features

try:
    model, scaler, features = load_artifacts()
except Exception as e:
    st.error("Could not load model artifacts. Ensure they are in the 'models/' folder.")
    st.stop()

# 3. Create clean user form layout blocks
st.header("👤 Customer Profile")
col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (Months)", min_value=1, max_value=72, value=12)
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=10.0, max_value=150.0, value=65.0)
    total_charges = st.number_input("Total Charges ($)", min_value=10.0, max_value=9000.0, value=780.0)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

with col2:
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

# 4. On-click calculations execution block
if st.button("Predict Churn Probability"):
    
    # Scale ONLY the continuous numeric inputs using our updated scaler
    numeric_inputs = pd.DataFrame([[tenure, monthly_charges, total_charges]], columns=['tenure', 'MonthlyCharges', 'TotalCharges'])
    scaled_numeric = scaler.transform(numeric_inputs)[0]
    
    # Initialize dictionary matching ALL streamlined trained features starting at 0
    encoded_inputs = {feat: 0 for feat in features}
    
    # Insert the scaled continuous variables
    encoded_inputs['tenure'] = scaled_numeric[0]
    encoded_inputs['MonthlyCharges'] = scaled_numeric[1]
    encoded_inputs['TotalCharges'] = scaled_numeric[2]
    
    # Map contract categories
    if contract == "One year" and 'Contract_One year' in encoded_inputs:
        encoded_inputs['Contract_One year'] = 1
    elif contract == "Two year" and 'Contract_Two year' in encoded_inputs:
        encoded_inputs['Contract_Two year'] = 1
        
    # Map internet service categories
    if internet_service == "Fiber optic" and 'InternetService_Fiber optic' in encoded_inputs:
        encoded_inputs['InternetService_Fiber optic'] = 1
    elif internet_service == "No" and 'InternetService_No' in encoded_inputs:
        encoded_inputs['InternetService_No'] = 1
        
    # Map payment method categories
    if payment_method == "Credit card (automatic)" and 'PaymentMethod_Credit card (automatic)' in encoded_inputs:
        encoded_inputs['PaymentMethod_Credit card (automatic)'] = 1
    elif payment_method == "Electronic check" and 'PaymentMethod_Electronic check' in encoded_inputs:
        encoded_inputs['PaymentMethod_Electronic check'] = 1
    elif payment_method == "Mailed check" and 'PaymentMethod_Mailed check' in encoded_inputs:
        encoded_inputs['PaymentMethod_Mailed check'] = 1
        
    # Map paperless billing categories
    if paperless == "Yes" and 'PaperlessBilling_Yes' in encoded_inputs:
        encoded_inputs['PaperlessBilling_Yes'] = 1
        
    # Map tech support categories
    if tech_support == "No internet service" and 'TechSupport_No internet service' in encoded_inputs:
        encoded_inputs['TechSupport_No internet service'] = 1
    elif tech_support == "Yes" and 'TechSupport_Yes' in encoded_inputs:
        encoded_inputs['TechSupport_Yes'] = 1

    # Convert dictionary into DataFrame matching the exact trained order
    input_df = pd.DataFrame([encoded_inputs])[features]
    
    # Calculate genuine mathematical probabilities directly from features
    probability = model.predict_proba(input_df)[0][1]
    
    # 5. UI Render Output
    st.markdown("---")
    st.subheader("🔮 Prediction Results")
    
    if probability >= 0.5:
        st.error(f"⚠️ High Risk of Churn! Probability: {probability:.2%}")
    else:
        st.success(f"✅ Low Risk. Customer likely to stay. Probability of leaving: {probability:.2%}")

    # 📊 Key Churn Drivers Visualization Feature
    st.markdown("---")
    st.subheader("📊 Key Churn Drivers")
    st.markdown("Here are the top factors our model analyzes to determine if a customer is at risk:")
    
    try:
        # Extract the weight coefficients directly from the loaded model
        coefficients = model.coef_[0]
        
        # Match coefficients to their exact features list positioning 
        importance_df = pd.DataFrame({
            'Feature': features,
            'Importance': coefficients
        }).sort_values(by='Importance', ascending=True)
        
        # Render native interactive bar chart
        st.bar_chart(data=importance_df, x='Feature', y='Importance', use_container_width=True)
        st.caption("💡 Negative values decrease risk (keep customers), positive values increase risk (predict churn).")
        
    except Exception as e:
        st.info("Visual analytics chart ready for deployment configuration.")