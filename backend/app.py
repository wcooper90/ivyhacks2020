import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from textManipulation.summarization import summarize_text, summarize_speech_transcription, summarize_article_text
from UserInputs import UserInputs
from inputs.article_scraper import url_text_conversion
from inputs.scanned_input import image_text_conversion



app = Flask(__name__)
CORS(app)

@app.route('/get_text', methods=['POST'])
def get_text():
    text = request.get_json(force=True)
    output, _ = summarize_text(text, num_sentences=3)
    return jsonify(output=output)


@app.route('/get_article', methods=['POST'])
def get_article():
    url = request.get_json(force=True)
    text = url_text_conversion(url)
    output, _ = summarize_text(text, num_sentences=8)
    return jsonify(output=output)


@app.route('/get_scan', methods=['POST'])
def get_scan():
    file = request.files['body'] 
    text = image_text_conversion(scan)
    output, _ = summarize_text(text, num_sentences=8)
    return jsonify(output=output)


@app.route('/time')
def get_time():
    print('hello')
    return {'time': time.time()}
