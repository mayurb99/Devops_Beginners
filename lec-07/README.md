# Lecture 7 — Kubernetes on EKS

Module 3: Kubernetes and Terraform.

**Read the deck first.** It starts from lecture 6 (why Fargate was enough for one task, and why you still learn Kubernetes). Then it explains the cluster, Pod, ReplicaSet, Deployment, Service, labels, ECR images, and EKS / AKS / GKE.

**Architecture (PNG, AWS + Kubernetes logos):** `resources/lecture-7-architecture.png` — the picture of what class built.

**What you build today:** a small VPC (two public subnets, no NAT), an ECR image `notes-api:l7` (HTML page at `/`), an EKS cluster in the console, one Deployment (`replicas: 1`), one Service `type: LoadBalancer`. You open the public hostname in your browser, add a note, show notes.

**Terminal:** CloudShell in the AWS console for `kubectl`. Git Bash only to SSH into the tiny build EC2 (Windows has no Docker Desktop).

**Cleanup is required.** EKS is billed while the cluster exists, even with zero Pods. Delete Service, node group, cluster, build EC2, and VPC before you leave.

Lecture 8 is replicas, ConfigMap, crash states, rollout. Lecture 11 is still one project EC2 + GitHub Actions, not EKS.

## Folder

```text
lec-07/
├── README.md
├── assignment.md
├── presentation/lec-07-kubernetes-eks.pptx
├── codebase/
│   ├── eks-lab-instructions.txt
│   ├── k8s/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── notes-api/
└── resources/
    ├── lecture-7-architecture.png
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
