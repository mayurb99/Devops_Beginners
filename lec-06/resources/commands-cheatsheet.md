# Lecture 6 cheat sheet

Console = key, SG, IAM role, Launch instance, ECR, ECS/Fargate.  
Windows Git Bash = `ssh` / `scp` / `curl` to Fargate.  
EC2 after SSH = `sudo docker build` / `run` / `push` / `aws ecr login`.  
No Compose.

## Clock

Build on EC2 → Hub → ECR → Fargate curl from Windows → delete. About 75 minutes. No extra demos.

## Console (EC2)

1. Same Region as lectures 4–5. Write REGION and 12-digit ACCOUNT.
2. Key: reuse `lec05-docker.pem` or create `lec06-docker`.
3. SG `lec06-docker-ssh`: SSH 22 **My IP** only. Do not open 8080 here.
4. IAM role `lec06-ec2-ecr` (EC2 + `AmazonEC2ContainerRegistryPowerUser`).
5. Launch: Amazon Linux 2023, t3.micro, Default VPC, public IP **Enable**, that SG, IAM profile `lec06-ec2-ecr`.
6. Wait Running + 2/2. Copy Public IPv4.

## Git Bash → EC2

```bash
chmod 400 ~/lec06-docker.pem
ssh -i ~/lec06-docker.pem -o StrictHostKeyChecking=accept-new ec2-user@$PUBLIC
```

## Docker (on the EC2)

```bash
sudo dnf install -y docker git
sudo systemctl enable --now docker
sudo docker version
cd ~/notes-api
sudo docker build -t notes-api:l6 .
sudo docker run --rm -p 8080:8080 --name notes-l6 notes-api:l6
# other window:
curl http://127.0.0.1:8080/health
```

## Docker Hub

```bash
sudo docker login -u $HUB          # access token as password
sudo docker tag notes-api:l6 $HUB/notes-api:l6
sudo docker push $HUB/notes-api:l6
```

## ECR

Console: ECR → Create private repo `notes-api`. Copy URI.

```bash
aws sts get-caller-identity
aws ecr get-login-password --region $REGION | sudo docker login --username AWS --password-stdin $ACCOUNT.dkr.ecr.$REGION.amazonaws.com
sudo docker tag notes-api:l6 $URI:l6
sudo docker push $URI:l6
```

## Fargate (console)

1. ECS → Create cluster `lec06-cluster` (Fargate).
2. Task definition `notes-api`: 0.25 vCPU, 0.5 GB, execution role, image `$URI:l6`, port 8080, env `HOST=0.0.0.0` `PORT=8080`.
3. Service `notes-svc`: 1 task, Default VPC, **public IP ON**, new SG `lec06-fargate-8080` inbound **8080** `0.0.0.0/0`, no load balancer.
4. Task → Public IP. From **Windows**:

```bash
curl http://FARGATE_IP:8080/health
curl http://FARGATE_IP:8080/notes
```

Logs: task → Logs (CloudWatch). No SSH into Fargate.

## Azure / GCP names (no lab)

| Job | AWS (today) | Azure | GCP |
| --- | --- | --- | --- |
| Shelf | ECR | ACR | Artifact Registry |
| Run, little VM work | Fargate | Container Apps (ACI older) | Cloud Run |
| Kubernetes | EKS (we use kind) | AKS | GKE |

## Cleanup (order)

Service desired 0 → delete service → delete cluster → deregister task def → delete ECR repo → terminate EC2 → delete both SGs → delete log group → delete `lec06-ec2-ecr`.

## Do not

- Open 8080 on the EC2 SG.
- Use `:latest` on Fargate.
- Put Hub tokens in the Dockerfile.
- Leave Fargate or lecture 4 NAT running.
- Expect lecture 11 to use Fargate (project = one EC2 + GitHub Actions).
