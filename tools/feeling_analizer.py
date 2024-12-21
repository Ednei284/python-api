from textblob import TextBlob
import time            
from googletrans import Translator
from flask import  jsonify

def analize(texto):
    blob = TextBlob(texto)
    sentimento = blob.sentiment
    if sentimento.polarity < 0.0:
        return 'negativo'  
    if sentimento.polarity > 0.0:          
        return 'positivo'
    if sentimento.polarity == 0.0:
        return 'neutro'
    
def pt_to_english(text):
    translator = Translator()
    translated = translator.translate(text, src='pt', dest='en')
    return translated

def speech_text(text):
    convert_to_english =  pt_to_english(text)
    convert_to_english = str(convert_to_english)
    feeling = analize(convert_to_english)
    return jsonify({"recognized_text": text,'feeling':feeling}), 200
