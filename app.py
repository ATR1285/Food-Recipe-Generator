import streamlit as st
import os
import requests
from gtts import gTTS
import tempfile
import base64

# ✅ Set Page Config
st.set_page_config(page_title="AI Recipe Generator", page_icon="🍽️", layout="wide")

# ✅ Function to Set Background Image (only if available)
def set_background(image_path):
    if os.path.exists(image_path):  # ✅ Check if image exists before applying
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

# ✅ Apply Background Image (only if the file exists)
bg_image_path = "static/background.jpg"
set_background(bg_image_path)

# ✅ Load External CSS (only if available)
def load_css():
    css_path = "static/styles.css"
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ✅ Sidebar Toggle Logic
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = False  # Initially hidden

# Show button only when sidebar is closed
if not st.session_state.sidebar_open:
    if st.button("⚙️ Show Sidebar"):
        st.session_state.sidebar_open = True
        st.rerun()  # ✅ Reload UI to apply sidebar immediately

# Sidebar Content (Appears only when toggled)
if st.session_state.sidebar_open:
    with st.sidebar:
        st.markdown("📌 **Instructions:**")
        st.write("1. Enter ingredients.")
        st.write("2. Click **Generate Recipe**.")
        st.write("3. Play or Download the recipe audio.")

# ✅ Main UI
st.markdown('<h1 class="title-text">🍽️ AI-Powered Recipe Generator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Enter ingredients to generate a unique recipe using AI.</p>', unsafe_allow_html=True)

# ✅ User Input for Ingredients
ingredients = st.text_area("Enter ingredients:", "chicken, garlic, onion")

if "recipe" not in st.session_state:
    st.session_state.recipe = ""
if "fetching" not in st.session_state:
    st.session_state.fetching = False  # ✅ Track fetching status

# 🔥 **Hardcoded API Key (Replace with a valid one)**
API_KEY = "API HERE "  # ✅ Keep this format

# ✅ Generate Recipe Button
if st.button("Generate Recipe", key="generate_recipe", help="Click to generate a unique recipe"):
    if API_KEY:
        st.session_state.fetching = True  # ✅ Set fetching state
        st.rerun()

# ✅ Fetch API & Update Recipe (if fetching is True)
if st.session_state.fetching:
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",  # ✅ Uses correct API key format
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": f"Create a recipe with these ingredients: {ingredients}"}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        recipe = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No recipe found.")
        st.session_state.recipe = recipe + "\n\n**🍀 Good Luck!**"  # ✅ Append "Good Luck!" at the end

    except requests.exceptions.RequestException as e:
        st.session_state.recipe = f"❌ API Request Failed: {e}"

    st.session_state.fetching = False  # ✅ Hide fetching status after request
    st.rerun()

# ✅ Display Recipe Only After Fetching is Done
if st.session_state.recipe:
    st.subheader("🍳 Your AI-Generated Recipe:")
    st.write(st.session_state.recipe)

# ✅ Play & Download Recipe Audio
if st.session_state.recipe:
    col1, col2 = st.columns(2)

    # ✅ Define audio file path globally
    audio_file_path = tempfile.mktemp(suffix=".mp3")

    with col1:
        if st.button("🔊 Play Recipe Audio", key="play_audio"):
            tts = gTTS(st.session_state.recipe, lang="en")
            tts.save(audio_file_path)  # Save the audio file
            st.audio(audio_file_path, format="audio/mp3")  # Play the audio

    with col2:
        # ✅ Ensure the file exists before downloading
        if os.path.exists(audio_file_path):
            with open(audio_file_path, "rb") as file:
                st.download_button("🔉 Download Recipe Audio", file, file_name="recipe.mp3", mime="audio/mp3")

# ✅ Footer
st.markdown("---")
st.write("📢 **Built with ❤️ using Streamlit**")
