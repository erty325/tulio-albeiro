from flask import Flask
import threading
import os

app = Flask('')


@app.route('/')
def home():
    return 'Bot is running!'


def run():
    port = int(os.environ.get('PORT', 8000))
    # debug and reloader disabled for thread
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)


def start():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
