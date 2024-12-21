import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment 
from pydub.playback import play
from flask import  jsonify
import os 
import random
# Função para converter voz em texto

# Função para converter texto em voz
def text_speech(texto):
    try:
        file_path = os.path.join(os.path.dirname(__file__), f'{random.randint(1, 100)}audio.mp3')
        tts = gTTS(texto, lang="pt")
        tts.save(file_path)
    except:
        response = { "error": "Not Found"} 
        return jsonify(response), 404

def play_sound(file_path):
    song = AudioSegment.from_mp3(file_path) 
    return play(song)

def speech_text(file_path):
    r = sr.Recognizer()
    audio = AudioSegment.from_mp3(file_path) 
    audio.export("uploads/audio.wav", format="wav")
    with sr.AudioFile("uploads/audio.wav") as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio, language="pt-BR")
            return jsonify({"transcription": text}), 200
        except sr.UnknownValueError:
            return jsonify({"error": "Desculpe, não consegui entender o que você disse."}), 400
        except sr.RequestError as e:
            return jsonify({"error": f"Não foi possível solicitar os resultados: {e}"}), 500
    