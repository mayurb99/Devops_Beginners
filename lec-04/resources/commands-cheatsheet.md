# Lecture 4 cheat sheet

No CLI is required. These are names from the PowerPoint and the lab.

## Create today (AWS)

| Thing | Lab section | Remember |
|---|---|---|
| Budget | A | Before NAT and ALB |
| VPC `10.0.0.0/16` | C | One Region |
| Public / private subnet | C | Public = route to IGW |
| NACL | D | We keep allow-all |
| `sg-hello` / `sg-private` / `sg-alb` | E | SSH = My IP only |
| hello-a, hello-b | F–H | User data is the hello page |
| Elastic IP | I | Release in cleanup |
| private-nat-test | J | No public IP |
| NAT Gateway | K | Public subnet; delete same day |
| ALB + target group | L | http:// DNS name; delete same day |
| S3 bucket | M | Block public access ON |
| Lambda + S3 trigger | N | Deploy, then upload, then logs |

## Use cases

| You do | You should see |
|---|---|
| Connect before SSH rule | Fail |
| Add 22 from My IP | Shell works |
| Stop/start without EIP | Public IP changes |
| Stop/start with EIP | Public IP stays |
| curl from private VM before NAT | Timeout |
| curl after NAT + route | HTTP 200 |
| Refresh ALB URL | APP-A and APP-B |
| Stop hello-b | Only APP-A |
| Upload to S3 | Lambda log has the file name |

## Three clouds — names (Different in italics)

| Idea | AWS | Azure | GCP |
|---|---|---|---|
| Network | VPC, *subnet = one AZ* | VNet, *subnet can span AZs* | *VPC can be global*, subnet regional |
| VM | EC2 | Virtual Machine | Compute Engine |
| Function | Lambda | Functions | Cloud Functions (*Cloud Run* is common too) |
| Object files | S3 | Blob Storage | Cloud Storage |
| Disk on one VM | EBS | Managed Disk | Persistent Disk |
| Shared files | EFS | Azure Files | Filestore |
| Managed SQL | RDS | Azure SQL | Cloud SQL |
| VM firewall | Security group | NSG (*NIC or subnet*) | VPC firewall (*on the VPC*) |
| HTTP LB | ALB | Application Gateway | Cloud Load Balancing |
| Sticky IP | Elastic IP | Public IP | Reserved External IP |
| Identity | IAM user/role | *Entra ID* + RBAC | *Google account* + service account |

## Later lectures

Fargate / ECS → Docker lectures. EKS → Kubernetes lectures (class uses **kind**, not EKS).

## Cleanup order

ALB → NAT → release Elastic IPs → terminate/stop EC2 → Connect endpoint → Lambda → empty S3.
