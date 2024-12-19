import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
from datetime import datetime

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("There seems to be an issue with the speech recognition service.")
        return None

def process_command(command):
    if 'wikipedia' in command:
        topic = command.replace("wikipedia", "").strip()
        summary = wikipedia.summary(topic, sentences=2)
        speak(f"According to Wikipedia, {summary}")
    elif 'play' in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    else:
        speak("Sorry, I didn't understand that command.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            if 'exit' in command or 'quit' in command:
                speak("Goodbye!")
                break
            process_command(command)