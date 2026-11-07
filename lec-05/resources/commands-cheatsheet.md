# Lecture 5 cheat sheet

Console (CLI-0 to CLI-3) = key, SG, Launch instance.  
Windows Git Bash = `ssh` / `scp`.  
EC2 after SSH = `sudo docker` / `curl`.

## Console (CLI-0 to CLI-3)

1. Lock the Region (same as lecture 4).
2. EC2 → Key Pairs → Create `lec05-docker` (.pem). Move to `~/lec05-docker.pem`, `chmod 400`.
3. Security group `lec05-docker-ssh`: SSH 22 from **My IP**. Do not open 8080.
4. Launch instance: Amazon Linux 2023, t3.micro, that key, **Default VPC**, Auto-assign public IP **Enable**, that SG only.
5. Wait Running + Status check 2/2. Copy **Public IPv4**.

## Git Bash (after the instance is up)

```bash
chmod 400 ~/lec05-docker.pem
ssh -i ~/lec05-docker.pem -o StrictHostKeyChecking=accept-new ec2-user@$PUBLIC
scp -i ~/lec05-docker.pem -r notes-api ec2-user@$PUBLIC:~/
```

## Docker (on the EC2)

```bash
sudo dnf install -y docker
sudo systemctl enable --now docker
sudo docker version
cd ~/notes-api
sudo docker build -t notes-api:l5 .
sudo docker images
sudo docker run --rm -p 8080:8080 --name notes-l5 notes-api:l5
curl http://127.0.0.1:8080/health
sudo docker ps
sudo docker logs notes-l5
sudo docker exec -it notes-l5 hostname
sudo docker stop notes-l5
sudo docker start notes-l5
sudo docker rm -f notes-l5
sudo docker rmi notes-api:l5
```

| Flag | Meaning |
|---|---|
| `-t name:tag` | Name the image |
| `.` | Build context = this folder |
| `-p host:container` | Map a **host** (EC2) port to a container port |
| `--name` | Name this container |
| `--rm` | Delete the container when it stops |
| `-d` | Run in the background |
| `-e KEY=value` | Environment variable |
| `-v name:/path` | Named volume |

Left side of `-p` = this EC2. Right side = inside the container.  
You curl `127.0.0.1` **on the EC2**. Do not open 8080 on the security group.

## Cleanup (console)

Instances → `lec05-docker` → Terminate. Then delete security group `lec05-docker-ssh`.

## Words

| Word | Meaning |
|---|---|
| Image | The recipe result. Read-only. `notes-api:l5` |
| Container | A running (or stopped) copy of an image |
| Dockerfile | The recipe |
| Layer | One instruction in the Dockerfile, cached |
| Registry | Where images are stored (Docker Hub, ECR next lecture) |

## Three clouds (names — not today)

| Idea | AWS | Azure | GCP |
|---|---|---|---|
| Store the image | ECR | ACR | Artifact Registry |
| Run containers, little VM ops | ECS / Fargate | Container Apps / ACI | Cloud Run |

Fargate is named in lecture 6. EKS is lectures 7–8 (`kind`).
