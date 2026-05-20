# pyrefly: ignore [missing-import]
import streamlit as st
import requests

# OpenRouter API Key
API_KEY = "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"

# API URL
url = "https://openrouter.ai/api/v1/chat/completions"

# Set up page configuration with a modern feel
st.set_page_config(page_title="This is made by wangchuk", page_icon="🤖", layout="centered")

# Inject premium custom CSS styling (gradient header, smooth animations, elegant fonts)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Glowing Title */
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
    
    /* Subtle subtitle */
    .subtitle-container {
        text-align: center;
        color: #888888;
        font-size: 1.1rem;
        margin-top: -1.5rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-container">🤖 This Chatbot made by wangchuks</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-container">Powered by OpenRouter</div>', unsafe_allow_html=True)

# Initialize chat history in Streamlit session state


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all messages from the chat history on every rerun
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input using modern chat input
message = st.chat_input("Ask AI:")

if message == "who made you":
    with st.chat_message("user"):
        st.markdown(message)
    with st.chat_message("assistant"):
        st.markdown("I am made by Wangchuk")
    st.session_state.messages.append({"role":"assistant","content":'I am made by Wangchuk'})
    st.session_state.messages.append({"role":"user","content":message})


elif message:
    # Display the user message immediately
    with st.chat_message("user"):
        st.markdown(message)
    
    # Save the user message to history
    st.session_state.messages.append({"role": "user", "content": message})
    
    # Setup headers and payload for OpenRouter
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # We include all message history to let the AI understand context
    data = {
        "model": "nvidia/nemotron-3-super-120b-a12b:free",
        "messages": [
            {"role": msg["role"], "content": msg["content"]} 
            for msg in st.session_state.messages
        ]
    }
    
    # Display a loader while the request is being sent
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Thinking..."):
            try:
                response = requests.post(url, headers=headers, json=data)
                
                if response.status_code == 200:
                    result = response.json()
                    ai_reply = result["choices"][0]["message"]["content"]
                    
                    # Render AI response
                    message_placeholder.markdown(ai_reply)
                    
                    # Save AI reply to history
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                else:
                    message_placeholder.error(f"Error {response.status_code}: Could not fetch response.")
                    st.error(response.text)
                    
            except Exception as e:
                message_placeholder.error(f"Request failed: {e}")
