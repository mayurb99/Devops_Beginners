# Lecture 4 command cheat sheet

Console first. CLI is optional.

## Stay in one Region

Example: `ap-south-1`

## Optional AWS CLI

```bash
aws sts get-caller-identity
aws ec2 describe-instances --output table
aws ec2 stop-instances --instance-ids i-xxxxxxxx
aws s3 ls
aws s3 mb s3://your-unique-bucket-name
```

Configure once (not in Git):

```bash
aws configure
```

## Free Tier box we use

| Create | Do not create |
|---|---|
| Billing budget / alarm | NAT Gateway |
| IAM user (not daily root) | Load balancer |
| Default VPC, public subnet, IGW | RDS |
| One t3.micro / t2.micro | EKS / extra EC2 |
| Security group, SSH from My IP | 0.0.0.0/0 on SSH |
| Private S3 bucket | Public bucket |

## Stop vs terminate

| Action | Instance | Disk | Public IP |
|---|---|---|---|
| Stop | Off, can start again | Kept (small charge) | Usually released |
| Terminate | Deleted | Deleted (unless you set keep) | Gone |

## Azure / GCP names

| Idea | AWS | Azure | GCP |
|---|---|---|---|
| Virtual machine | EC2 | Virtual Machine | Compute Engine |
| Network | VPC | Virtual Network | VPC |
| Object files | S3 | Blob Storage | Cloud Storage |
| Who can do what | IAM | Entra ID / RBAC | IAM |
| Firewall on the VM | Security group | Network Security Group | VPC firewall |

## Not today

Docker, Kubernetes, Terraform apply, GitHub Actions, opening port 8080.
