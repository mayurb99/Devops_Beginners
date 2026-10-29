# Lecture 3 — Networking

75-minute teaching pack. Module 1: Foundations.

**Curriculum:** DNS, IP, TCP, ports, TLS, load balancers, proxies, firewalls, security groups, connection refused vs timeout vs 403, public vs private IP.

Do not open the AWS console today except as a picture. Do not create a NAT Gateway, load balancer, or EC2 instance. That is lecture 4.

## The PowerPoint is written for students to read

`presentation/lec-03-networking.pptx` explains every idea on the slides.

## Learning objectives

1. Read a URL as DNS → IP → TCP port → TLS → HTTP.
2. Explain a port in one sentence.
3. Tell connection refused, timeout, and 403 apart.
4. Tell public IP from private IP.
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
