# notes-api (Lecture 6)

Same API as lecture 5. Listens on `0.0.0.0`. Non-root `USER` in the Dockerfile.

```bash
sudo docker build -t notes-api:l6 .
sudo docker run --rm -p 8080:8080 --name notes-l6 notes-api:l6
curl http://127.0.0.1:8080/health
```

Do not put secrets in this folder. Do not rewrite the Python.
