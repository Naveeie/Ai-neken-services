from .text_speech import TextSpeech
from routes.response import success, error

def TextToSpeech (body):
    try:
        TextSpeech(body['text'])
        return success('', 'Speech Successfully')
    except NameError:
        print(NameError)
        return error(NameError)
         
       