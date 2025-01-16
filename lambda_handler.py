from flask import Flask, request, jsonify
from mangum import Mangum

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in request body"}),
        400
    
    converted_text = data['text'].upper()
    return jsonify({"converted_text": converted_text})

handler = Mangum(app)