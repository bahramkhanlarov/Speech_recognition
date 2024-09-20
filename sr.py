import streamlit as st
import speech_recognition as sr
import os

# Create a Streamlit app
st.title("Audio Transcription App")

# File uploader
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process the audio file
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source,duration=20)  # This captures the audio data

    result = r.recognize_google(audio)
    st.write("Transcription:")
    st.write(result)

    # Save the result to a text file
    with open('transcription.txt', 'w') as f:
        f.write(result)

    # Provide a download link for the transcription
    st.download_button("Download Transcription", data='transcription.txt', file_name='transcription.txt')
