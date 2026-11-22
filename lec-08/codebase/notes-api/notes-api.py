# Lecture 8 — same notes-api HTML page.
# PAGE_TITLE and PAGE_SUB come from a ConfigMap (env). The page prints them.
# NOTES_TOKEN comes from a Secret. The page prints that dummy class token too.
# Real apps do not print secrets. This one does so you can see envFrom worked.
# CRASH=1 makes the process exit so you can see CrashLoopBackOff.
# HOSTNAME is the Pod name. Two Pods = two Python lists.
# You RUN this. You do not rewrite it.

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import sys

if os.environ.get("CRASH", "") == "1":
    print("CRASH=1 is set. Exiting on purpose so you can see CrashLoopBackOff.", flush=True)
    sys.exit(1)

notes = [
    {"id": 1, "text": "Lecture 1: Linux"},
    {"id": 2, "text": "Lecture 2: REST APIs"},
]

POD = os.environ.get("HOSTNAME", "local")
TITLE = os.environ.get("PAGE_TITLE", "notes-api")
SUB = os.environ.get("PAGE_SUB", "Lecture 8. Two Pods mean two lists.")
TOKEN = os.environ.get("NOTES_TOKEN", "")
TOKEN_SET = "yes" if TOKEN else "no"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>__TITLE__</title>
  <style>
    body { margin: 0; font-family: Calibri, Segoe UI, sans-serif; background: #F8FAFC; color: #0F172A; }
    main { max-width: 640px; margin: 48px auto; background: #fff; padding: 32px; border-radius: 12px;
           box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08); }
    h1 { margin: 0 0 6px; color: #0F766E; font-size: 28px; }
    .sub { color: #64748B; margin: 0 0 24px; }
    label { display: block; font-weight: 700; margin-bottom: 8px; }
    input { width: 100%; box-sizing: border-box; padding: 10px 12px; font-size: 16px;
            border: 1px solid #CBD5E1; border-radius: 8px; }
    .row { display: flex; gap: 12px; margin: 16px 0 28px; }
    button { font-size: 16px; padding: 10px 18px; border-radius: 8px; cursor: pointer; }
    .add { background: #0F766E; color: #fff; border: 0; }
    .show { background: #fff; color: #0F172A; border: 1px solid #0F172A; }
    h2 { font-size: 18px; margin: 0 0 12px; }
    li { margin: 8px 0; }
    .id { color: #64748B; margin-right: 8px; }
    .err { color: #B45309; }
    .pod { margin-top: 24px; font-size: 14px; color: #64748B; }
    .from { margin-top: 28px; padding: 16px; background: #F1F5F9; border-radius: 8px; font-size: 14px; }
    .from p { margin: 6px 0; }
    .from .warn { color: #B45309; margin-top: 12px; }
  </style>
</head>
<body>
  <main>
    <h1>__TITLE__</h1>
    <p class="sub">__SUB__</p>
    <label for="text">Write a note</label>
    <input id="text" placeholder="Example: this note may vanish on Show">
    <div class="row">
      <button class="add" type="button" onclick="addNote()">Add note</button>
      <button class="show" type="button" onclick="showNotes()">Show notes</button>
    </div>
    <h2>Notes</h2>
    <ul id="list"></ul>
    <p id="msg" class="err"></p>
    <p class="pod">This page was served by Pod: <strong id="pod">…</strong></p>
    <div class="from">
      <p><strong>From ConfigMap</strong> (plain settings)</p>
      <p>PAGE_TITLE: <strong id="cm-title">__TITLE__</strong></p>
      <p>PAGE_SUB: <strong id="cm-sub">__SUB__</strong></p>
      <p><strong>From Secret</strong> (dummy class token, not an AWS key)</p>
      <p>NOTES_TOKEN: <strong id="tok">__TOKEN__</strong></p>
      <p class="warn">Class only: we print the Secret so you can see the app read it. A real app would not put this on the page.</p>
    </div>
  </main>
  <script>
    function msg(t) { document.getElementById("msg").textContent = t || ""; }
    async function who() {
      const r = await fetch("/health");
      const d = await r.json();
      document.getElementById("pod").textContent = d.pod || "unknown";
      if (d.title) document.getElementById("cm-title").textContent = d.title;
      if (d.sub) document.getElementById("cm-sub").textContent = d.sub;
      document.getElementById("tok").textContent = d.token || "(empty)";
    }
    async function showNotes() {
      msg("");
      const r = await fetch("/notes");
      const d = await r.json();
      const ul = document.getElementById("list");
      ul.innerHTML = "";
      (d.notes || []).forEach(function (n) {
        const li = document.createElement("li");
        li.innerHTML = '<span class="id">' + n.id + "</span>" + n.text;
        ul.appendChild(li);
      });
      who();
    }
    async function addNote() {
      const box = document.getElementById("text");
      const text = box.value.trim();
      if (!text) { msg("Type a note first."); return; }
      msg("");
      await fetch("/notes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
      });
      box.value = "";
      showNotes();
    }
    showNotes();
  </script>
</body>
</html>
""".replace("__TITLE__", esc(TITLE)).replace("__SUB__", esc(SUB)).replace("__TOKEN__", esc(TOKEN or "(empty)"))


def send(handler, status, data):
    body = json.dumps(data).encode()
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.end_headers()
    handler.wfile.write(body)


def send_html(handler, html):
    body = html.encode("utf-8")
    handler.send_response(200)
    handler.send_header("Content-Type", "text/html; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
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


def clean_path(path):
    return path.split("?")[0]


class NotesAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        path = clean_path(self.path)
        if path in ("/", "/index.html"):
            send_html(self, PAGE)
        elif path == "/health":
            send(self, 200, {
                "status": "ok",
                "pod": POD,
                "title": TITLE,
                "sub": SUB,
                "token": TOKEN,
                "token_set": bool(TOKEN),
            })
        elif path == "/notes":
            send(self, 200, {"notes": notes, "pod": POD})
        else:
            send(self, 404, {"error": "not found"})

    def do_POST(self):
        if clean_path(self.path) != "/notes":
            send(self, 404, {"error": "not found"})
            return
        data = read_json(self)
        new_note = {"id": len(notes) + 1, "text": data.get("text", "")}
        notes.append(new_note)
        send(self, 201, new_note)

    def do_PUT(self):
        note = find_note(id_from_path(clean_path(self.path)))
        if note is None:
            send(self, 404, {"error": "not found"})
            return
        data = read_json(self)
        note["text"] = data.get("text", "")
        send(self, 200, note)

    def do_PATCH(self):
        note = find_note(id_from_path(clean_path(self.path)))
        if note is None:
            send(self, 404, {"error": "not found"})
            return
        data = read_json(self)
        if "text" in data:
            note["text"] = data["text"]
        send(self, 200, note)

    def do_DELETE(self):
        note = find_note(id_from_path(clean_path(self.path)))
        if note is None:
            send(self, 404, {"error": "not found"})
            return
        notes.remove(note)
        send(self, 200, {"deleted": note["id"]})


host = os.environ.get("HOST", "0.0.0.0")
port = int(os.environ.get("PORT", "8080"))
print("API is running at http://%s:%s" % (host, port), flush=True)
print("Title=%s  token_set=%s  pod=%s" % (TITLE, TOKEN_SET, POD), flush=True)
print("Open / in a browser. JSON is still at /notes and /health.", flush=True)
HTTPServer((host, port), NotesAPI).serve_forever()
