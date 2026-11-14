# Lecture 7 — notes-api with the HTML page at GET /
# You read this. You do not invent a new one today.

FROM python:3.12-slim

WORKDIR /app
COPY notes-api.py .

RUN useradd --create-home --uid 10001 appuser \
    && chown appuser:appuser /app/notes-api.py
USER appuser

EXPOSE 8080
CMD ["python", "-u", "notes-api.py"]
