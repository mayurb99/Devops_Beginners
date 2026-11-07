# Lecture 5 — Docker

Module 2: AWS and Containers.

**Theory (read the deck):** why containers, image vs container, Dockerfile and layers, ports, env, volumes, `.dockerignore`. Registries and Fargate are **named** (Lecture 6 / later).

**Demo host:** Amazon Linux EC2. Windows has no Docker Desktop. **Console** (CLI-0 to CLI-3) starts the instance; Git Bash is only SSH/`scp` after that. `sudo docker` runs **on** that Linux box. Curl `/health` from a second SSH session (127.0.0.1 on the EC2 — not from Windows).

Then: `ps`, `logs`, `exec`, port map, env mismatch, volume, stop/start/rm. Terminate the instance when class ends.

This copy of notes-api listens on `0.0.0.0` so `docker run -p` works. Lecture 2 used `127.0.0.1` (that process only).

No Compose, no ECR, no Fargate, no NAT, no ALB today. Do not open port 8080 on the security group.

## Folder

```text
lec-05/
├── README.md
├── assignment.md
├── presentation/lec-05-docker.pptx
├── codebase/
│   ├── docker-lab-instructions.txt
│   └── notes-api/
│       ├── notes-api.py
│       ├── Dockerfile
│       ├── .dockerignore
│       └── README.md
└── resources/
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
