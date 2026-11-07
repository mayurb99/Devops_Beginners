# notes-api (Lecture 5)

Same API as lecture 2. This copy listens on `0.0.0.0` so Docker can map port 8080 to your laptop.

You **run the container**. You do not rewrite the Python.

```bash
cd lec-05/codebase/notes-api
docker build -t notes-api:l5 .
docker run --rm -p 8080:8080 notes-api:l5
```

Then: `curl http://127.0.0.1:8080/health`

Follow `../docker-lab-instructions.txt`.
