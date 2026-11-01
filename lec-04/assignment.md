# Lecture 4 assignment

Follow `codebase/aws-lab-instructions.txt` in the AWS console (buttons only). Then answer below. A beginner who did the lab can finish this.

Due: before Lecture 5. If you created a NAT Gateway or load balancer, they must be **deleted** before you submit.

---

## 1. Region and money

1. Which Region did you use?  
2. Paste a screenshot of your **budget** (hide the account id if you want).  
3. Why do we create the budget **before** NAT and the load balancer?

---

## 2. Network picture

Draw (phone photo of paper is fine):

```text
Internet → ALB → hello-a and hello-b (public subnet)
Internet → IGW → VPC
Private subnet → (no internet) then → NAT → internet
```

Label: VPC CIDR, public CIDR, private CIDR, security groups.

---

## 3. Use cases — what did you see?

Write one or two sentences each. Screenshot if you have one.

| Use case | What did you do? | What happened? |
|---|---|---|
| SSH **without** port 22 on the security group | | |
| SSH **with** port 22 from **My IP** | | |
| Ordinary public IP: stop then start | | |
| Elastic IP: stop then start | | |
| Private VM **before** NAT: `curl https://example.com` | | |
| Private VM **after** NAT: same curl | | |
| ALB URL, refresh many times | | |
| Stop hello-b, refresh the ALB URL | | |
| Upload a file to S3, open Lambda logs | | |

---

## 4. Three clouds (theory — no Azure/GCP console)

Fill the names. Highlight in your own words if one cloud is **different**.

| Idea | AWS | Azure | GCP | What is different? |
|---|---|---|---|---|
| Private network | | | | |
| VM | | | | |
| Object files | | | | |
| Function (no server) | | | | |
| Firewall on the VM | | | | |
| Managed SQL database (we did **not** create this) | | | | |

---

## 5. Spoken answers (write them, then say them out loud)

1. Why can the internet not SSH to `private-nat-test` even after NAT works?  
2. Why must the NAT Gateway sit in the **public** subnet?  
3. What does the load balancer use to decide A vs B?  
4. Why do we delete NAT and the ALB the same day?  
5. S3 vs EBS vs EFS — one line each. Which one did we create?  
6. Where will this course show Fargate? Where will it show EKS?

---

## 6. Cleanup checklist (required)

Tick and date. Submission without this is incomplete.

- [ ] Application Load Balancer deleted  
- [ ] Target group deleted  
- [ ] NAT Gateway deleted  
- [ ] All Elastic IPs released  
- [ ] Three instances stopped or terminated  
- [ ] Instance Connect Endpoint deleted  
- [ ] Lambda deleted  
- [ ] S3 bucket emptied or deleted  
- [ ] Date: _____________

---

## How you are marked

- Lab use cases observed (section 3): most of the marks  
- Cleanup done: required  
- Three-cloud table and spoken answers: the rest  
- Screenshots help but are not the whole assignment  
