# Customer Churn Prediction

A machine learning project that predicts whether a telecom customer is likely to churn. The project covers data cleaning, exploratory data analysis (EDA), feature engineering, supervised machine learning, model comparison, and a Streamlit prediction application.

## Project Overview

Customer churn is a major business problem for subscription-based companies. The goal of this project is to identify customers who are more likely to leave so that businesses can take proactive retention actions.

The project uses customer demographic, service, contract, tenure, and billing information to predict the `Churn` outcome.

## Project Workflow

```text
Raw Customer Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering & Encoding
        ↓
Train/Test Split
        ↓
Model Training
        ↓
Model Evaluation & Comparison
        ↓
Random Forest Tuning
        ↓
Streamlit Prediction App
```

## Dataset

The dataset contains telecom customer information such as:

- Gender
- Senior citizen status
- Partner and dependents
- Tenure
- Phone and internet services
- Online security and backup
- Device protection and technical support
- Streaming services
- Contract type
- Paperless billing
- Payment method
- Monthly charges
- Total charges
- Churn status

The working dataset contains **7,032 customers** after cleaning the records with missing `TotalCharges` values.

### Target Distribution

| Churn | Customers | Percentage |
|---|---:|---:|
| No | 5,174 | 73.46% |
| Yes | 1,869 | 26.54% |

The dataset is imbalanced, so accuracy alone is not sufficient for evaluating the model. Precision, recall, and F1-score are also considered.

## Exploratory Data Analysis

The EDA examined relationships between churn and customer characteristics including:

- Gender
- Senior citizen status
- Partner status
- Dependents
- Tenure
- Monthly charges
- Total charges
- Service and contract-related features

Some important observations from the analysis:

- Senior citizens showed a higher churn rate than non-senior customers.
- Customers without partners had a higher churn rate than customers with partners.
- Customers without dependents had a higher churn rate than customers with dependents.
- Churned customers generally had shorter tenure.
- Churned customers tended to have higher monthly charges.
- Tenure and total charges showed a strong positive relationship (`0.83`).
- Monthly charges and total charges also showed a positive relationship (`0.65`).

## Machine Learning Models

The following models were evaluated:

| Model | Accuracy |
|---|---:|
| Logistic Regression | 78.68% |
| Decision Tree | 73.13% |
| Random Forest (tuned) | **79.46%** |
| K-Nearest Neighbors | 74.98% |

### Final Model

The tuned **Random Forest Classifier** achieved the highest accuracy among the evaluated models at approximately **79.46%** on the test set.

Final test-set results:

| Class | Precision | Recall | F1-score |
|---|---:|---:|---:|
| 0 (No Churn) | 0.83 | 0.91 | 0.87 |
| 1 (Churn) | 0.66 | 0.48 | 0.55 |
| **Accuracy** | | | **0.79** |

Test set size: **1,407 customers**.

The model's churn recall is lower than its no-churn recall. This is important from a business perspective because some customers who eventually churn may still be missed by the model.

## Streamlit Application

The project includes a Streamlit web application that allows a user to enter customer information and receive:

- Churn prediction
- Churn probability
- Risk level
- Business recommendations

The application uses the saved Random Forest model and saved feature list to transform the user inputs into the feature format expected by the model.

## Project Structure

```text
customer-churn-prediction/
│
├── app/
│   └── app.py
│
├── model/
│   ├── customer_churn_model.pkl
│   ├── features.pkl
│   └── scaler.pkl
│
├── Data/
│   └── telecom churn dataset
│
├── Notebooks/
│   └── Task_1.ipynb
│
├── README.md
└── requirements.txt
```

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/shakti501/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app/app.py
```

## Business Use Case

A telecom company can use a churn prediction system to identify customers who may be at higher risk of leaving. Potential retention actions include:

- Targeted loyalty offers
- Contract upgrades or discounts
- Technical support follow-ups
- Customer engagement campaigns
- Personalized retention strategies

The predictions should be treated as decision-support information rather than guaranteed outcomes.

## Future Improvements

- Improve recall for the churn class.
- Experiment with class balancing techniques such as SMOTE or class weights.
- Add cross-validation and hyperparameter optimization.
- Add feature importance visualizations to the application.
- Deploy the Streamlit application publicly.
- Add model monitoring and performance tracking.

## Author

**Shakti Singh Shekhawat**

B.Tech Computer Science Engineering Student

GitHub: https://github.com/shakti501

---

If you find this project useful, feel free to explore the repository and provide feedback.