from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean = path.split("?", 1)[0].split("#", 1)[0]
        if clean == "/docs":
            clean = "/docs/index.html"
        elif clean.endswith("/"):
            clean += "index.html"
        return str(ROOT / clean.lstrip("/"))

    def do_POST(self):
        body = b'{"error":"Live backend actions are disabled in this local mirror."}'
        self.send_response(503)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(fmt % args, flush=True)


if __name__ == "__main__":
    os.chdir(ROOT)
    print("SXG mirror: http://127.0.0.1:4173/", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 4173), Handler).serve_forever()
