# app.py
from flask import Flask, render_template, jsonify, request
import threading
import ids

app = Flask(__name__)

@app.route('/')
def index():
    with open('alerts.log', 'r') as f:
        logs = f.readlines()
    return render_template('index.html', logs=logs)

@app.route('/stats')
def stats():
    # Assuming 'traffic_stats' is a dictionary in ids.py storing the stats
    return jsonify(ids.traffic_stats)

@app.route('/control', methods=['POST'])
def control():
    # Placeholder to handle settings updates
    data = request.json
    # You might adjust settings like thresholds or enabled rules here
    # Example: ids.update_settings(data['new_settings'])
    return jsonify({"status": "Settings updated successfully"})

def start_ids():
    ids.start_sniffing('en0')  # Adjust the interface based on the actual environment

if __name__ == '__main__':
    t = threading.Thread(target=start_ids)
    t.start()
    app.run(debug=True, port=5001)  # Make sure to use an available port
