from flask import Flask, render_template, jsonify, send_from_directory
import json
import os

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph.json')
def graph():
    # Load the generated graph.json
    if os.path.exists('graph.json'):
        with open('graph.json', 'r') as f:
            return jsonify(json.load(f))
    return jsonify({'nodes': [], 'edges': []})

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)