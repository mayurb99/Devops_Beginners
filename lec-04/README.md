# Lecture 4 — AWS Fundamentals

75-minute teaching pack. Module 2: AWS and Containers.

**Curriculum:** account, Region, billing alarm, IAM, VPC (public subnet only), Internet Gateway, security group, one t3.micro / t2.micro, S3, stop vs terminate.

**Hard rule:** billing alarm **before** the instance. Stop the instance before you leave. No NAT Gateway, no load balancer, no RDS, no second EC2, no EKS.

## The PowerPoint is written for students to read

`presentation/lec-04-aws-fundamentals.pptx` explains every idea on the slides.

## Learning objectives

1. Create a billing alarm / budget on day one.
2. Explain IAM user vs role vs policy, and least privilege.
3. Draw VPC → public subnet → Internet Gateway → security group → one EC2.
4. Launch one Free Tier micro instance and **stop** it.
5. Create a private S3 bucket.
6. Map the same ideas to Azure and GCP by name only.

## Lab

Follow `codebase/aws-lab-instructions.txt` in the AWS console.

Pick **one Region** and stay there (example: `ap-south-1` Mumbai).

## Folder structure

```text
lec-04/
├── README.md
├── presentation/lec-04-aws-fundamentals.pptx
├── codebase/
│   └── aws-lab-instructions.txt
└── resources/
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
