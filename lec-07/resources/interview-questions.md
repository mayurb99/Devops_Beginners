# Lecture 7 — answers you can say

**Why Kubernetes if you already used Fargate?**  
Fargate ran one notes-api task well. Kubernetes is the API for many copies, restarts, and a stable Service URL while Pod IPs change.

**Pod vs Deployment vs Service?**  
Pod = running container(s). Deployment = keep N Pods (it creates a ReplicaSet). Service = stable name/port in front of Pods selected by label.

**What is a ReplicaSet?**  
The object that actually keeps the Pod count. You apply a Deployment; the Deployment owns the ReplicaSet.

**How does a Service find Pods?**  
`selector: app: notes` must match the Pod template label `app: notes`. Not the Pod IP.

**What is EKS?**  
AWS runs the Kubernetes control plane. You still give it a VPC, subnets, a node group, and IAM roles. AKS / GKE are the Azure / GCP names.

**type: LoadBalancer?**  
Kubernetes asks the cloud for a public hostname. On AWS that is a load balancer you did not click Create for. Delete the Service to drop it.

**Where are notes stored?**  
In process RAM. No database. Delete the Pod and extra notes are gone. Two replicas (lecture 8) means two lists.

**Why pull from ECR?**  
The node is not your laptop. The Pod image field is an ECR URI `:l7`. The node role needs `AmazonEC2ContainerRegistryReadOnly`.

**Does the course project use EKS?**  
No. Lecture 11 is one EC2 + GitHub Actions. You delete this cluster today because the control plane is billed while it exists.
