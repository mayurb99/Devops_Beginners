# Lecture 6 — same API as lecture 5, plus a non-root user.
# You read this. You do not invent a new one today.

FROM python:3.12-slim

WORKDIR /app
COPY notes-api.py .

# Process is not root. Port 8080 does not need root.
RUN useradd --create-home --uid 10001 appuser \
    && chown appuser:appuser /app/notes-api.py
USER appuser

EXPOSE 8080
CMD ["python", "-u", "notes-api.py"]
