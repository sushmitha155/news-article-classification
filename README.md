
# 📰 News Article Classification (Fake or Real)

This project uses machine learning and natural language processing (NLP) to classify news articles as **Fake** or **Real**. It was developed as part of the Elevate Labs internship and demonstrates the use of text vectorization, model training, and Streamlit deployment.

---

## 📌 Features

- 🔍 Classifies news articles using a trained ML model
- 🧠 TF-IDF + Passive Aggressive Classifier
- ✅ Achieved 99.45% accuracy on the test set
- 🌐 Includes a Streamlit app for real-time prediction

---

## 📁 Project Structure

```
News_Article_Classification/
├── dataset/
│   ├── Fake.csv
│   └── True.csv
├── models/
│   ├── fake_news_model.pkl
│   └── vectorizer.pkl
├── news_classifier.ipynb
├── streamlit_app.py
└── Final_Report.pdf
```

---

## 📦 Tech Stack

- **Language**: Python 3.x
- **Libraries**: Pandas, Sklearn, Joblib, Streamlit
- **Model**: PassiveAggressiveClassifier
- **Interface**: Streamlit Web App

---

## 🚀 How to Run

1. Clone the repo:
   ```
   git clone https://github.com/yourusername/news-article-classification.git
   cd news-article-classification
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

---

## 📊 Example Output

> Input: News article about Chandrayaan-3  
> Output: ✅ This looks like Real News

---

## 📄 Report

A complete 2-page report summarizing the project is included as `Final_Report.pdf`.

---

## ✨ Future Enhancements

- Add advanced NLP models (e.g., BERT)
- Train on a more diverse dataset
- Deploy publicly via Streamlit Cloud

---

## 👩‍💻 Author

- **Sushmitha Gundeboina** | AIML | MRECW | 2025 Batch
