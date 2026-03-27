from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# SMALL MODEL (IMPORTANT)
generator = pipeline("text-generation", model="sshleifer/tiny-gpt2")

@app.route("/")
def home():
    return "Tiny GPT-2 API running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    result = generator(prompt, max_length=30)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
