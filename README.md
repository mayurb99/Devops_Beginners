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

- Path of a request: DNS → IP → port → TLS → HTTP
- Lab: `lec-03/codebase/networking-lab-instructions.txt` (`curl -v`)

## Lecture 4 — AWS Fundamentals

[lec-04/README.md](lec-04/README.md)

- Billing alarm first. One micro EC2. Stop it.
- Lab: `lec-04/codebase/aws-lab-instructions.txt` (no NAT, no ALB, no RDS)
