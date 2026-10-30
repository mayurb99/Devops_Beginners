# Lecture 3 — Networking

75-minute teaching pack. Module 1: Foundations.

**Curriculum:** DNS, IP, TCP, ports, TLS. Then the same cloud network on every provider: VPC/VNet, CIDR, subnets, route tables, Internet Gateway, NAT, security groups / NSG / firewall, NACLs, public vs Elastic IP, load balancers, cloud DNS. Failures: refused vs timeout vs 403.

Do not create a NAT Gateway, load balancer, or EC2 instance today. Lecture 4 is clicking this picture on AWS.

## The PowerPoint is written for students to read

`presentation/lec-03-networking.pptx` explains every idea on the slides.

## Learning objectives

1. Read a URL as DNS → IP → TCP port → TLS → HTTP.
2. Tell connection refused, timeout, and 403 apart.
3. Draw a VPC: public subnet, private subnet, IGW, NAT, security group.
4. Map those boxes to AWS, Azure, and GCP names.
5. Explain why this course uses a public subnet (NAT costs money).
6. Use `curl -v` to see why a request failed.

## Lab

Follow `codebase/networking-lab-instructions.txt` line by line.

You will reuse notes-api from lecture 2. Start it, then break connections on purpose.

## Folder structure

```text
lec-03/
├── README.md
├── presentation/lec-03-networking.pptx
├── codebase/
│   └── networking-lab-instructions.txt
└── resources/
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
