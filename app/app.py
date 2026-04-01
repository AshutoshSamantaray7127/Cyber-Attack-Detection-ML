import streamlit as st
import joblib
import os

st.title("🔐 Cyber Attack Detection System")

# Load model
model_path = os.path.join("models", "best_model.pkl")
model = joblib.load(model_path)

st.write("Enter all 41 feature values:")

# Create input fields for 41 features
features = []

for i in range(41):
    val = st.number_input(f"Feature {i+1}", value=0.0)
    features.append(val)

# Prediction
if st.button("Predict"):
    prediction = model.predict([features])

    if prediction[0] == 1:
        st.error("⚠️ Attack Detected!")
    else:
        st.success("✅ Normal Traffic")
