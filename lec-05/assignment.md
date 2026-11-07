# Lecture 5 assignment

Follow `codebase/docker-lab-instructions.txt`. Docker runs on the EC2. Console launches the instance (CLI-0 to CLI-3). Git Bash is SSH after that.

---

## 1. Image vs container

In your own words: what is an **image**? What is a **container**?  
Which command created the image? Which command created a container?

---

## 2. Health check

Paste the `curl` command you used and the JSON you got for `/health`.  
(You curled on the EC2, not from Windows.)

---

## 3. Ports

What does `-p 8080:8080` mean (left vs right)?  
Left is the **host** (the EC2). Right is inside the container.  
What happened when you used `-p 9090:8080`?

---

## 4. Env mismatch

You ran `-e PORT=9090` with `-p 8080:8080`. Did `/health` work? Why or why not?

---

## 5. Volume

You wrote `from-container.txt`, removed the container, started a new one with the same volume. Was the file still there?

---

## 6. stop vs rm vs rmi

One line each: `docker stop`, `docker rm`, `docker rmi`.  
After `rm`, is the image still on the EC2?

---

## 7. 0.0.0.0 vs 127.0.0.1

Why does the Lecture 5 API listen on `0.0.0.0` instead of `127.0.0.1`?

---

## 8. Later (names only)

Where in this course do we push an image (Hub + ECR)? Where do we run a short Fargate demo? Where is Kubernetes? (Project deploy in lecture 11 is still one EC2.)

---

## Cleanup

- [ ] Instance `lec05-docker` is **terminated** (not only stopped)  
- [ ] Security group `lec05-docker-ssh` deleted  
- [ ] No container left running  
