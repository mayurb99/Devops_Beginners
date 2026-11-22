# notes-api (Lecture 8)

Same HTML page as lecture 7, plus three env vars you do not bake into the image:

- `PAGE_TITLE` / `PAGE_SUB` — from a ConfigMap. Change them, restart the Pod, the heading changes.
- `NOTES_TOKEN` — from a Secret. The page and `/health` print this dummy class token so you can see the app read it. A real app would not print a Secret. Never put AWS keys here.
- `CRASH=1` — process exits on purpose (CrashLoopBackOff demo).

Notes are still a Python list in **this** process. Two Pods = two lists.

You do not rewrite this file.
