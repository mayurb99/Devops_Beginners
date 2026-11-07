# Lecture 6 — Hub, ECR, Fargate

Module 2: AWS and Containers.

**Theory (read the deck):** tags vs `latest`. Docker Hub vs Amazon ECR. Azure/GCP names (ACR + Container Apps, Artifact Registry + Cloud Run). Fargate = ECS runs the image; you do not SSH in. Secrets do not belong in the image. Non-root `USER` in the Dockerfile. Compose is skipped (one service — lecture 5 `docker run` is enough).

**Demo (~75 min, cleanup included):** Amazon Linux EC2 for Docker (no Docker Desktop). Console launches the box (CLI-0 to CLI-3) plus ECR and Fargate. Git Bash is SSH and the Fargate `curl`. Path: `docker build` / `docker run` `/health` on the EC2 → push `:l6` to Docker Hub → push `:l6` to ECR → Fargate public IP → `curl` from Windows → delete the same day.

Fargate uses a **public subnet + public IP** so it can pull ECR **without** lecture 4’s NAT. Security group **8080** is for this demo only. Terminate the practice EC2. Lecture 11 still deploys with GitHub Actions onto **one** project EC2 — not Fargate.

## Folder

```text
lec-06/
├── README.md
├── assignment.md
├── presentation/lec-06-hub-ecr-fargate.pptx
├── codebase/
│   ├── hub-ecr-fargate-lab-instructions.txt
│   └── notes-api/
│       ├── notes-api.py
│       ├── Dockerfile
│       ├── .dockerignore
│       └── README.md
└── resources/
    ├── path.png
    ├── hub-ecr.png
    ├── three-clouds.png
    ├── ec2-vs-fargate.png
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
