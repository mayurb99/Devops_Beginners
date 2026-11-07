# Lecture 6 — spoken answers

**Left vs right in `-p 8080:8080`?**  
Left is the host (the EC2 today). Right is the port inside the container. You curl the left number on that host.

**Image tag vs `latest`?**  
A tag is a name you choose (`l6`). `latest` is just another tag people reuse. Pin a version so Fargate does not silently get a different image next month.

**Docker Hub vs ECR?**  
Hub is Docker’s website for images. ECR is AWS’s registry in your account and Region. Fargate in this account pulls from ECR.

**Azure / GCP names?**  
Registry: ACR / Artifact Registry. Run a container without managing a VM: Container Apps (ACI is older) / Cloud Run. Kubernetes: AKS / GKE — this course uses kind, not those.

**What is Fargate?**  
ECS runs your container. You do not pick an EC2 type or SSH in. You still need a VPC, subnet, security group, and an execution role so the task can pull ECR and write logs.

**Why public IP on the Fargate task?**  
Default public subnet + public IP lets the task reach ECR (and lets you curl it) without a NAT gateway. NAT is billed. We delete this stack the same day.

**Task definition vs service vs cluster?**  
Cluster = the ECS home. Task definition = the recipe (image, CPU, port). Service = keep N copies of that recipe running.

**Why CloudWatch logs?**  
There is no SSH into Fargate. Logs are how you see `API is running…` and crashes.

**Secrets in the image?**  
Never. `.pem`, Hub tokens, API keys stay out of `COPY` and out of Hub/ECR. `.dockerignore` helps.

**Non-root `USER`?**  
The process inside the container is not root. Port 8080 does not need root.

**Compose?**  
YAML for several containers. We skip it — one service, so `docker run` from lecture 5 is enough.

**Does this course’s project use Fargate?**  
No. Lecture 11 runs the container on one Free Tier EC2 with GitHub Actions. Today is the showcase so you have seen build → registry → run without SSH.
