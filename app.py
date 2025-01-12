import openai
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Set API Key
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        logging.debug(f"Request data: {data}")

        # Validate input
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # OpenAI ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Gunakan model terbaru
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        bot_reply = response['choices'][0]['message']['content']

        return jsonify({"reply": bot_reply})

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
