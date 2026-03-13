import streamlit as st
import pandas as pd
import joblib

st.title("Hotel Booking Cancellation Prediction")

# Load model
model = joblib.load("best_model2.pkl")

st.write("Masukkan informasi reservasi:")

# Input dari user
lead_time = st.number_input("Lead Time", 0, 365, 30)
adr = st.number_input("ADR (Average Daily Rate)", 0.0, 500.0, 100.0)
adults = st.number_input("Adults", 1, 5, 2)
children = st.number_input("Children", 0, 5, 0)

# Data lengkap sesuai fitur training
input_data = {
    "hotel": "City Hotel",
    "lead_time": lead_time,
    "arrival_date_year": 2017,
    "arrival_date_month": "July",
    "arrival_date_week_number": 30,
    "arrival_date_day_of_month": 15,
    "stays_in_weekend_nights": 1,
    "stays_in_week_nights": 2,
    "adults": adults,
    "children": children,
    "babies": 0,
    "meal": "BB",
    "country": "PRT",
    "market_segment": "Online TA",
    "distribution_channel": "TA/TO",
    "is_repeated_guest": 0,
    "previous_cancellations": 0,
    "previous_bookings_not_canceled": 0,
    "reserved_room_type": "A",
    "assigned_room_type": "A",
    "booking_changes": 0,
    "deposit_type": "No Deposit",
    "agent": 0,
    "days_in_waiting_list": 0,
    "customer_type": "Transient",
    "adr": adr,
    "required_car_parking_spaces": 0,
    "total_of_special_requests": 0
}

input_df = pd.DataFrame([input_data])

# Tombol prediksi
if st.button("Predict"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error("Booking kemungkinan akan dibatalkan")
    else:
        st.success("Booking kemungkinan tidak dibatalkan")

    st.write(f"Probability Cancel: {round(probability*100,2)}%")