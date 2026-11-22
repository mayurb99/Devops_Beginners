# Lecture 8 cheat sheet

Console = recreate cluster if gone (same names as lecture 7).  
CloudShell = `kubectl`.  
Git Bash = SSH to the build EC2 only.

## Clock

Cluster first → build/push `:l8` while it cooks → apply four YAML files → two lists in the browser → ConfigMap restart → break + undo → delete cluster.

## kubectl (CloudShell)

```bash
aws eks update-kubeconfig --name lec07-eks --region $REGION
kubectl apply -f configmap.yaml -f secret.yaml -f deployment.yaml -f service.yaml
kubectl get deploy,pods,svc
kubectl describe pod -l app=notes
kubectl logs -l app=notes --tail=20
kubectl edit configmap notes-config
kubectl rollout restart deploy notes
kubectl rollout status deploy notes
kubectl set image deploy/notes notes=$URI:no-such-tag
kubectl set env deploy/notes CRASH=1
kubectl set env deploy/notes CRASH-
kubectl rollout undo deploy/notes
kubectl patch deploy notes --type json -p '[{"op":"replace","path":"/spec/template/spec/containers/0/livenessProbe/httpGet/path","value":"/nope"}]'
kubectl auth can-i get pods --as=system:serviceaccount:default:notes-reader
helm upgrade --install notes ./helm/notes-api --set image=$URI:l8
kubectl delete svc notes
```

## Docker push (build EC2)

```bash
sudo docker build -t notes-api:l8 .
aws ecr get-login-password --region $REGION | sudo docker login --username AWS --password-stdin $ACCOUNT.dkr.ecr.$REGION.amazonaws.com
sudo docker tag notes-api:l8 $URI:l8
sudo docker push $URI:l8
```

## Service URL

`http://EXTERNAL-IP/`  — http, no `:8080`. Click Show several times. Watch the Pod name.

## Azure / GCP names

EKS = AKS = GKE. Same YAML. You only click EKS today.

## Cleanup order

Service → Deployment / ConfigMap / Secret → node group → cluster → build EC2 → VPC.
