Hotel Booking Cancellation Prediction
Project Overview

This project aims to predict whether a hotel booking will be canceled or not using Machine Learning.
The model analyzes reservation information such as booking lead time, customer segment, room type, and other booking details to estimate the probability of cancellation.

By predicting cancellations early, hotels can optimize their reservation strategy and reduce revenue loss caused by last-minute cancellations.

Business Problem

Hotel cancellations can significantly impact revenue, occupancy planning, and operational efficiency.

The main objective of this project is:

Predict the probability of booking cancellation

Help hotel management anticipate potential cancellations

Improve revenue management strategies

Business Impact

Using this predictive model, hotels can:

Identify high-risk bookings

Implement deposit policies for risky reservations

Apply smart overbooking strategies

Send reminder promotions to customers likely to cancel

Dataset

The dataset contains hotel reservation information such as:

Hotel type

Lead time

Arrival date

Length of stay

Customer segment

Deposit type

Previous booking history

Special requests

Average daily rate (ADR)

Target variable:

is_canceled

1 = Booking canceled

0 = Booking not canceled

Data Science Workflow

Business Understanding

Data Cleaning and Preprocessing

Exploratory Data Analysis (EDA)

Feature Preparation

Machine Learning Modeling

Model Evaluation

Model Deployment

Models Used

Several Machine Learning models were tested:

Logistic Regression

K-Nearest Neighbors

Decision Tree

Random Forest

Gradient Boosting

Naive Bayes

XGBoost

Model comparison used the following metrics:

Accuracy

Precision

Recall

F1 Score

ROC AUC

The best performing model was selected and deployed.

Model Deployment

The trained model is deployed using Streamlit to create an interactive web application where users can input booking information and get a cancellation prediction.

Streamlit App

The application allows users to:

Input booking information

Predict booking cancellation

See cancellation probability

To run the app locally:

streamlit run app.py
Project Structure
hotel-predict
│
├── app.py
├── best_model.pkl
├── notebook.ipynb
├── requirements.txt
└── README.md
Installation

Clone the repository:

git clone https://github.com/yourusername/hotel-predict.git
cd hotel-predict

Create environment:

conda create -n hotel_ml python=3.10
conda activate hotel_ml

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py
Technologies Used

Python

Pandas

NumPy

Scikit-learn

XGBoost

Streamlit

Future Improvements

Possible improvements for this project:

Hyperparameter optimization

Model explainability (SHAP / Feature Importance)

Deployment to cloud platform

Real-time prediction API

Author

Muhammad Lukmanul Hakim

Data Science Project – Hotel Booking Cancellation Prediction