"""Start a lightweight keep-alive HTTP server.

This module prefers Flask if it's installed (same behaviour as before),
but will fall back to Python's built-in http.server so the / endpoint
always responds with 200 even if Flask isn't available on the host.
"""

import threading
import os


def _start_flask(port: int):
    from flask import Flask

    app = Flask('')

    @app.route('/')
    def home():
        return 'Bot is running!'

    # debug and reloader disabled for thread
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)


def _start_simple_http(port: int):
    # Minimal HTTP server that responds 200 on /
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(b'Bot is running!')
            else:
                self.send_response(404)
                self.end_headers()

        def log_message(self, format, *args):
            # suppress default logging to keep logs clean
            return

    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()


def start():
    port = int(os.environ.get('PORT', 8000))
    # Try Flask first; if it's not available, fall back to simple HTTP server
    try:
        _start = _start_flask
    except Exception:
        _start = None

    if _start is None:
        # Try importing Flask at runtime; if that fails, use fallback
        try:
            # attempt to import Flask to decide
            import importlib

            importlib.import_module('flask')
            _start = _start_flask
        except Exception:
            _start = _start_simple_http

    t = threading.Thread(target=_start, args=(port,))
    t.daemon = True
    t.start()
