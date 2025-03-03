from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Legge la chiave da variabile d'ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/ask', methods=['POST'])
def ask_cartomante():
    data = request.get_json()
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"error": "Nessuna domanda ricevuta"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Tu sei una cartomante sensuale e intrigante, pronta a leggere il destino."},
            {"role": "user", "content": user_question}
        ]
    )

    ai_answer = response['choices'][0]['message']['content']

    return jsonify({"answer": ai_answer})

# Usa la porta corretta di Render
port = int(os.environ.get("PORT", 10000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
