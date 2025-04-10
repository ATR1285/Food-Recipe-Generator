import streamlit as st
import requests
from gtts import gTTS
import tempfile
import os
import base64

# ----------------------- PAGE CONFIG -----------------------
st.set_page_config(page_title="AI Recipe Generator", page_icon="🍽️", layout="wide")

# ----------------------- BACKGROUND -----------------------
def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        bg_style = f"""
        <style>
        .stApp {{
            background: url("data:image/png;base64,{encoded_string}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """
        st.markdown(bg_style, unsafe_allow_html=True)

set_background("static/background.jpg")

# ----------------------- CSS LOADER -----------------------
def load_css():
    css_path = "static/styles.css"
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ----------------------- SESSION STATE -----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# ----------------------- SIGN-IN PAGE -----------------------
if not st.session_state.logged_in:
    st.markdown("## 🔐 Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Simple check (replace with real validation if needed)
        if username and password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Please enter both username and password.")

# ----------------------- MAIN APP -----------------------
if st.session_state.logged_in:

    st.markdown(f'<h1 class="title-text">🍽️ Welcome {st.session_state.username}! AI Recipe Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Enter ingredients to generate a recipe using LLaMA 3 AI</p>', unsafe_allow_html=True)

    # Sidebar Toggle
    if "sidebar_open" not in st.session_state:
        st.session_state.sidebar_open = False

    if not st.session_state.sidebar_open:
        if st.button("⚙️ Show Sidebar"):
            st.session_state.sidebar_open = True
            st.rerun()

    if st.session_state.sidebar_open:
        with st.sidebar:
            st.markdown("📌 **Instructions:**")
            st.write("1. Enter ingredients.")
            st.write("2. Click Generate Recipe.")
            st.write("3. Listen or download audio.")

    # Ingredient input
    ingredients = st.text_area("Enter ingredients:", "chicken, garlic, onion")

    if "recipe" not in st.session_state:
        st.session_state.recipe = ""
    if "fetching" not in st.session_state:
        st.session_state.fetching = False

    # 🟠 Replace this with your actual API Key
    API_KEY = "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"

    if st.button("🍳 Generate Recipe"):
        if API_KEY and ingredients.strip():
            st.session_state.fetching = True
            st.rerun()

    # 🔥 API Request with Groq
    if st.session_state.fetching:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama3-70b-8192",
            "messages": [{"role": "user", "content": f"Create a recipe with these ingredients: {ingredients}"}],
            "temperature": 0.7
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            recipe = response.json()["choices"][0]["message"]["content"]
            st.session_state.recipe = recipe + "\n\n🍀 **Good Luck!**"
        except Exception as e:
            st.session_state.recipe = f"❌ API Error: {e}"

        st.session_state.fetching = False
        st.rerun()

    # Show Recipe
    if st.session_state.recipe:
        st.subheader("🍳 Your AI-Generated Recipe:")
        st.write(st.session_state.recipe)

        # Audio Buttons
        col1, col2 = st.columns(2)
        audio_file_path = tempfile.mktemp(suffix=".mp3")

        with col1:
            if st.button("🔊 Play Recipe Audio"):
                tts = gTTS(st.session_state.recipe, lang="en")
                tts.save(audio_file_path)
                st.audio(audio_file_path, format="audio/mp3")

        with col2:
            if os.path.exists(audio_file_path):
                with open(audio_file_path, "rb") as file:
                    st.download_button("🎧 Download Recipe Audio", file, file_name="recipe.mp3", mime="audio/mp3")

    # Footer
    st.markdown("---")
    st.write("📢 **Built with ❤️ using Streamlit**")
