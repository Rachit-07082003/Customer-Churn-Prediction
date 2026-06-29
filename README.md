# Telco Customer Churn Prediction & Retention System
```md
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
```


An end-to-end Machine Learning project to predict customer churn (attrition) using the **IBM Telco Customer Churn dataset**. The project includes exploratory data analysis (EDA), data preprocessing, class balancing using SMOTE, model training and comparison (Logistic Regression, Decision Tree, Random Forest), and an interactive **Streamlit web application** for real-time predictions and customer retention recommendations.

---

## 🚀 Project Overview & Key Features

* **Data Preprocessing & Cleaning**: Handled missing values (specifically in `TotalCharges`), dropped non-predictive features (`customerID`), and encoded categorical variables using custom `LabelEncoder` mappings.
* **Class Balancing (SMOTE)**: Dealt with class imbalance (more non-churners than churners) in the training dataset using Synthetic Minority Over-sampling Technique (SMOTE).
* **Machine Learning Pipeline**: Trained and evaluated three models:
  * **Logistic Regression** (with Feature Scaling)
  * **Decision Tree**
  * **Random Forest** (Best Performing Model: **~80.1% accuracy**)
* **Interactive Streamlit Web App**: A beautiful, premium, tabbed dashboard built to accept customer details and provide real-time churn predictions with actionable retention strategies.
* **Pre-fit Encoders**: Encoded mappings are stored separately in `models/encoders.pkl` and dynamically applied to streamlit user inputs, resolving encoding misalignment.

---
````md
## 🔄 Project Workflow

```text
IBM Telco Customer Churn Dataset
                │
                ▼
      Data Cleaning & Preprocessing
                │
                ▼
      Exploratory Data Analysis
                │
                ▼
        Label Encoding
                │
                ▼
        Train-Test Split
                │
                ▼
             SMOTE
                │
                ▼
      Model Training
      ├── Logistic Regression
      ├── Decision Tree
      └── Random Forest
                │
                ▼
      Model Evaluation
                │
                ▼
      Best Model Selection
                │
                ▼
      Save Model (.pkl)
                │
                ▼
      Streamlit Web Application
                │
                ▼
      Real-Time Churn Prediction
```
````


## 📁 Project Folder Structure

```text
Customer-Churn-Prediction/
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Telco Churn CSV Dataset
├── models/
│   ├── churn_model.pkl                        # Trained Random Forest Model
│   └── encoders.pkl                           # Fitted Label Encoders Dictionary
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb       # Jupyter Notebook for EDA & Training
├── src/                                       # Source code folder (for modular utilities)
├── app.py                                     # Streamlit Web App entry point
├── requirements.txt                           # Project dependencies
└── README.md                                  # Project documentation (this file)
```

---

## 📊 Dataset & Feature Dictionary

The dataset consists of **7,043 rows** and **21 columns**, representing customer info at a fictional telecom company.

| Feature Name | Description | Type |
| :--- | :--- | :--- |
| `gender` | Customer's gender (Female, Male) | Categorical |
| `SeniorCitizen` | Whether the customer is a senior citizen (1, 0) | Numeric (Binary) |
| `Partner` | Whether the customer has a partner (Yes, No) | Categorical |
| `Dependents` | Whether the customer has dependents (Yes, No) | Categorical |
| `tenure` | Number of months the customer has stayed with the company | Numeric |
| `PhoneService` | Whether the customer has a phone service (Yes, No) | Categorical |
| `MultipleLines` | Whether the customer has multiple lines (Yes, No, No phone service) | Categorical |
| `InternetService` | Customer’s internet service provider (DSL, Fiber optic, No) | Categorical |
| `OnlineSecurity` | Whether the customer has online security (Yes, No, No internet service) | Categorical |
| `OnlineBackup` | Whether the customer has online backup (Yes, No, No internet service) | Categorical |
| `DeviceProtection` | Whether the customer has device protection (Yes, No, No internet service) | Categorical |
| `TechSupport` | Whether the customer has tech support (Yes, No, No internet service) | Categorical |
| `StreamingTV` | Whether the customer has streaming TV (Yes, No, No internet service) | Categorical |
| `StreamingMovies` | Whether the customer has streaming movies (Yes, No, No internet service) | Categorical |
| `Contract` | The contract term of the customer (Month-to-month, One year, Two year) | Categorical |
| `PaperlessBilling` | Whether the customer has paperless billing (Yes, No) | Categorical |
| `PaymentMethod` | The customer’s payment method (Electronic check, Mailed check, etc.) | Categorical |
| `MonthlyCharges` | The amount charged to the customer monthly | Numeric |
| `TotalCharges` | The total amount charged to the customer | Numeric |
| `Churn` | Whether the customer churned or not (Yes, No) — **Target Variable** | Categorical |

---

## 📈 Model Performance Comparison

The following models were trained and compared using an 80/20 train-test split:

| Model | Scaling Applied | Class Balancing | Accuracy |
| :--- | :---: | :---: | :---: |
| **Logistic Regression** | Yes | SMOTE | ~75% |
| **Decision Tree** | No | SMOTE | ~73% |
| **Random Forest** (Best) | **No** | **SMOTE** | **~80.1%** |

The **Random Forest** model was chosen due to its high accuracy and robustness to outliers/noise. It has been serialized and saved to `models/churn_model.pkl`.

---

## 🛠️ Installation & Setup Instructions

### Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### 1. Clone or Open the Directory
Navigate to the root directory `Customer-Churn-Prediction`.

### 2. Install Dependencies
Install all the required python packages using:
```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit Web Application
To run the web app locally, execute:
```bash
streamlit run app.py
```
This will start a local web server, and a browser window should automatically open at `http://localhost:8501`.

---

## 💡 Using the Web Application

1. **Input Customer Details**: 
   - **Demographics Tab**: Specify Gender, Senior status, Partner, and Dependents.
   - **Services Tab**: Configure Phone/Internet services, Streaming add-ons, Online Security, and Tech Support.
   - **Billing & Contract Tab**: Set Contract type, Tenure (0-72 months), Monthly charges, and Total charges.
2. **Make Prediction**: Click the **Predict Churn Risk** button.
3. **Analyze Output**:
   - The app displays a clear green/red status block along with the churn probability percentage.
   - **High Churn Risk (>= 50%)**: Displays key retention strategies such as pitching 1 or 2-year contracts, security/tech support bundles, and billing incentives.
   - **Low Churn Risk (< 50%)**: Displays customer relationship practices to maintain loyalty.

---

## 🔮 Future Enhancements (Roadmap)

1. **Model Upgrades**: Implement **XGBoost** and **LightGBM** classifiers to check if prediction performance can be further improved.
2. **Deep Learning**: Train a simple multi-layer perceptron (Neural Network) using TensorFlow/Keras.
3. **Hyperparameter Tuning**: Run RandomizedSearchCV or GridSearchCV to find the optimal hyperparameters for the Random Forest model.
4. **Cloud Deployment**: Deploy the Streamlit application to **Streamlit Community Cloud**, Heroku, or AWS Elastic Beanstalk.
5. **Database Integration**: Store predictions and customer input history in a SQLite or PostgreSQL database for auditing and retrain monitoring.
