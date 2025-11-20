from flask import Flask, request, jsonify, render_template
from gpt4all import GPT4All

app = Flask(__name__)

# Load GPT4All model
model = GPT4All("ggml-gpt4all-j-v1.3-groovy")  # Download model once

conversation_history = []

def ai_response(message):
    conversation_history.append(f"You: {message}")
    prompt = "\n".join(conversation_history) + "\nAI:"
    response = model.generate(prompt)
    conversation_history.append(f"AI: {response}")
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = ai_response(user_message)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
