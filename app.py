from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)

# paste your key inside quotes
import os
API_KEY = os.environ.get("OPENAI_API_KEY")
@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message")

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are StudyBuddy AI. Only answer study-related questions like programming, computer science, mathematics, science, engineering, exams, theory, or concepts. If the question is not related to studies, politely refuse."
            },
                

            {
                "role": "user",
                "content": message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    reply = result["choices"][0]["message"]["content"]

    return jsonify({"reply": reply})

app.run(port=5000)
