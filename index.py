import os
from flask import Flask, request,send_file, jsonify
from tools.text_to_speech import text_speech,speech_text
UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.json
    audio = text_speech(data['text'])
    return audio

@app.route('/get-audio') 
def get_audio(): 
    file_path = f'{UPLOAD_FOLDER}/audio.mp3' 
    return send_file(file_path, mimetype='audio/mpeg')

@app.route('/generate-text',methods=['POST']) 
def generate(): 
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file part"}), 400
    file = request.files['audio']
    print(file)
    if file.filename == '':
        return jsonify({"error": "Not File Found."}), 400
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        text = speech_text(file_path)
        os.remove(f"{UPLOAD_FOLDER}/{file.filename}.wav")
        return text

if __name__ == "__main__":
    app.run(debug=True)
