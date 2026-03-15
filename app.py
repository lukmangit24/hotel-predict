import streamlit as st

st.set_page_config(
    page_title="Hotel Booking Cancellation Prediction",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 Hotel Booking Cancellation Prediction")

st.markdown("---")

st.header("📊 Latar Belakang")

st.write("""
Industri perhotelan sering menghadapi masalah **pembatalan reservasi** yang cukup tinggi.
Pembatalan ini dapat menyebabkan kehilangan potensi pendapatan dan menyulitkan hotel
dalam mengelola ketersediaan kamar.
""")

st.markdown("---")

st.header("🚨 Masalah Utama")

st.write("""
Masalah utama yang ingin diselesaikan dalam proyek ini adalah
**memprediksi kemungkinan pembatalan reservasi hotel berdasarkan karakteristik pemesanan.**

Pembatalan menyebabkan **kehilangan potensi pendapatan bagi hotel**.
""")

st.markdown("---")

st.header("🎯 Objective")

st.write("""
Hasil prediksi ini dapat membantu hotel dalam:

- Mengurangi potensi kerugian akibat pembatalan reservasi
- Mengoptimalkan strategi overbooking
- Menyesuaikan kebijakan deposit
- Mengembangkan strategi pemasaran yang lebih tepat sasaran
""")

st.markdown("---")

st.header("🤖 Model yang Digunakan")

st.write("""
Model Machine Learning yang digunakan adalah **Random Forest Classifier**.

Model ini dipilih karena:
- mampu menangani data kompleks
- robust terhadap overfitting
- memiliki performa yang baik pada dataset tabular
""")

st.success("Gunakan menu di sidebar untuk membuka halaman lainnya.")