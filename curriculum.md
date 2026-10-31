# DEVOPS COURSE CURRICULUM

Beginner-Friendly Learning Plan

**Duration:** 16 lectures × 75 minutes  
**Cloud platform:** Amazon Web Services (AWS) — Free Tier  
**CI/CD:** GitHub Actions (not Jenkins)  
**Continuous example:** notes-api application

## Course Structure

- **Module 1: Foundations — Lectures 1–3**
- **Module 2: AWS and Containers — Lectures 4–6**
- **Module 3: Kubernetes and Terraform — Lectures 7–9**
- **Module 4: CI/CD and Production Operations — Lectures 10–13**
- **Module 5: Security, Cost and Integration — Lectures 14–15**
- **Module 6: Capstone Project — Lecture 16**

## Lecture 1: Introduction to DevOps and Linux
*Module 1: Foundations*

- What DevOps is and why it is needed.
- Software Development Life Cycle (SDLC).
- CI, Continuous Delivery and Continuous Deployment.
- Linux basics: files, directories, commands and permissions.
- Processes, services and application logs.
- Practical: run, stop and troubleshoot a simple service.

## Lecture 2: REST APIs
*Module 1: Foundations*

- HTTP and HTTPS.
- URL, methods, headers and request body.
- GET, POST, PUT, PATCH and DELETE.
- Status codes: 200, 201, 400, 401, 403, 404, 429, 500, 502 and 503.
- JSON payloads.
- API keys, bearer tokens and reading API documentation.
- curl, Postman and a simple AWS CLI call.
- Practical: call notes-api and read the response.

## Lecture 3: Networking
*Module 1: Foundations*

- Beginner path only (no OSI, TCP vs UDP, frames, or routers): DNS, IP (public vs private), port, HTTPS as encrypted HTTP, refused vs timeout vs 403, ping and traceroute.
- Cloud network (same picture on AWS, Azure, GCP): VPC/VNet, CIDR, subnet, route table, Internet Gateway, NAT Gateway (do not create), security group / NSG / VPC firewall, NACL, public vs Elastic IP, VPC endpoints / PrivateLink, flow logs, WAF, load balancer, cloud DNS.
- Region vs Availability Zone (a subnet lives in one AZ on AWS).
- Peering, VPN, Direct Connect / ExpressRoute / Interconnect — names only.
- Why this course uses a public subnet (NAT Gateway is billed).
- No required lab. Lecture 4 is the AWS clicks.

## Lecture 4: AWS Fundamentals
*Module 2: AWS and Containers*

- AWS account, Region and billing alarm.
- IAM users, roles, policies and least-privilege access.
- Click the Lecture 3 picture: VPC, public subnet, Internet Gateway and security group. No NAT Gateway.
- Amazon EC2: one t3.micro or t2.micro instance. Stop vs terminate.
- Amazon S3 as object storage.
- Azure and GCP: same ideas, different names.
- Practical: create a billing alarm, launch one micro instance, then stop it.

## Lecture 5: Docker
*Module 2: AWS and Containers*

- Why containers are needed.
- Images vs containers.
- Dockerfile and image layers.
- docker build, run, ps, logs, exec, stop and rm.
- Ports, environment variables, volumes and .dockerignore.
- Practical: containerize notes-api and call /health.

## Lecture 6: Docker Compose and Amazon ECR
*Module 2: AWS and Containers*

- Docker Compose for local run.
- Multi-stage builds, image size and non-root user.
- Secrets must not be stored in the image.
- Amazon Elastic Container Registry (ECR).
- Image tags and versioning; why not to rely on latest.
- Practical: push a small notes-api image to ECR.

## Lecture 7: Kubernetes
*Module 3: Kubernetes and Terraform*

- Why Kubernetes exists and where it is used.
- Cluster architecture: control plane, node and kubelet.
- Pods, ReplicaSets, Deployments and Services.
- kubectl apply, get, describe, logs and delete.
- Local cluster with kind. No EKS in this course (EKS is billed even when idle).
- Practical: deploy notes-api on kind and curl the Service.

