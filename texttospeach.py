import pyttsx3 # type: ignore

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
speak("Hello! I am your assistant.")