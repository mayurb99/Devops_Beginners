# Lecture 5 interview questions

Speak in your own words.

---

## 1. Why Docker?

**Spoken:** “So the app plus its runtime travel together. If it runs in the container on my laptop, the same image runs on a classmate’s laptop or later on EC2.”

---

## 2. Image vs container?

**Spoken:** “An image is the packed recipe, read-only. A container is a running (or stopped) instance of that image. I can start many containers from one image.”

---

## 3. What is a Dockerfile?

**Spoken:** “A text file of steps: FROM a base image, COPY my app, CMD to start it. `docker build` walks those steps and stores layers.”

---

## 4. What does `-p 8080:8080` mean?

**Spoken:** “Left is the port on my laptop. Right is the port inside the container. curl to 127.0.0.1:8080 hits the laptop door, which Docker forwards inside.”

---

## 5. Why 0.0.0.0 inside the container, not 127.0.0.1?

**Spoken:** “127.0.0.1 inside the container is only the container. Docker’s port map cannot reach it. 0.0.0.0 means all interfaces inside, so -p works.”

---

## 6. stop vs rm vs rmi?

**Spoken:** “stop turns the process off. rm deletes that container. rmi deletes the image. After rm the image is still on disk.”

---

## 7. What is a volume?

**Spoken:** “A folder that lives outside the container’s writable layer. If I rm the container, files in a named volume are still there.”

---

## 8. Where do images go in the cloud?

**Spoken:** “A registry. AWS ECR, Azure ACR, GCP Artifact Registry. We push in lecture 6. Running without managing a VM is Fargate / Cloud Run — named later, not today.”
