# Lecture 2 command cheat sheet

Run in Git Bash, WSL, or Linux. Postman is a separate app.

## Start notes-api

```bash
cd lec-02/codebase/notes-api
python notes-api.py
```

Base URL: `http://127.0.0.1:8080`

## curl

| Command | Purpose |
|---|---|
| `curl URL` | GET that URL, print the body |
| `curl -i URL` | Include response headers and status |
| `curl -v URL` | Verbose: DNS, connect, request, response |
| `curl -X POST URL` | Use POST instead of GET |
| `curl -H "Name: value"` | Add a request header |
| `curl -d '{"text":"hi"}'` | Send a request body |
| `curl -o file.txt URL` | Save the body to a file |

## Lab calls

```bash
curl -i http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/notes
curl -X POST http://127.0.0.1:8080/notes \
  -H "Content-Type: application/json" \
  -d '{"text": "hello"}'
curl -i http://127.0.0.1:8080/does-not-exist
curl -i http://127.0.0.1:8080/notes/secret
curl -i http://127.0.0.1:8080/notes/secret -H "X-API-Key: lecture2-key"
```

## Status codes to remember

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 400 | Bad request (your JSON or URL is wrong) |
| 401 | Not authenticated (missing/wrong key) |
| 403 | Authenticated, but not allowed |
| 404 | URL not found |
| 429 | Too many requests |
| 500 | Server error |
| 502 | Bad gateway (proxy got a bad answer) |
| 503 | Service unavailable |

## Optional AWS

```bash
aws --version
aws sts get-caller-identity
```

## Not today

Docker, Kubernetes, Terraform, GitHub Actions, `git init`.
