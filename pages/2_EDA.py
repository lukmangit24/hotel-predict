import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Exploratory Data Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    return df

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.markdown("---")

# 1 Cancellation Distribution
st.subheader("1️⃣ Booking Cancellation Distribution")

fig, ax = plt.subplots()
sns.countplot(x="is_canceled", data=df, ax=ax)
ax.set_title("Booking Cancellation Distribution")

st.pyplot(fig)

st.write("""
Insight:
Sebagian booking tidak dibatalkan, namun jumlah pembatalan masih cukup besar sehingga
perlu strategi untuk mengurangi cancellation.
""")

st.markdown("---")

# 2 Lead Time vs Cancellation
st.subheader("2️⃣ Lead Time vs Cancellation")

fig, ax = plt.subplots()
sns.boxplot(x="is_canceled", y="lead_time", data=df, ax=ax)

st.pyplot(fig)

st.write("""
Insight:
Booking dengan **lead time yang lebih lama** cenderung memiliki kemungkinan
pembatalan lebih tinggi.
""")

st.markdown("---")

# 3 Market Segment
st.subheader("3️⃣ Market Segment vs Cancellation")

fig, ax = plt.subplots(figsize=(8,4))
sns.countplot(x="market_segment", hue="is_canceled", data=df, ax=ax)
plt.xticks(rotation=45)

st.pyplot(fig)

st.write("""
Insight:
Segment **Online Travel Agent (OTA)** memiliki tingkat pembatalan lebih tinggi.
""")

st.markdown("---")

# 4 Deposit Type
st.subheader("4️⃣ Deposit Type vs Cancellation")

fig, ax = plt.subplots()
sns.countplot(x="deposit_type", hue="is_canceled", data=df, ax=ax)

st.pyplot(fig)

st.write("""
Insight:
Booking dengan **No Deposit** lebih sering dibatalkan dibandingkan
booking dengan deposit.
""")

st.markdown("---")

# 5 Distribution Channel
st.subheader("5️⃣ Distribution Channel")

fig, ax = plt.subplots()
sns.countplot(x="distribution_channel", data=df, ax=ax)

st.pyplot(fig)

st.write("""
Insight:
Sebagian besar booking berasal dari channel **TA/TO (Travel Agent)**.
""")

st.markdown("---")

# 6 ADR Distribution
st.subheader("6️⃣ ADR Distribution")

fig, ax = plt.subplots()
sns.histplot(df["adr"], bins=30, ax=ax)

st.pyplot(fig)

st.write("""
Insight:
Sebagian besar harga kamar berada pada rentang ADR tertentu,
namun terdapat beberapa booking dengan harga sangat tinggi.
""")

st.markdown("---")

# 7 Booking per Month
st.subheader("7️⃣ Booking per Month")

fig, ax = plt.subplots(figsize=(8,4))
sns.countplot(x="arrival_date_month", data=df, ax=ax,
              order=df['arrival_date_month'].value_counts().index)

plt.xticks(rotation=45)

st.pyplot(fig)

st.write("""
Insight:
Beberapa bulan menunjukkan tingkat booking yang lebih tinggi,
menunjukkan adanya **seasonality dalam industri hotel**.
""")

st.markdown("---")

# 8 Special Requests
st.subheader("8️⃣ Special Requests vs Cancellation")

fig, ax = plt.subplots()
sns.countplot(x="total_of_special_requests", hue="is_canceled", data=df, ax=ax)

st.pyplot(fig)

st.write("""
Insight:
Tamu yang membuat **lebih banyak special requests** cenderung
lebih kecil kemungkinan membatalkan reservasi.
""")

st.markdown("---")

# 9 Customer Type
st.subheader("9️⃣ Customer Type")

fig, ax = plt.subplots()
sns.countplot(x="customer_type", data=df, ax=ax)

st.pyplot(fig)

st.write("""
Insight:
Mayoritas pelanggan adalah tipe **Transient** (individual traveler).
""")

st.markdown("---")

# 10 Correlation Heatmap
st.subheader("🔟 Correlation Heatmap")

numeric_df = df.select_dtypes(include=['int64','float64'])

fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(numeric_df.corr(), cmap="coolwarm")

st.pyplot(fig)

st.write("""
Insight:
Heatmap membantu melihat hubungan antar variabel numerik
yang dapat mempengaruhi pembatalan booking.
""")