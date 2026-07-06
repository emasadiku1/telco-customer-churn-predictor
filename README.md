# 📊 Telco Customer Churn Prediction & Analytics App

A full-stack, interactive machine learning web application that predicts individual customer churn risk and visualizes core risk drivers in real-time. This solution bridges data engineering, predictive modeling, and user interface deployment.

Live Demo: https://telco-customer-churn-predictor-dkkqtkavzabhfbggbb9g8n.streamlit.app/

## 🚀 Project Overview
Customer attrition directly impacts business profitability. This project extracts customer interaction profiles from a localized SQLite relational database, processes features through a custom-engineered Scikit-Learn pipeline, and surfaces real-time classification probabilities through an intuitive Streamlit dashboard.

### Key Engineering Features:
* **Decoupled Preprocessing:** Scalers are applied strictly to continuous columns (`tenure`, `MonthlyCharges`, `TotalCharges`), ensuring categorical binary dummies remain unwarped by variance transformations.
* **Explainable AI UI:** Dynamically displays feature coefficients to explain precisely *why* a customer is flagged as high or low risk.
* **Production-Safe Pipeline:** Fully synchronized data-shaping architecture that guarantees user input structure matches training matrix columns.

## 📁 Project Architecture
```text
telco_project_churn/
│
├── data/              # Raw customer baseline datasets
├── models/            # Serialized model parameters & scaler weights (.pkl)
├── notebooks/         # Exploratory data analysis & model iteration scratchpads
├── app.py             # Streamlit application UI and execution script
├── telco_churn.db     # SQLite source database engine
└── requirements.txt   # Explicit cloud dependency tracking manifest
```

###🛠️ Local Installation & Execution
Follow these steps to replicate the environment and run the application locally:

1. Clone the repository:
```
git clone [https://github.com/emasadiku1/telco-customer-churn-predictor.git](https://github.com/emasadiku1/telco-customer-churn-predictor.git)

cd telco-customer-churn-predictor
```
2. Set up and activate your virtual environment:
```
python -m venv env

#On Windows:
.\env\Scripts\activate

#On Mac/Linux:
source env/bin/activate
```
3. Install the tracked dependencies:
```
pip install -r requirements.txt
```
4. Launch the web application:
```
streamlit run app.py
```
