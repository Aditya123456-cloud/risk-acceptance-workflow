import os
import time
import logging
import requests

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

API_KEY = os.getenv("GROQ_API_KEY")


class GroqClient:

    def __init__(self):
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def call(self, prompt: str):

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2
        }

        for attempt in range(3):
            try:
                response = requests.post(
                    self.url,
                    json=payload,
                    headers=headers,
                    timeout=10
                )

                response.raise_for_status()

                json_response = response.json()

                return json_response["choices"][0]["message"]["content"]

            except Exception as error:
                logging.error(
                    f"Groq API failure | attempt={attempt + 1} | error={error}"
                )

                time.sleep(2 ** attempt)

        return "AI Service Unavailable"