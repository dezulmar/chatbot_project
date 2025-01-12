from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Masukkan API Key OpenAI Anda
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Ambil pesan dari body permintaan
        data = request.json
        user_message = data.get('message', '')

        # Panggil API ChatGPT untuk mendapatkan respons
    response = openai.ChatCompletion.acreate(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)

        # Ambil respons dari ChatGPT
        chatbot_reply = response['choices'][0]['message']['content']
        return jsonify({"reply": chatbot_reply}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
