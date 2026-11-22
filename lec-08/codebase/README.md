# Lecture 8 lab

1. Recreate the Lecture 7 cluster if you deleted it (same names). Follow `eks-lab-instructions.txt`.
2. Build `notes-api:l8` on the tiny EC2 and push to ECR while the cluster is Creating.
3. CloudShell: apply ConfigMap, Secret, Deployment, Service. Replace `IMAGE` with `$URI:l8`.
4. Browser: refresh until the Pod name changes. Add a note. Show notes more than once.
5. Change the ConfigMap title, `rollout restart`, then break and undo.
6. Delete the Service first, then the cluster. Fill `../assignment.md`.
