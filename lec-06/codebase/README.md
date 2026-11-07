# Lecture 6 lab

1. Follow `hub-ecr-fargate-lab-instructions.txt`.
2. Console starts one Amazon Linux EC2 (SSH only). `sudo docker` runs **there**.
3. Put `notes-api/` on the box (`git clone` or `scp`). Do not rewrite the Python. No Compose.
4. `docker build -t notes-api:l6 .` then `docker run --rm -p 8080:8080 --name notes-l6 notes-api:l6`.
5. Push `:l6` to Docker Hub, then to ECR.
6. Fargate runs the **ECR** image. `curl` `/health` from **Windows** to the task public IP.
7. Delete Fargate, ECR, and the EC2 the same day. Fill `../assignment.md`.
