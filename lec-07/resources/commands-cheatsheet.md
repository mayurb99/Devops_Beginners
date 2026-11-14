# Lecture 7 cheat sheet

Console = VPC, IAM roles, ECR, EKS cluster, node group, cleanup.  
CloudShell = `kubectl`.  
Git Bash = SSH to the build EC2 only.

## Clock

VPC + IAM + ECR → Create cluster → build/push `:l7` while it cooks → node group → apply YAML → browser → delete cluster.

## kubectl (CloudShell)

```bash
aws eks update-kubeconfig --name lec07-eks --region $REGION
kubectl get nodes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get deploy,pods,svc
kubectl describe pod -l app=notes
kubectl logs -l app=notes --tail=20
kubectl delete pod -l app=notes
kubectl get pods -w
kubectl delete svc notes
kubectl delete deploy notes
```

## Docker push (build EC2)

```bash
sudo docker build -t notes-api:l7 .
aws ecr get-login-password --region $REGION | sudo docker login --username AWS --password-stdin $ACCOUNT.dkr.ecr.$REGION.amazonaws.com
sudo docker tag notes-api:l7 $URI:l7
sudo docker push $URI:l7
```

## Service URL

`http://EXTERNAL-IP/`  — http, no `:8080`. Port 80 on the Service, 8080 inside the container.

## Azure / GCP names

EKS = AKS = GKE. Same YAML. You only click EKS today.

## Cleanup order

Service → Deployment → node group → cluster → build EC2 → VPC → IAM roles.
