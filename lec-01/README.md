# Lecture 1 — Introduction to DevOps and Linux

This folder is the complete 75-minute teaching pack for Lecture 1 of a 16-lecture beginner DevOps course.

Do not teach Git, VPC, Terraform, Docker, or Kubernetes today. Those are later lectures.

## What this lecture covers

- What DevOps is and why teams need it
- Software Development Life Cycle (SDLC)
- Continuous Integration vs Continuous Delivery vs Continuous Deployment
- Linux basics: who you are, files, logs, disk, processes

Cloud names appear only as a map: Linux on **AWS EC2**, **Azure Virtual Machines**, and **GCP Compute Engine**. No paid cloud account is required.

## The PowerPoint is written for students to read

`presentation/lec-01-devops-fundamentals.pptx` is a full lesson, not a set of labels. Each slide explains the idea in sentences, gives a definition or example, and says what to remember.

## Learning objectives

By the end of 75 minutes the learner can:

1. Explain DevOps in their own words without naming a tool.
2. Place a feature on the SDLC and on the DevOps loop.
3. Distinguish CI, Continuous Delivery, and Continuous Deployment.
4. Use a few Linux commands: who, where, list, read, search, copy, disk, processes.
5. Read a log file with `cat`, `head`, `tail`, and `grep`.
6. Answer entry-level interview questions on today’s topics honestly.

## Lab

```bash
cd lec-01/codebase
bash linux-basics.sh
```

## Folder structure

```text
lec-01/
├── README.md
├── presentation/lec-01-devops-fundamentals.pptx
├── codebase/
│   ├── README.md
│   └── linux-basics.sh
└── resources/
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
