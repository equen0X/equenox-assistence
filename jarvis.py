import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import pywhatkit # type: ignore
import wikipedia # type: ignore
import datetime
import openai # type: ignore

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice; use [0] for male
engine.setProperty('rate', 150)  # Adjust speaking rate

def talk(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and recognize it."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            talk("Sorry, I did not understand that.")
            return ""
        except sr.RequestError as e:
            talk("There seems to be an issue with the recognition service.")
            return ""

def handle_command(command):
    """Process the user's command and respond accordingly."""
    if "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"The current time is {time}.")
    elif "search for" in command or "who is" in command:
        query = command.replace("search for", "").replace("who is", "").strip()
        info = wikipedia.summary(query, sentences=2)
        talk(f"Here is what I found: {info}")
    elif "what is" in command:
        query = command.replace("what is", "").strip()
        info = wikipedia.summary(query, sentences=2)
        talk(f"Here's what I found: {info}")
    elif "stop" in command:
        talk("Goodbye!")
        return False
    else:
        talk("I can try to answer that using OpenAI.")
        response = ask_openai(command)
        talk(response)
    return True

def ask_openai(prompt):
    """Get a response from OpenAI GPT."""
    openai.api_key = "your_openai_api_key"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Sorry, I couldn't fetch an answer from OpenAI."

def run_jarvis():
    """Main loop to run the assistant."""
    talk("Hello! I am equenox. How can I help you?")
    running = True
    while running:
        command = listen()
        if command:
            running = handle_command(command)

if __name__ == "__main__":
    run_jarvis()