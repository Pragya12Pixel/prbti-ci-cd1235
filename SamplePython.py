from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! CI/CD deployment is working pragyyyya successfully 🚀"

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "message": "Application is healthy"
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)