import pyttsx3

def TextSpeech (text = ''):
    text_speech = pyttsx3.init()
    voice = text_speech.getProperty('voices')
    text_speech.setProperty('voice', voice[1].id)
    text_speech.say(text) 
    text_speech.runAndWait()