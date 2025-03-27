# AI-Powered Recipe Generator

## 🍽️ Overview
The **AI-Powered Recipe Generator** is a web application that generates unique recipes based on user-provided ingredients using AI. It also provides text-to-speech conversion, allowing users to listen to and download their generated recipes.

## 🎯 Features
- **AI-Generated Recipes** – Creates unique recipes based on input ingredients using Groq API.
   **Text-to-Speech (TTS)** – Converts text-based recipes into an MP3 audio file.
   **Audio Playback & Download** – Users can listen to or download their recipe audio.
   **Dynamic Background Support** – Loads a background image if available.
   **User-Friendly UI** – Developed using Streamlit for a seamless experience.
   **API Integration** – Uses **Groq API** for AI-powered recipe generation.
   **Error Handling** – Ensures smooth functioning with proper error handling.

## 🛠️ Tech Stack
- **Frontend & UI:** Streamlit
- **AI Integration:** Groq API
- **Text-to-Speech:** Google Text-to-Speech (gTTS)
- **Audio Handling:** Python's `tempfile` and `base64` encoding

## 🔗 Workflow
1 **User Inputs Ingredients** – Enter a list of ingredients.
2 **AI Generates Recipe** – The Groq API processes the input and returns a unique recipe.
3 **Recipe Displayed** – The AI-generated recipe is shown on the screen.
4 **Text-to-Speech Conversion** – Users can click to convert the recipe into speech.
5 **Audio Playback & Download** – Users can listen to or download the MP3 file.

## 🚀 How to Run the Project
###  Install Dependencies
```sh
pip install streamlit requests gtts
```

###  Run the Application
```sh
streamlit run app.py
```

## 📝 Usage
1 Open the application.
2 Enter ingredients in the text box.
3 Click **"Generate Recipe"** to get a unique AI-generated recipe.
4 Click **"🔊 Play Recipe Audio"** to listen to it.
5 Click **"🔉 Download Recipe Audio"** to save the MP3 file.

## 🔑 API Key Setup
Replace the API key in `app.py` with your valid **Groq API Key**:
```python
API_KEY = "your_groq_api_key_here"


📂 AI_Recipe_Generator/
│── 📂 static/                  # Static assets (CSS, images, etc.)
│   │── background.jpg          # Optional background image
│   │── styles.css              # Custom CSS styles
│
│── 📂 assets/                  # Store additional resources (if needed)
│   │── 📂 audio/                   # Temporary storage for generated audio files
│   │── temp_audio.mp3          # (Dynamically generated)
│
│── 📂env/
│
│── 📂 Template/                   
│   │── index.hrml                  # frotend 
│
│── 📜 app.py                   # Main Streamlit app
│── 📜 requirements.txt         # Dependencies (gtts, requests, streamlit, etc.)
│── 📜 .gitignore               # Ignore unnecessary files (e.g., `audio/*.mp3`)
│── 📜 config.py                # API keys & configuration settings

```

## 📌 Notes
- If the background image is missing, the app will continue without it.
- If an API key is invalid or missing, an error message will be displayed.
- The app will display **"Good Luck!"** after fetching the recipe.

## 📢 Credits
Built with ❤️ using **Streamlit, Groq API, and gTTS**.

