# 🛡️ AI Fact Checker

An AI-powered fact-checking web application built with **Streamlit** and **Google Gemini AI**. This application verifies news and claims by leveraging **Google Search grounding**, allowing Gemini to search the web before generating a response.

## 🚀 Features

- 🔍 Fact-check any news article or claim
- 🌐 Uses Google Search for real-time verification
- 🤖 Powered by Google Gemini 2.5 Flash
- ⚡ Fast and responsive Streamlit interface
- 🔒 Secure API key management using Streamlit Secrets
- 📱 Simple and user-friendly design

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API (`google-genai`)
- Google Search Grounding

## 📂 Project Structure

```
AI-Fact-Checker/
│
├── app.py
├── requirements.txt
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Keerthan2718/Fake_news_detecter.git
cd Fake_news_detecter
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Streamlit secrets

Create the following file:

```
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

## 📸 Demo

Paste any news article or claim into the text area, and the application will:

- Search the web using Google Search
- Analyze the claim with Gemini AI
- Return a fact-check result with supporting information

- https://fake-news-detecterr.streamlit.app/

## 🔐 Environment Variables

The application requires one secret:

| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Your Google Gemini API Key |

## 📌 Future Improvements

- Upload PDF and image news articles
- Display confidence score
- Highlight verified sources
- Show fact-check history
- Multi-language support
- Export reports as PDF

