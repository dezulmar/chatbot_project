from flask import Flask, request, jsonify
import openai
import logging
import os

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Inisialisasi logging untuk debug
logging.basicConfig(level=logging.DEBUG)

# Masukkan API Key Anda (bisa langsung atau dari environment variables)
openai.api_key = "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"  # Ganti dengan API Key Anda

# Endpoint '/chat' untuk menerima permintaan POST
@app.route('/chat', methods=['POST'])
def chat():
    logging.debug("Endpoint '/chat' hit successfully.")
    try:
        # Ambil data JSON dari request
        data = request.json
        logging.debug(f"Request data: {data}")

        # Validasi apakah JSON memiliki field "message"
        user_message = data.get('message', '')
        if not user_message:
            logging.warning("Field 'message' tidak ditemukan dalam request.")
            return jsonify({"error": "Message field is required"}), 400

        # Panggil OpenAI API untuk mendapatkan balasan
        response = openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        chatbot_reply = response['choices'][0]['message']['content']
        logging.debug(f"Chatbot reply: {chatbot_reply}")

        # Return balasan sebagai JSON
        return jsonify({"reply": chatbot_reply}), 200

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500

# Menjalankan aplikasi
if __name__ == '__main__':
    # Jalankan aplikasi pada host 0.0.0.0 dan port 10000 (disesuaikan dengan Render)
    app.run(host='0.0.0.0', port=10000)
