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


def find_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


def id_from_path(path):
    # "/notes/1" -> 1
    parts = path.split("/")
    if len(parts) == 3 and parts[1] == "notes" and parts[2].isdigit():
        return int(parts[2])
    return None


def read_json(handler):
    size = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(size)
    return json.loads(body)


class NotesAPI(BaseHTTPRequestHandler):
    # You never type these yourself.
    # HTTPServer waits, then Python calls:
    #   GET    -> do_GET
    #   POST   -> do_POST
    #   PUT    -> do_PUT
    #   PATCH  -> do_PATCH
    #   DELETE -> do_DELETE

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
        # PUT = replace the whole note
        note = find_note(id_from_path(self.path))
        if note is None:
            send(self, 404, {"error": "not found"})
            return
        data = read_json(self)
        note["text"] = data.get("text", "")
        send(self, 200, note)

    def do_PATCH(self):
        # PATCH = change only the field you send
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


print("API is running at http://127.0.0.1:8080")
print("Stop with Ctrl+C")
HTTPServer(("127.0.0.1", 8080), NotesAPI).serve_forever()
