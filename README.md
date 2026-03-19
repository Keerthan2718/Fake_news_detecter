# Fake News Detection System 📰
A real-time web application that uses Artificial Intelligence to verify the authenticity of news articles and social media claims. Built with Streamlit for the frontend and powered by Google Gemini Pro for advanced natural language understanding.

# Overview
In an era of rapid information spread, distinguishing between fact and fiction is critical. This project leverages Large Language Models (LLMs) to analyze text patterns, source credibility, and logical consistency to provide a probability score of whether a piece of news is "Real" or "Fake."

# Tech Stack
<br>
Language:  Python
<br>
AI Model:  Google Gemini 2.5 and 1.5 Flash (via Gemini API)
<br>
Web Framework:  Streamlit
<br>
Library Imports:
<br>
 1.import streamlit as st
 <br>
 2.from google import genai
 <br>
 3.import datetime
 <br>
 4.from google.genai import types
 <br>

Google Search_tool = types.Tool(...):  It gives Gemini the ability to search the live internet to verify facts.
