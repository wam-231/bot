import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration (easy to change)
API_KEY = os.getenv("API_KEY", "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")
API_URL = os.getenv("API_URL", "https://openrouter.ai/api/v1/chat/completions")
MODEL = os.getenv("MODEL", "nvidia/nemotron-3-super-120b-a12b:free")
CREATOR_NAME = os.getenv("CREATOR_NAME", "wangchuk")

# Set up page configuration
st.set_page_config(page_title=f"Chatbot by {CREATOR_NAME}", page_icon="🤖", layout="centered")

# CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body {
        font-family: 'Outfit', sans-serif;
    }
    
    .title-container {
        text-align: center;
        padding: 1.5rem 0;
        background: linear-gradient(135deg, #ff007f 0%, #7928ca 50%, #00dfd8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .subtitle-container {
        text-align: center;
        color: #888888;
        font-size: 1.1rem;
        margin-top: -1.5rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(f'<div class="title-container">🤖 Chatbot by {CREATOR_NAME}</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-container">Powered by OpenRouter</div>', unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
message = st.chat_input("Ask AI:")

if message == "who made you":
    with st.chat_message("user"):
        st.markdown(message)
    with st.chat_message("assistant"):
        st.markdown(f"I am made by {CREATOR_NAME}")
    st.session_state.messages.append({"role": "user