## Lecture 8: Kubernetes Administration
*Module 3: Kubernetes and Terraform*

- ConfigMaps and Secrets.
- Requests, limits, liveness and readiness probes.
- Rolling updates and rollout undo.
- Pending, CrashLoopBackOff and ImagePullBackOff.
- Helm for notes-api.
- Basic RBAC.
- Practical: break a Pod, debug it, then roll back.

## Lecture 9: Terraform
*Module 3: Kubernetes and Terraform*

- Infrastructure as Code (IaC).
- Providers, resources, variables, outputs and data sources.
- State, remote backend on S3 and state locking.
- Modules and infrastructure drift.
- Declare VPC, security group and one EC2 instance. No NAT, no RDS, no EKS.
- terraform init, validate, plan, apply and destroy.
- Practical: apply the tiny stack, then destroy it before leaving class.

## Lecture 10: Continuous Integration with GitHub Actions
*Module 4: CI/CD and Production Operations*

- What a CI/CD pipeline is.
- Workflows, jobs, steps, runners and triggers.
- Introduction to YAML.
- Running tests on push and pull request.
- Build a Docker image, scan it and push it to Amazon ECR.
- Pipeline secrets. OIDC is how teams avoid long-lived keys; class may use a short-lived key.
- Practical: automate testing and image building. Read a failed job.

## Lecture 11: Continuous Deployment with GitHub Actions
*Module 4: CI/CD and Production Operations*

- Deploy job after a green CI run.
- Pull the image from ECR and run it on the one EC2 instance.
- Health checks.
- Rollback to the previous image tag.
- No Jenkins, no ECS Fargate and no Application Load Balancer in this course.
- Practical: deploy notes-api to the micro instance and roll back a bad tag.

## Lecture 12: Monitoring and Logging
*Module 4: CI/CD and Production Operations*

- Why monitoring is important.
- Health endpoint vs process is running.
- docker logs and application logs on the instance.
- Introduction to Amazon CloudWatch, with short log retention.
- kubectl logs and events on kind.
- Basic metrics and alarms.
- Practical: break the app and find the failure in the logs.

## Lecture 13: Troubleshooting
*Module 4: CI/CD and Production Operations*

- Debug order: is it running, port, IAM, image, logs, disk, DNS.
- Security group closed.
- Instance stopped.
- Wrong pipeline secret (403).
- CrashLoopBackOff on kind.
- Bad image tag.
- Practical: break the app on purpose and restore service.

## Lecture 14: Security and Cost Management
*Module 5: Security, Cost and Integration*

- Least-privilege IAM for this pipeline.
- Stop vs terminate vs terraform destroy.
- Why this course does not use EKS, NAT Gateway, ALB or RDS.
- AWS Budgets and common cloud cost traps.
- Packer and Ansible: names only, not a lab.
- Practical: review Free Tier usage and tighten one IAM permission.

## Lecture 15: Integration
*Module 5: Security, Cost and Integration*

- Full path once, with no new tools.
- Terraform apply of the tiny stack.
- GitHub Actions CI and CD.
- curl the application on EC2.
- Helm on kind.
- One failure and one rollback.
- Practical: rehearsal of the capstone checklist.

## Lecture 16: End-to-End DevOps Project: notes-api
*Module 6: Capstone Project*

- Objective: demonstrate the complete application delivery lifecycle using only concepts already covered.
- Run GitHub Actions tests, build the Docker image and store it in Amazon ECR.
- Deploy the container to the Free Tier EC2 instance.
- Run the same application on kind with Helm.
- Use logs to inspect health and errors.
- Simulate a failed deployment and roll back to the previous version.
- terraform destroy and confirm the instance is gone.
- Expected outcome: demonstrate the working application and explain how code reaches the server, how infrastructure is managed, and how failures are diagnosed.
