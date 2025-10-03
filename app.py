# app.py — Chirag AI Demo
import streamlit as st

# Page config
st.set_page_config(page_title="Chirag AI", layout="centered")

# Welcome message
st.title("🤖 Chirag AI — हिंदी समाचार और सामान्य ज्ञान सहायक")
st.markdown("👋 नमस्ते, मैं **Chirag Sharma** हूँ — मैं आपकी क्या सेवा कर सकता हूँ?")

# User input
query = st.text_input("अपना प्रश्न यहाँ लिखें (हिंदी में भी लिख सकते हैं):")

# Response (Demo Only)
if st.button("उत्तर सुनें"):
    if query.strip() == "":
        st.warning("❗ कृपया कोई प्रश्न लिखें।")
    else:
        st.success(f"आपने पूछा: {query}")
        st.info("👉 यह एक demo जवाब है। असली न्यूज़, GK और Study features आगे जोड़े जाएंगे।")
