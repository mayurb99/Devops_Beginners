# Lecture 7 assignment

Follow `codebase/eks-lab-instructions.txt`. Cleanup is part of the grade.

---

## 1. After Fargate

In your own words: what did lecture 6 Fargate already do well?  
What problem does Kubernetes add that one Fargate task does not solve?

---

## 2. Four objects

One sentence each: Pod, ReplicaSet, Deployment, Service.  
Which file did you `kubectl apply` first? Which object created the ReplicaSet for you?

---

## 3. Labels

The Service does not use the Pod IP. What field on the Service must match a label on the Pod?

---

## 4. Image

Paste your ECR URI including `:l7`.  
Why did the node role need `AmazonEC2ContainerRegistryReadOnly`?

---

## 5. LoadBalancer

What did `kubectl get svc notes` show in EXTERNAL-IP while it was waiting?  
What did you type in the browser (http or https, with or without `:8080`)?

---

## 6. HTML page

What happened when you clicked Add note, then Show notes?  
Where was that new note stored?

---

## 7. Delete one Pod

You ran `kubectl delete pod -l app=notes`. Did a new Pod appear?  
Was your extra note still on the page? Why or why not?

---

## 8. Names and later

What is the Azure name for EKS? The GCP name?  
Where does this course’s **project** run in lecture 11 — EKS or one EC2?

---

## Cleanup (tick)

- [ ] `kubectl delete svc notes` (load balancer gone)
- [ ] Deployment deleted
- [ ] Node group deleted
- [ ] Cluster `lec07-eks` deleted
- [ ] Build instance `lec07-build` terminated
- [ ] VPC `notes-k8s` deleted
- [ ] IAM roles `lec07-eks-cluster-role`, `lec07-eks-node-role`, `lec07-ec2-ecr` deleted (or noted)
