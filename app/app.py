import streamlit as st
import joblib

st.title("🔐 Cyber Attack Detection System")

# Load model
model = joblib.load("models/best_model.pkl")

st.write("Enter network details:")

# Inputs
duration = st.number_input("Duration")
src_bytes = st.number_input("Source Bytes")
dst_bytes = st.number_input("Destination Bytes")

if st.button("Predict"):
    # 41 features total
    features = [duration, src_bytes, dst_bytes] + [0]*38

    prediction = model.predict([features])

    if prediction[0] == 1:
        st.error("⚠️ Attack Detected!")
    else:
        st.success("✅ Normal Traffic")