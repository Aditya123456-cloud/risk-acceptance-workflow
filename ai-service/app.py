from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from groq_client import GroqClient
from security import validate_request
from prompts import (
    classify_prompt,
    summarize_prompt,
    recommend_prompt
)

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

groq_client = GroqClient()


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "service": "Risk Acceptance Workflow AI Service"
    })


@app.route("/classify", methods=["POST"])
def classify():
    text, error = validate_request()

    if error:
        return error

    prompt = classify_prompt(text)
    result = groq_client.call(prompt)

    return jsonify({
        "endpoint": "classify",
        "input": text,
        "result": result
    })


@app.route("/summarize", methods=["POST"])
def summarize():
    text, error = validate_request()

    if error:
        return error

    prompt = summarize_prompt(text)
    result = groq_client.call(prompt)

    return jsonify({
        "endpoint": "summarize",
        "input": text,
        "result": result
    })


@app.route("/recommend", methods=["POST"])
def recommend():
    text, error = validate_request()

    if error:
        return error

    prompt = recommend_prompt(text)
    result = groq_client.call(prompt)

    return jsonify({
        "endpoint": "recommend",
        "input": text,
        "result": result
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )