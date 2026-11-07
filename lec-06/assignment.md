# Lecture 6 assignment

Follow `codebase/hub-ecr-fargate-lab-instructions.txt`. Docker runs on the EC2. Fargate `curl` is from **Windows** Git Bash. Cleanup is part of the grade.

---

## 1. Ports

What does `-p 8080:8080` mean (left vs right)?  
You curled `/health` on the EC2 — which number did you use?

---

## 2. Health on the EC2

Paste the `curl` you ran **on the EC2** after `docker run`, and the JSON you got.

---

## 3. Tags

Why did we push `:l6` instead of `:latest`?  
One sentence.

---

## 4. Hub vs ECR

In your own words: what is Docker Hub for? What is Amazon ECR for?  
Which one did Fargate pull from today?

---

## 5. Azure and GCP names

What is the Azure name for ECR? For Fargate?  
What is the GCP name for ECR? For Fargate?

---

## 6. Fargate curl

Paste the `curl` from **Windows** to the Fargate public IP (`/health`) and the JSON.  
Why could you not SSH into that container?

---

## 7. Public IP (no NAT)

Fargate sat in a **public** subnet with **public IP on**. Why?  
What would break if public IP were off and there was no NAT?

---

## 8. Secrets, user, later

Name two things that must not go in the image.  
What does `USER appuser` change?  
Where does the **project** run the container in lecture 11 — Fargate or EC2?

---

## Cleanup (tick)

- [ ] ECS service `notes-svc` deleted (desired was 0 first)
- [ ] Cluster `lec06-cluster` deleted
- [ ] Task definition `notes-api` deregistered
- [ ] ECR repository `notes-api` deleted
- [ ] Instance `lec06-docker` **terminated**
- [ ] Security groups `lec06-fargate-8080` and `lec06-docker-ssh` deleted
- [ ] CloudWatch log group for the task deleted
- [ ] IAM role `lec06-ec2-ecr` deleted (or noted if you kept it)
