# Lecture 4 interview questions

Speak in your own words. Do not claim production AWS if you only ran this lab.

---

## 1. Why a budget before NAT and a load balancer?

**Spoken:** “Both are billed by the hour even if idle. The budget email is cheaper than a surprise.”

---

## 2. IAM user vs role vs policy?

**Spoken:** “A user is a person login. A role is temporary identity a service assumes. A policy says allow or deny. Azure uses Entra ID and RBAC. GCP uses Google accounts and service accounts — there is no IAM user copy of AWS.”

---

## 3. Why is an AWS subnet different from Azure and GCP?

**Spoken:** “In AWS one subnet lives in one Availability Zone. In Azure a subnet can span AZs. In GCP the VPC can be global and the subnet is regional.”

---

## 4. Security group vs NACL?

**Spoken:** “A security group is on the VM and remembers the conversation. A NACL is on the subnet and does not. I showed SSH fail with no port 22, then work after 22 from My IP.”

---

## 5. Ordinary public IP vs Elastic IP?

**Spoken:** “Stop and start: the ordinary public IP usually changes. An Elastic IP stays. If I allocate one and leave it unused, it can still be billed. Azure says Public IP. GCP says reserved External IP.”

---

## 6. What did NAT prove?

**Spoken:** “The private VM had no public IP and curl to example.com failed. After a NAT Gateway in the public subnet and a 0.0.0.0/0 route, curl worked. The internet still cannot SSH in — NAT is outbound only.”

---

## 7. Why must NAT sit in the public subnet?

**Spoken:** “NAT needs a path to the Internet Gateway. Private instances only point at NAT. They never get a public IP.”

---

## 8. What did the load balancer prove?

**Spoken:** “One URL, two hello apps on two EC2s. Refresh showed APP-A or APP-B. When I stopped B, only A answered — the target was unhealthy.”

---

## 9. S3 vs EBS vs EFS? What did you create?

**Spoken:** “S3 is a bucket of files. EBS is the disk on one VM. EFS is a shared file system. I created S3 only.”

---

## 10. What is Lambda with an S3 trigger?

**Spoken:** “A function. I uploaded a file; the log showed the bucket and key. There is no EC2 to stop. Azure Functions and GCP Cloud Functions are the same idea. GCP also pushes Cloud Run.”

---

## 11. Where are Fargate and EKS in this course?

**Spoken:** “Fargate in the Docker lectures. EKS is named in Kubernetes; this class uses kind so we do not pay for a control plane.”

---

## 12. RDS?

**Spoken:** “Managed SQL. Azure SQL, GCP Cloud SQL. We did not create it — easy to forget and pay. notes-api keeps notes in memory.”
