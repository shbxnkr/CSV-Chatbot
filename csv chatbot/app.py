from flask import Flask, request, jsonify
from chatbot import load_agent, ask_question
import os

app = Flask(__name__)
agent = None

@app.route('/load_csv', methods=['POST'])
def load_csv():
    global agent
    data = request.get_json()

    # Ensure we received data
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    csv_path = data.get('csv_path')

    # Validate the CSV path
    if not csv_path:
        return jsonify({'error': 'No CSV path provided'}), 400
    if not os.path.exists(csv_path):
        return jsonify({'error': 'CSV file does not exist at provided path'}), 400

    try:
        agent = load_agent(csv_path)
        return jsonify({'message': 'CSV loaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/ask', methods=['POST'])
def ask():
    global agent

    if agent is None:
        return jsonify({'error': 'Agent not loaded. Please load a CSV first.'}), 400

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    question = data.get('question')
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    try:
        answer = ask_question(agent, question)
        return jsonify({'answer': answer}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
