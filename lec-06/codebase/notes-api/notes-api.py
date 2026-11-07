# Tiny practice API for Lecture 6 (Compose, Hub, ECR, Fargate).
# Same app as lecture 5. Listens on 0.0.0.0 so Docker and Fargate can reach it.
# You RUN this inside a container. You do not rewrite it.

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

notes = [
    {"id": 1, "text": "Lecture 1: Linux"},
    {"id": 2, "text": "Lecture 2: REST APIs"},
]


def send(handler, status, data):
    body = json.dumps(data).encode()
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.end_headers()
    handler.wfile.write(body)


def find_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


def id_from_path(path):
    parts = path.split("/")
    if len(parts) == 3 and parts[1] == "notes" and parts[2].isdigit():
        return int(parts[2])
    return None


def read_json(handler):
    size = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(size)
    return json.loads(body)


class NotesAPI(BaseHTTPRequestHandler):
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

    def do_POST(self):
        if self.path != "/notes":
            send(self, 404, {"error": "not found"})
            return
        data = read_json(self)
        new_note = {"id": len(notes) + 1, "text": data.get("text", "")}
        notes.append(new_note)
        send(self, 201, new_note)

    def do_PUT(self):
        note = find_note(id_from_path(self.path))
        if note is None:
            send(self, 404, {"error": "not found"})
            return
        data = read_json(self)
        note["text"] = data.get("text", "")
        send(self, 200, note)

    def do_PATCH(self):
        note = find_note(id_from_path(self.path))
        if note is None:
            send(self, 404, {"error": "not found"})
            return
        data = read_json(self)
        if "text" in data:
            note["text"] = data["text"]
        send(self, 200, note)

    def do_DELETE(self):
        note = find_note(id_from_path(self.path))
        if note is None:
            send(self, 404, {"error": "not found"})
            return
        notes.remove(note)
        send(self, 200, {"deleted": note["id"]})


host = os.environ.get("HOST", "0.0.0.0")
port = int(os.environ.get("PORT", "8080"))
print("API is running at http://%s:%s" % (host, port), flush=True)
print("Stop with Ctrl+C", flush=True)
HTTPServer((host, port), NotesAPI).serve_forever()
