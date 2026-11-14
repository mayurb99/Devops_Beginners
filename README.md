# DevOps for Beginners

A 16-lecture beginner DevOps course for a **DevOps Engineer** seat on **AWS Free Tier**.

**Syllabus (1–2 page index):** [curriculum.md](curriculum.md) · [DevOps-Foundation-Curriculum.docx](DevOps-Foundation-Curriculum.docx)

CI/CD is **GitHub Actions**, not Jenkins. There is **no Git/GitHub lecture**. Kubernetes is on the laptop (`kind`), not EKS. The AWS deploy is **one** free-tier EC2 running a container.

## Lecture 1 — Introduction to DevOps and Linux

[lec-01/README.md](lec-01/README.md) — already taught.

## Lecture 2 — REST APIs

[lec-02/README.md](lec-02/README.md)

- Student-readable PowerPoint
- Lab: run `notes-api.py`, then `curl` (Postman optional)
- Instruction list: `lec-02/codebase/api-lab-instructions.txt`

## Lecture 3 — Networking

[lec-03/README.md](lec-03/README.md)

- Student-readable PowerPoint (general networking + cloud VPC). No required lab.
- Optional practice only: `lec-03/codebase/networking-lab-instructions.txt`

## Lecture 4 — AWS Fundamentals

[lec-04/README.md](lec-04/README.md)

- Three-cloud theory. AWS console demo (VPC, NAT, two hellos + ALB, S3, Lambda).
- Lab: `lec-04/codebase/aws-lab-instructions.txt` · Assignment: `lec-04/assignment.md`
- Delete NAT and the load balancer the same day.

## Lecture 5 — Docker

[lec-05/README.md](lec-05/README.md)

- Student-readable PowerPoint (image vs container, Dockerfile, ports, env, volumes)
- Lab: console launches one EC2 (CLI-0 to CLI-3); Docker and `curl /health` run **on that Linux box** (no Docker Desktop)
- Assignment: `lec-05/assignment.md` — terminate the instance the same day

## Lecture 6 — Hub, ECR, Fargate

[lec-06/README.md](lec-06/README.md)

- Student-readable PowerPoint (path diagrams, Hub vs ECR, Azure/GCP names, Fargate, money)
- Lab: `docker build` / `run` on one Amazon Linux EC2; push `:l6` to Docker Hub and ECR; one Fargate task (public IP); `curl` `/health` from Windows; delete the same day. No Compose.
- Assignment: `lec-06/assignment.md` — Fargate and the practice EC2 must be gone before the student leaves
- Lecture 11 project is still one EC2 + GitHub Actions, not Fargate

## Lecture 7 — Kubernetes on EKS

[lec-07/README.md](lec-07/README.md)

- Student-readable PowerPoint (why not Fargate only; cluster, Pod, Deployment, Service, diagrams)
- Lab: VPC → ECR `notes-api:l7` → EKS in the console → Service LoadBalancer → HTML page in the browser. `kubectl` in CloudShell
- Assignment: `lec-07/assignment.md` — delete the cluster the same day (control plane is billed while it exists)
