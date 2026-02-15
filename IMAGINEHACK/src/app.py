# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 19:09:30 2025

@author: rajia
"""

import streamlit as st
import joblib
import os

# --- Load model and vectorizer ---
MODEL_PATH = "model_fake_news.pkl"
VECTORIZER_PATH = "vectorizer_fake_news.pkl"

# Check file existence
if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    st.error("Model or vectorizer file not found. Please train the model and ensure the .pkl files are in the same directory.")
    st.stop()

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# --- Streamlit UI ---
st.set_page_config(page_title="Malaysia Fake News Detector", page_icon="📰")
st.title("IS IT REAL OF FAKE NEWS??")
st.write("Check the **credibility** of Malaysian news by entering a headline or short article below.")

# --- Input text box ---
news_text = st.text_area("Enter News Text or Headline:", height=200, placeholder="E.g. Malaysia to switch to right-hand driving in 2026")

# --- Predict ---
if st.button("Check"):
    if news_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_vector = vectorizer.transform([news_text])
        prediction = model.predict(input_vector)[0]
        probas = model.decision_function(input_vector)

        if prediction == "FAKE":
            st.error("❌ The news is predicted to be **FAKE**.")
        elif prediction == "REAL":
            st.success("✅ The news is predicted to be **REAL**.")
        else:
            print("Uncertain!")
        
# --- Footer ---
st.markdown("---")
st.caption("Built using a machine learning model trained on Malaysian real and fake news.")
