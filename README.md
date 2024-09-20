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


The record() method, when used inside a with block, always moves ahead in the file stream. This means that if you record once for four seconds and then record again for four seconds, the second time returns the four seconds of audio after the first four seconds.


```python
# Process the audio file
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        # Record the first 4 seconds
        audio1 = r.record(source, duration=4)
        # Record the next 4 seconds
        audio2 = r.record(source, duration=4)

    # Transcribe the audio segments
    result1 = r.recognize_google(audio1)
    result2 = r.recognize_google(audio2)


In addition to specifying a recording duration, the record() method can be given a specific starting point using the offset keyword argument. This value represents the number of seconds from the beginning of the file to ignore before starting to record.

To capture only the second phrase in the file, you could start with an offset of four seconds and record for, say, three seconds.

```python
with sr.AudioFile(file_path) as source:
        audio = r.record(source, offset=4, duration=3)

r.recognize_google(audio)
