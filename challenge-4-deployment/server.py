from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", "8000"))


class InventoryHandler(BaseHTTPRequestHandler):

    def send_json(self, status, data):

        body = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        self.wfile.write(body)

    def do_GET(self):

        if self.path == "/health":
            self.send_json(200, {"status": "ok"})

        elif self.path == "/":
            self.send_json(200, {
                "service": "inventory-api",
                "port": PORT
            })

        else:
            self.send_json(404, {"error": "not_found"})

    def log_message(self, fmt, *args):
        print(fmt % args, flush=True)


if __name__ == "__main__":

    print(
        f"Inventory API listening on {HOST}:{PORT}",
        flush=True
    )

    server = ThreadingHTTPServer(
        (HOST, PORT),
        InventoryHandler
    )

    server.serve_forever()