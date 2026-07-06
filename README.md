# 📊 Telco Customer Churn Prediction & Analytics App

An end-to-end machine learning application that predicts customer churn risk and provides insights into the factors influencing each prediction. The project demonstrates the complete data science workflow, from data storage and preprocessing to model deployment using Streamlit.

## 🌐 Live Demo

https://telco-customer-churn-predictor-dkkqtkavzabhfbggbb9g8n.streamlit.app/


# 🚀 Project Overview

Customer churn is a major challenge for subscription-based businesses. Identifying customers who are likely to leave allows companies to take proactive retention measures.

This project uses the **IBM Telco Customer Churn** dataset to build a machine learning model capable of predicting whether a customer is likely to churn based on their account information and service usage.

The application provides an intuitive web interface where users can enter customer information, receive a churn probability, and understand which features contributed most to the prediction.


# 📂 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

- 7,043 customer records
- 21 original features
- Binary target variable (`Churn`)

To simplify the user experience, the deployed application focuses on eight key features:

- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Internet Service
- Payment Method
- Paperless Billing
- Tech Support


# 🛠️ Tech Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- Logistic Regression

### Database

- SQLite
- SQL

### Deployment

- Streamlit

### Model Serialization

- Joblib


# ⚙️ Machine Learning Workflow

```
CSV Dataset
      │
      ▼
SQLite Database
      │
      ▼
SQL Data Extraction
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Encoding & Scaling
      │
      ▼
Train/Test Split
      │
      ▼
Model Training
(Logistic Regression, Random Forest, XGBoost)
      │
      ▼
Model Evaluation
      │
      ▼
Winning Logistic Regression Model
      │
      ▼
Streamlit Deployment
```


# 🤖 Model Selection

Several classification algorithms were trained and evaluated:

- Logistic Regression
- Random Forest
- XGBoost

After comparing their performance, **Logistic Regression** was selected as the final model because it achieved the best overall balance between predictive performance and interpretability.

The deployed application uses the trained model stored as:

```
winning_churn_model.pkl
```


# 📈 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | **79.4%** |
| Precision (Churn) | **63%** |
| Recall (Churn) | **53%** |
| F1-score (Churn) | **58%** |

Although more complex models were evaluated, Logistic Regression provided the most consistent performance while allowing direct interpretation of feature coefficients.


# ✨ Application Features

The deployed web application allows users to:

- Enter customer information through an interactive form
- Predict customer churn probability in real time
- Display the estimated churn percentage
- Categorize customers as Low Risk or High Risk
- Visualize the most influential features contributing to the prediction
- Ensure consistent preprocessing between model training and prediction


# 🗄️ Database Workflow

Rather than training directly from a CSV file, this project follows a database-driven workflow.

1. The raw dataset is imported into an SQLite database.
2. Customer data is queried using SQL.
3. The extracted data is loaded into Pandas.
4. Features are preprocessed and used for model training.

This mirrors a common workflow used in production data science environments where models are trained using data stored in relational databases.


# 📁 Project Structure

```
telco-customer-churn-predictor/
│
├── data/
├── models/
├── notebooks/
├── app.py
├── init_db.py
├── telco_churn.db
├── requirements.txt
└── README.md
```


# 💻 Local Installation

Clone the repository

```bash
git clone https://github.com/emasadiku1/telco-customer-churn-predictor.git

cd telco-customer-churn-predictor
```

Create a virtual environment

```bash
python -m venv env
```

Activate the environment

Windows

```bash
.\env\Scripts\activate
```

macOS/Linux

```bash
source env/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```


# 🔮 Future Improvements

Possible enhancements include:

- Hyperparameter tuning
- Cross-validation
- Probability calibration
- SHAP-based explainability
- Docker containerization
- FastAPI deployment
- PostgreSQL integration
- Cloud deployment using AWS or Azure


# 👩‍💻 Author

**Ema Sadiku**

GitHub:
https://github.com/emasadiku1
