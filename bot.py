import os
import requests
from flask import Flask, request

app = Flask(__name__)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8741441665:AAG4ZVlk5B-CwNWsXktU8ySZuGGttTcaeg0")
API_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["GET"])
def index():
    return "Hermes Cloud Bot is active and running perfectly.", 200

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    if update and "message" in update:
        message = update["message"]
        chat_id = message["chat"]["id"]
        user_text = message.get("text", "")
        response_text = f"🤖 أهلاً بك يا عمر. تلقيت أمرك السحابي: {user_text}"
        requests.post(f"{API_URL}/sendMessage", json={"chat_id": chat_id, "text": response_text})
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
