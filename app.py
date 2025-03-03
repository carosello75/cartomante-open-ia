
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Imposta la tua chiave API OpenAI (sostituisci con la tua reale!)
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/ask', methods=['POST'])
def ask_cartomante():
    data = request.get_json()
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"error": "Nessuna domanda ricevuta"}), 400

    # Chiamata a OpenAI per ottenere la risposta della Cartomante
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu sei una cartomante sensuale e intrigante, pronta a leggere il destino."},
            {"role": "user", "content": user_question}
        ]
    )

    ai_answer = response['choices'][0]['message']['content']

    return jsonify({"answer": ai_answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
