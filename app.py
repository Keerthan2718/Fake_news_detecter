import streamlit as st
from google import genai
import datetime
from google import genai
from google.genai import types

# 1. Setup with Stable API Version
# This 'http_options' fix is what stops the 404 Error!
try:
    # Pull the key safely from Streamlit secrets
    api_key = st.secrets["GEMINI_API_KEY"]

    client = genai.Client(
        api_key=api_key, 
        http_options={'api_version': 'v1beta'}
    )
    active_model = 'gemini-2.5-flash'
except Exception:
    # Fallback using the same secret key
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    active_model = 'gemini-1.5-flash-preview'

st.title("🛡️ AI Fact-Checker")

user_input = st.text_area("Paste News Here:")

if st.button("Fact Check"):
    with st.spinner("Searching the web for facts..."):
        today = datetime.date.today().strftime("%B %d, %Y")
    
    # 1. Define the Grounding Tool
    # This is the "magic" that stops hallucinations for current events
    google_search_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    try:
        response = client.models.generate_content(
            model=active_model,
            contents=f"Today is {today}. Fact-check this news accurately: {user_input}",
            config=types.GenerateContentConfig(
                tools=[google_search_tool] # 2. Pass the tool here
            )
        )
        st.markdown(response.text)
        
        # Optional: Show the sources Gemini found
        if response.candidates[0].grounding_metadata.search_entry_point:
            st.info("Sources verified via Google Search")
            
    except Exception as e:
        st.error(f"Error: {e}")
