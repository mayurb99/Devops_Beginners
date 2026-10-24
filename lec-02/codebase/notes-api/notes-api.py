# Tiny practice API for Lecture 2.
# You only RUN this file. Then you call it with curl.
# You do not need to change anything here.

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

notes = [
    {"id": 1, "text": "Lecture 1: Linux"},
    {"id": 2, "text": "Lecture 2: REST APIs"},
]


def send(handler, status, data):
    """Send a JSON answer back to curl / Postman."""
    body = json.dumps(data).encode()
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.end_headers()
    handler.wfile.write(body)


class NotesAPI(BaseHTTPRequestHandler):
    # You never type do_GET() or do_POST() yourself.
    # HTTPServer below waits for a request, then Python calls:
    #   curl GET  ...  ->  do_GET
    #   curl POST ...  ->  do_POST

    # GET = read
    def do_GET(self):
        if self.path == "/health":
            send(self, 200, {"status": "ok"})
        elif self.path == "/notes":
            send(self, 200, {"notes": notes})
        elif self.path == "/notes/secret":
            key = self.headers.get("X-API-Key", "")
            if key == "lecture2-key":
                send(self, 200, {"secret": "the API key worked"})
            else:
                send(self, 401, {"error": "missing or wrong API key"})
        else:
            send(self, 404, {"error": "not found"})

    # POST = create
    def do_POST(self):
        if self.path != "/notes":
            send(self, 404, {"error": "not found"})
            return

        size = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(size)
        data = json.loads(body)
        text = data.get("text", "")

        new_note = {"id": len(notes) + 1, "text": text}
        notes.append(new_note)
        send(self, 201, new_note)


print("API is running at http://127.0.0.1:8080")
print("Stop with Ctrl+C")
# This line starts the server and waits.
# Each incoming request makes Python call do_GET or do_POST above.
HTTPServer(("127.0.0.1", 8080), NotesAPI).serve_forever()
