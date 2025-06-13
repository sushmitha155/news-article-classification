import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('models/fake_news_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# App UI
st.set_page_config(page_title="Fake News Classifier", layout="centered")
st.title("📰 News Article Classifier (Fake or Real)")
st.markdown("Enter a news article below and the model will predict whether it's **Fake** or **Real**.")

# Text input
news_input = st.text_area("📝 Paste the news article text here:", height=250)

# Predict button
if st.button("🔍 Classify"):
    if news_input.strip() == "":
        st.warning("Please enter some news text to classify.")
    else:
        input_vec = vectorizer.transform([news_input])
        prediction = model.predict(input_vec)[0]

        if prediction == 1:
            st.success("✅ This looks like **Real News**.")
        else:
            st.error("🚨 This looks like **Fake News**.")
