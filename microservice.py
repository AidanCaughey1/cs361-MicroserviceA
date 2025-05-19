from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ Microservice is running! Use POST /verify to send a media link."

@app.route("/verify", methods=["POST"])
def verify_link():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"valid": False, "error": "No URL provided", "error_code": 400}), 400

    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            return jsonify({
                "valid": True,
                "file_name": url.split("/")[-1],
                "content_type": response.headers.get("Content-Type"),
                "file_size": response.headers.get("Content-Length")
            })
        else:
            return jsonify({
                "valid": False,
                "error": f"Received status code {response.status_code}",
                "error_code": response.status_code
            }), response.status_code
    except Exception as e:
        return jsonify({
            "valid": False,
            "error": str(e),
            "error_code": 500
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
