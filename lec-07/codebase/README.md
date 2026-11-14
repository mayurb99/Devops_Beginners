# Lecture 7 lab

1. Follow `eks-lab-instructions.txt` from the start (VPC, then IAM, then ECR, then EKS).
2. Build `notes-api:l7` on the tiny EC2 and push to ECR while the cluster is Creating.
3. CloudShell: `kubectl apply` the files in `k8s/` after you replace `IMAGE`.
4. Open `http://EXTERNAL-IP/` — Add note and Show notes.
5. Delete the Service first, then the cluster. Fill `../assignment.md`.
