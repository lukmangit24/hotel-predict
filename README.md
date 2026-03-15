# Hotel Booking Cancellation Prediction

## Project Overview

This project aims to predict whether a hotel booking will be **canceled or not** using Machine Learning. The model analyzes reservation information such as booking lead time, customer segment, room type, and other booking details to estimate the probability of cancellation.

By predicting cancellations early, hotels can optimize their reservation strategy and reduce revenue loss caused by last-minute cancellations.

---

## Business Problem

Hotel cancellations can significantly impact revenue, occupancy planning, and operational efficiency.

The main objective of this project is to:

* Predict the **probability of booking cancellation**
* Help hotel management **anticipate potential cancellations**
* Improve **revenue management strategies**

---

## Business Impact

Using this predictive model, hotels can:

* Identify **high-risk bookings**
* Implement **deposit policies** for risky reservations
* Apply **smart overbooking strategies**
* Send **reminder promotions to customers likely to cancel**

---

## Dataset

The dataset contains hotel reservation information such as:

* Hotel type
* Lead time
* Arrival date
* Length of stay
* Customer segment
* Deposit type
* Previous booking history
* Special requests
* Average Daily Rate (ADR)

Target Variable:

```
is_canceled
```

* **1 = Booking canceled**
* **0 = Booking not canceled**

---

## Data Science Workflow

1. Business Understanding
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Preparation
5. Machine Learning Modeling
6. Model Evaluation
7. Model Deployment

---

## Machine Learning Models

Several machine learning models were evaluated:

* Logistic Regression
* K-Nearest Neighbors
* Decision Tree
* Random Forest
* Gradient Boosting
* Naive Bayes
* XGBoost

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC AUC

The **best-performing model** was selected and deployed.


---

## Future Improvements

Possible improvements for this project include:

* Hyperparameter tuning for better performance
* Model explainability using SHAP or feature importance
* Cloud deployment
* Real-time prediction API

---

## Author

Muhammad Lukmanul Hakim

Data Science Project – Hotel Booking Cancellation Prediction
https://hotelprdeic.streamlit.app/
