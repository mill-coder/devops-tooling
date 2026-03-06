import json
import os

import requests
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder="static")

with open("tools.json") as f:
    TOOLS = json.load(f)

TOOL_IDS = {t["id"] for t in TOOLS}


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/tools.json")
def tools_manifest():
    return send_from_directory(".", "tools.json")


@app.route("/tools/<name>")
def serve_tool(name):
    if name not in TOOL_IDS:
        return jsonify({"error": "Tool not found"}), 404
    return send_from_directory("tools", f"{name}.html")


ALLOWED_TOOL_DATA = {"ecs-fields", "ecs-custom-fields"}


@app.route("/tools/<name>.json")
def serve_tool_data(name):
    if name not in ALLOWED_TOOL_DATA:
        return jsonify({"error": "Not found"}), 404
    return send_from_directory("tools", f"{name}.json")


@app.route("/proxy", methods=["POST"])
def proxy():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing url"}), 400

    method = data.get("method", "GET").upper()
    headers = data.get("headers", {})
    body = data.get("body")

    try:
        resp = requests.request(
            method=method,
            url=data["url"],
            headers=headers,
            data=body,
            timeout=30,
        )
        return jsonify({
            "status": resp.status_code,
            "headers": dict(resp.headers),
            "body": resp.text,
        })
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 502


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(debug=debug, host="0.0.0.0", port=5000)
