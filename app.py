import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hotel Booking Cancellation Prediction",
    page_icon="🏨",
    layout="wide"
)

# ======================
# LOAD DATA
# ======================

@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    return df

df = load_data()

# ======================
# BANNER
# ======================

st.image(
    "https://images.unsplash.com/photo-1566073771259-6a8506099945",
    use_container_width=True
)

st.title("🏨 Hotel Booking Cancellation Prediction")

st.markdown(
"""
A Machine Learning project to predict the probability of **hotel booking cancellations**  
based on reservation characteristics.
"""
)

st.markdown("---")

# ======================
# METRIC CARDS
# ======================

total_booking = len(df)

cancel_rate = df["is_canceled"].mean() * 100

revenue = df[df["is_canceled"] == 0]["adr"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Booking", f"{total_booking:,}")

col2.metric("Cancellation Rate", f"{cancel_rate:.2f}%")

col3.metric("Estimated Revenue", f"${revenue:,.0f}")

st.markdown("---")

# ======================
# 2 COLUMN LAYOUT
# ======================

col1, col2 = st.columns(2)

with col1:
    st.header("📊 Project Background")

    st.write("""
    The hotel industry often faces the problem of **booking cancellations**, which can lead to significant revenue loss.

    Hotels need to manage room availability efficiently and develop strategies such as overbooking, deposit policies, and targeted marketing.

    Using **Machine Learning**, we can analyze historical booking data to predict the probability of cancellation.
    """)

    st.header("🚨 Business Problem")

    st.write("""
    The main problem addressed in this project is:

    **Predicting whether a hotel booking will be canceled based on booking characteristics.**

    Frequent cancellations create challenges such as:
    - lost potential revenue
    - inefficient room allocation
    - operational planning difficulties
    """)

with col2:

    st.header("🎯 Project Objectives")

    st.write("""
    The prediction results can help hotels to:

    - Reduce potential losses caused by booking cancellations
    - Optimize overbooking strategies
    - Adjust deposit or prepayment policies
    - Develop better targeted marketing strategies
    """)

    st.header("🤖 Machine Learning Model")

    st.write("""
    The model used in this project is **Random Forest Classifier**.

    Reasons for choosing Random Forest:
    - Works well with tabular data
    - Handles non-linear relationships
    - Robust against overfitting
    - Provides strong prediction performance
    """)

st.markdown("---")

st.success("Use the sidebar to explore EDA, Model Prediction, and provide Feedback.")