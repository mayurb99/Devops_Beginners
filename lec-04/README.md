# Lecture 4 — AWS Fundamentals

Module 2: AWS and Containers.

**Theory (read the deck):** each service in plain words, with an example, then the same idea on **AWS, Azure, and GCP**. Slides mark **Different** when a cloud is not a copy of AWS. One slide lists what we skip today and what later lectures or the project cover.

**Demo (long, AWS console, buttons only):** follow `codebase/aws-lab-instructions.txt`. No CLI.

**Assignment:** `assignment.md` — use cases you must have seen, three-cloud table, cleanup required.

Lecture 3 already explained VPC / subnet / IGW / NAT / SG. Today we **create** them and **test** the use cases.

## What you create

- Custom VPC, public + private subnet, Internet Gateway, NACL, security groups
- NAT Gateway (after proving the private VM has no internet)
- Two EC2 hello-world apps + Application Load Balancer (refresh to see A vs B)
- One private EC2 (no public IP)
- Elastic IP vs ordinary public IP (stop/start)
- SSH closed, then SSH 22 from My IP
- One S3 bucket + Lambda with an S3 trigger

## Theory only (do not create)

Database (RDS, DynamoDB, …). Extra disks / EFS / Glacier. Fargate (Docker lectures). EKS (Kubernetes lectures; class uses kind). Azure and GCP consoles.

## Money

NAT Gateway and the load balancer are billed by the hour. **Section Z** of the lab deletes them the same day. Unused Elastic IPs are billed. Budget **before** any of that.

## Folder

```text
lec-04/
├── README.md
├── assignment.md
├── presentation/lec-04-aws-fundamentals.pptx
├── codebase/
│   ├── README.md
│   └── aws-lab-instructions.txt
└── resources/
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
