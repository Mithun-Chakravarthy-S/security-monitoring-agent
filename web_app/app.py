from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    log = request.json.get("log")

    # This simulates using YOUR API key securely
    api_key = os.getenv("THREAT_API_KEY")


    if not api_key:
        return jsonify({"error": "API key not set"}), 500

    result = {
        "input_log": log,
        "analysis": "Suspicious activity detected",
        "severity": "High"
    }

    return jsonify(result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

