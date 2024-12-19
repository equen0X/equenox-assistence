import wolframalpha

wolfram_app_id = "YOUR_APP_ID"  # Get this from WolframAlpha Developer Portal
client = wolframalpha.Client(wolfram_app_id)

def ask_wolfram(query):
    res = client.query(query)
    try:
        answer = next(res.results).text
        speak(answer)
    except StopIteration:
        speak("Sorry, I couldn't find an answer.")