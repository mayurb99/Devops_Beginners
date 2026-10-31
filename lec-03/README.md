# Lecture 3 — Networking

Teaching pack. Module 1: Foundations.

The PowerPoint **is** the lesson. Written for someone with **no networking background**. There is **no required lab**.

**First:** only the words a cloud beginner needs — DNS, IP (public vs private), port, HTTPS as encrypted HTTP, then how a request fails.

**Then:** the same picture in the cloud (AWS / Azure / GCP names) — VPC/VNet, CIDR, subnet, route table, Internet Gateway vs NAT, security group / NSG, NACL, Elastic IP, endpoints, flow logs, WAF, load balancer, cloud DNS, peering / VPN (names).

Not in this lecture: OSI, TCP vs UDP, frames, MAC, ARP, switches, routers, DHCP, certificates in depth.

Lecture 4 is clicking the public-subnet picture on AWS. Do not create a NAT Gateway, load balancer, or extra EC2 in this course.

## The PowerPoint is written for students to read

`presentation/lec-03-networking.pptx` explains every idea on the slides, with examples.

## Learning objectives

1. Read a URL as DNS → IP → port → HTTP (HTTPS = encrypted).
2. Tell public IP from private IP, and name common ports (22, 80, 443, 8080).
3. Tell connection refused, timeout, and HTTP 403 apart.
4. Draw a VPC: public subnet, private subnet, IGW, NAT, security group.
5. Map those boxes to AWS, Azure, and GCP names.
6. Explain why this course uses a public subnet (NAT costs money).

## No required lab

Examples (`curl`, `ping`, `tracert`) are printed on the slides. Optional practice lives in `codebase/networking-lab-instructions.txt` if a student wants it at home.

## Folder structure

```text
lec-03/
├── README.md
├── presentation/lec-03-networking.pptx
├── codebase/
│   └── networking-lab-instructions.txt   (optional)
└── resources/
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
