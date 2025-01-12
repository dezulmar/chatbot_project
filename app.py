from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Masukkan API Key OpenAI Anda
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Ambil data JSON dari permintaan
        data = request.json
        user_message = data.get('message', '')

        # Validasi jika pesan kosong
        if not user_message:
            return jsonify({"error": "Message field is required"}), 400

        # Panggil OpenAI Chat API
        response = openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",  # Anda juga bisa menggunakan model "gpt-4"
            messages=[{"role": "user", "content": user_message}]
        )

        # Ambil respons dari ChatGPT
        chatbot_reply = response['choices'][0]['message']['content']
        return jsonify({"reply": chatbot_reply}), 200

    except Exception as e:
        # Tangani error dan kirimkan respons ke klien
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
