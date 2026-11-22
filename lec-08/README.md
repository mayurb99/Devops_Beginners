# Lecture 8 — Kubernetes administration

Module 3: Kubernetes and Terraform.

**Read the deck first.** It starts from lecture 7 (`replicas: 1`, one list). Then it shows two Pods, ConfigMap, Secret, three unhappy states, and `rollout undo`.

**Architecture (PNG):** `resources/lecture-8-architecture.png` — the picture of what class builds today.

**What you build today:** the **same** EKS cluster names as lecture 7 (`lec07-eks` in VPC `notes-k8s`). Image `notes-api:l8`. Deployment `replicas: 2`. ConfigMap for the page title. Secret for a dummy token. The HTML page **prints both**. You open the public hostname, watch the Pod name flip, see a note vanish, then break a Pod and undo.

**Terminal:** CloudShell for `kubectl`. Git Bash only to SSH into the tiny build EC2 (Windows has no Docker Desktop).

**Cleanup is required.** EKS is billed while the cluster exists. Delete Service, node group, cluster, build EC2, and VPC before you leave.

Probes, requests/limits, and RBAC (`auth can-i`) have short CloudShell demos. Helm is optional if cleanup is at risk. Lecture 11 is still one project EC2 + GitHub Actions, not EKS.

## Folder

```text
lec-08/
├── README.md
├── assignment.md
├── presentation/lec-08-kubernetes-admin-v2.pptx
├── codebase/
│   ├── eks-lab-instructions.txt
│   ├── k8s/
│   │   ├── configmap.yaml
│   │   ├── secret.yaml
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── helm/notes-api/          (optional)
│   └── notes-api/
└── resources/
    ├── lecture-8-architecture.png
    ├── generate-architecture.py
    ├── generate-diagrams.py
    ├── today-path.png
    ├── two-lists.png
    ├── config-vs-image.png
    ├── secret-vs-config.png
    ├── crash-states.png
    ├── rollout.png
    ├── three-clouds.png
    ├── resources.png
    ├── probes.png
    ├── rbac.png
    ├── helm-vs-apply.png
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
