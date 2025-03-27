from gtts import gTTS

# Text to convert into speech
text = "Welcome to our AI-powered recipe generator. Enjoy your cooking!"

# Convert text to speech
tts = gTTS(text=text, lang="en")

# Save the audio file
tts.save("output.mp3")

print("✅ Audio file 'output.mp3' generated successfully!")
