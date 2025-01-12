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
