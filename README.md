# Speech Recognition and Audio Transcription 

- The project uses SpeechRecognition library in Python to implement speech recognition functionality . 
- I explain to install and use the SpeechRecognition package, and how to work with audio files and microphones for capturing speech data. 
- Using Streamlit and the SpeechRecognition library users can upload audio files in WAV or MP3 format, and the local web app will transcribe the audio content using Google's speech recognition API. 
- The transcribed text can be easily downloaded as a text file.

## Setup


1. Clone the Repository:    git clone https://github.com/bahramkhanlarov/Speech_recognition.git
2. Navigate to the Project Directory: cd Speech_recognition
3. Install Required Packages: pip install -r requirements.txt
4. Run the Streamlit App:  streamlit run sr.py
5. Upload Audio Files:
Use the web interface to upload audio files in WAV or MP3 format.
6. Download Transcription:
After transcription, you can download the transcribed text as a .txt file.

## Capturing Segments With offset and duration
What if you only want to capture a portion of the speech in a file? The record() method accepts a duration keyword argument that stops the recording after a specified number of seconds.

For example, the following captures any speech in the first 20 seconds of the file:

```python
r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source,duration=20)  # This captures 20 seconds of audio data

    result = r.recognize_google(audio)
