# StudyBuddy AI

StudyBuddy AI is an LLM-powered academic chatbot designed to help students understand programming, computer science, mathematics, science, engineering, and other study-related concepts.

## Features

- Answers study-related questions using an LLM
- Simple and clean chatbot interface
- Restricts responses to academic and educational topics
- Real-time communication between frontend and backend
- Lightweight Python backend using Flask

## Tech Stack

- HTML
- CSS
- JavaScript
- Python
- Flask
- OpenAI API

## How It Works

1. The user enters a study question in the frontend.
2. JavaScript sends the question to the Flask backend using a POST request.
3. The Flask backend sends the question to the OpenAI API.
4. The language model generates a response.
5. The backend returns the response as JSON.
6. The frontend displays the answer in the chat interface.

## Project Structure

```text
studybuddy-ai/
├── app.py
├── index.html
└── README.md
