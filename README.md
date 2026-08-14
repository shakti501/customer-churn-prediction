# 📊 Customer Churn Prediction

An end-to-end machine learning project that predicts whether a telecom customer is likely to churn. The project covers data cleaning, exploratory data analysis (EDA), feature engineering, supervised machine learning, model comparison, Random Forest tuning, and a deployed Streamlit prediction application.

<p align="center">
  <a href="https://customer-churn-prediction-shakti.streamlit.app/">
    <strong>🚀 Try the Live Demo</strong>
  </a>
</p>

## 🎯 Project Objective

Customer churn is a major business problem for subscription-based companies. The goal of this project is to identify customers who are more likely to leave so that businesses can take proactive retention actions.

The model uses customer demographic, service, contract, tenure, and billing information to predict the `Churn` outcome.

## 🚀 Live Application

**Live Demo:** https://customer-churn-prediction-shakti.streamlit.app/

The Streamlit application allows users to enter customer information and receive:

- 🔮 Churn prediction
- 📈 Churn probability
- ⚠️ Risk level
- 💡 Business recommendations

The deployed application is connected to this GitHub repository and uses the saved trained model and feature list.

## 🔄 Project Workflow

```mermaid
graph LR
    A[Raw Customer Data] --> B[Data Cleaning]
    B --> C[EDA]
    C --> D[Feature Engineering]
    D --> E[Train/Test Split]
    E --> F[Model Training]
    F --> G[Model Comparison]
    G --> H[Random Forest Tuning]
    H --> I[Saved Model]
    I --> J[Streamlit App]
    J --> K[Churn Prediction]
    K --> L[Business Recommendation]
```

## 📁 Project Structure

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

## 🗃️ Dataset

The working dataset contains **7,032 customers** after cleaning records with missing `TotalCharges` values.

It contains information about:

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

### Target Distribution

| Churn | Customers | Percentage |
|---|---:|---:|
| No | 5,174 | 73.46% |
| Yes | 1,869 | 26.54% |

Because the target is imbalanced, accuracy is considered together with precision, recall, and F1-score.

## 🔍 Exploratory Data Analysis

The analysis examined relationships between churn and customer characteristics including gender, senior-citizen status, partner/dependent status, tenure, monthly charges, total charges, services, and contract type.

### Key Findings

- 👤 Senior citizens had a higher churn rate than non-senior customers.
- 🤝 Customers without partners had a higher churn rate than customers with partners.
- 👨‍👩‍👧 Customers without dependents had a higher churn rate than customers with dependents.
- 📅 Churned customers generally had shorter tenure.
- 💰 Churned customers tended to have higher monthly charges.
- 🔗 Tenure and total charges showed a strong positive correlation of **0.83**.
- 🔗 Monthly charges and total charges showed a positive correlation of **0.65**.

## 🤖 Machine Learning Models

The following supervised learning models were evaluated:

| Model | Accuracy |
|---|---:|
| Logistic Regression | 78.68% |
| Decision Tree | 73.13% |
| Random Forest — Tuned | **79.46%** |
| K-Nearest Neighbors | 74.98% |

### 🏆 Final Model: Tuned Random Forest

The tuned Random Forest achieved the highest test accuracy among the evaluated models at approximately **79.46%**.

| Class | Precision | Recall | F1-score |
|---|---:|---:|---:|
| 0 — No Churn | 0.83 | 0.91 | 0.87 |
| 1 — Churn | 0.66 | 0.48 | 0.55 |
| **Accuracy** | | | **0.79** |

**Test set:** 1,407 customers.

The churn class has lower recall than the no-churn class. In a real business setting, improving churn recall would therefore be an important next step.

## 🖥️ Streamlit Application

The deployed interface is organized into customer information, services, and billing sections. The user enters the customer's attributes and clicks **Predict Churn**.

The application then displays the model prediction, estimated churn probability, risk level, and a simple business recommendation.

### Example Prediction

The application produces results such as:

```text
Prediction Result

🟢 Customer is likely to Stay

Churn Probability: 23.29%

Risk Level: LOW

Business Recommendation:
• Customer is likely to stay.
• Continue providing good service.
• Maintain customer engagement.
```

The probability is model output, not a guarantee of future customer behavior.

## 🧠 Business Recommendations

The application connects the prediction to simple retention-oriented actions.

For customers predicted to be at higher risk, possible actions include:

- Targeted loyalty offers
- Contract incentives
- Technical support follow-ups
- Customer engagement campaigns
- Personalized retention strategies

For lower-risk customers, the application recommends maintaining service quality and engagement.

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Joblib**
- **Streamlit**
- **Jupyter Notebook**

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/shakti501/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app/app.py
```

## 📌 Limitations

- The model does not perfectly identify every customer who will churn.
- Churn-class recall is lower than no-churn recall.
- The model should support business decisions rather than replace human judgment.
- The current application provides rule-based business recommendations rather than a fully optimized retention strategy.

## 🔮 Future Improvements

- Improve recall for the churn class.
- Experiment with class weights and SMOTE.
- Perform cross-validation and broader hyperparameter optimization.
- Add feature-importance visualizations to the application.
- Add more advanced, probability-aware business recommendations.
- Add model monitoring and performance tracking.

## 👤 Author

**Shakti Singh Shekhawat**  
B.Tech Computer Science Engineering Student

GitHub: https://github.com/shakti501

---

⭐ If you find this project useful, feel free to explore the repository and try the live application.