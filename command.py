from texttospeach import speak
import wikipedia # type: ignore
import pywhatkit # type: ignore
from datetime import datetime

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

# Example usage
command = "play Imagine Dragons"
process_command(command)