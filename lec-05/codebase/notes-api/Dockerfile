# Lecture 5 — recipe for the notes-api image.
# You do not need to invent this. Read each line, then build.

# Base image: Python already installed. "slim" = smaller than the full image.
FROM python:3.12-slim

# Folder inside the container where we put our file.
WORKDIR /app

# Copy only the API file into that folder.
COPY notes-api.py .

# Document the door the app listens on. This does NOT publish it to your laptop.
# Publishing is docker run -p ...
EXPOSE 8080

# -u = unbuffered prints, so "API is running" shows in docker logs immediately.
CMD ["python", "-u", "notes-api.py"]
