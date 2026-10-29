# Lecture 4 interview questions

Speak in your own words. Do not claim production AWS if you only ran this lab.

---

## 1. What is a Region?

**Spoken:** “A geographic cluster of AWS data centres. I pick one and stay there so I do not pay for extra copies of resources.”

---

## 2. Why a billing alarm first?

**Spoken:** “So I know before the bill surprises me. I create a budget, then I launch the instance, then I stop it.”

---

## 3. IAM user vs role vs policy?

**Spoken:** “A user is a person or a long-lived login. A role is credentials a service or person assumes temporarily. A policy is the JSON that says allow or deny actions. Least privilege means the policy is only as wide as the job.”

---

## 4. What is a VPC?

**Spoken:** “My private network in AWS. Subnets live inside it. An Internet Gateway lets a public subnet reach the internet.”

---

## 5. Why no NAT Gateway in this course?

**Spoken:** “NAT lets private subnets reach the internet and it is billed by the hour plus data. For Free Tier we use one public subnet and lock the security group.”

---

## 6. Security group vs NACLs?

**Spoken:** “I talk about security groups: stateful allow rules on the instance. NACLs are subnet-level and exist, but I do not design with them in this class.”

---

## 7. Stop vs terminate?

**Spoken:** “Stop turns the VM off; I can start it later; disk can still cost a little. Terminate deletes the VM.”

---

## 8. What is S3?

**Spoken:** “Object storage for files. Not a database. Buckets are private unless I deliberately open them. I never should for this course.”

---

## 9. EC2 vs Lambda vs Kubernetes in one line?

**Spoken:** “EC2 is a VM I manage. Lambda is a short function AWS runs. Kubernetes is a cluster scheduler. This course’s cloud deploy is one small EC2. Kubernetes we practise on a laptop.”

---

## 10. Same idea on Azure / GCP?

**Spoken:** “EC2 is a VM, S3 is object storage, VPC is the network, IAM is who can do what. Names change. The picture does not.”
