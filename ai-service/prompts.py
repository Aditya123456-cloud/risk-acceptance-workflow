def classify_prompt(text):
    return f"""
Classify this risk as HIGH, MEDIUM, or LOW.

Risk:
{text}
"""


def summarize_prompt(text):
    return f"""
Summarize this risk.

Risk:
{text}
"""


def recommend_prompt(text):
    return f"""
Suggest mitigation steps for this risk.

Risk:
{text}
"""