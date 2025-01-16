from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    convert_text = data['text'].upper()
    return jsonify({'converted_text': convert_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)