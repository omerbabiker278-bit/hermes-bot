import os
import telebot
from flask import Flask
from threading import Thread

TOKEN = "7951239082:AAH0d_w7a92FvN9z01qg2Q6XzY7eY2Q8b4c" # أو التوكن الخاص بك
bot = telebot.TeleBot(TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Hello Master Omer. Hermes received your command: {message.text}")

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == '__main__':
    keep_alive()
    bot.infinity_polling()
