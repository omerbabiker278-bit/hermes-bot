import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ضع كود البوت الأساسي الخاص بك هنا تحت keep_alive()
if __name__ == '__main__':
    keep_alive()
    # مثال لتشغيل بوت تيليجرام (استبدله بأمر التشغيل الخاص بك):
    # bot.infinity_polling()
