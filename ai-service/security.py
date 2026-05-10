import re

from flask import request, jsonify


def sanitize_input(text: str):

    if not text:
        return None

    cleaned_text = re.sub(r"<.*?>", "", text)

    blocked_patterns = [
        "ignore previous instructions",
        "drop table",
        "delete from",
        "--",
        ";",
        "system prompt"
    ]

    lowered = cleaned_text.lower()

    for pattern in blocked_patterns:
        if pattern in lowered:
            return None

    return cleaned_text.strip()


def validate_request():

    data = request.get_json()

    if not data:
        return None, (
            jsonify({"error": "Request body missing"}),
            400
        )

    if "input" not in data:
        return None, (
            jsonify({"error": "input field missing"}),
            400
        )

    cleaned = sanitize_input(data["input"])

    if not cleaned:
        return None, (
            jsonify({"error": "Invalid or unsafe input"}),
            400
        )

    return cleaned, None