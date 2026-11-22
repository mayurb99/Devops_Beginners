# Lecture 8 assignment

Follow `codebase/eks-lab-instructions.txt`. Cleanup is part of the grade.

---

## 1. Two lists

You set `replicas: 2`. Why can Add note and Show notes disagree?  
What on the HTML page tells you which Pod answered?

---

## 2. ConfigMap

What heading did you put in `PAGE_TITLE`?  
Did you run `docker build` again to change it? What command made the Pods reread it?

---

## 3. ConfigMap and Secret on the page

What two ConfigMap values did the page print?  
What Secret value did it print?  
Why is the base64 blob in `kubectl get secret` not encryption?

---

## 4. ImagePullBackOff

Which tag did you set to break the pull?  
Which command put the good ReplicaSet back?

---

## 5. CrashLoopBackOff

What env var made the process exit?  
Which command showed you the log line?

---

## 6. Pending

What memory request made new Pods wait?  
Is Pending a crash, or a wait?

---

## 7. Requests vs limits

What happened when you asked for 8Gi? Was that a crash or a wait?  
In one sentence: what is a **limit** for?

---

## 8. Liveness vs readiness

After you pointed **liveness** at `/nope`, what number went up?  
After you pointed **readiness** at `/nope`, did `get pods` still say Running? Did the browser still work? Why?

---

## 9. RBAC

What did `auth can-i get pods` say for `notes-reader`?  
What did `auth can-i delete pods` say? You did not create a second AWS user — what identity did you use?

---

## 10. Helm (even if you skipped the optional install)

Helm is not a second Kubernetes. What problem does it solve that `kubectl apply -f` four times does not?  
If a team wants Prometheus on a cluster, why do they usually `helm install` a chart instead of writing 30 YAML files?

---

## 11. Later

What is the Azure name for EKS? The GCP name?  
Where does this course’s **project** run in lecture 11 — EKS or one EC2?

---

## Cleanup (tick)

- [ ] `kubectl delete svc notes` (load balancer gone)
- [ ] Deployment / ConfigMap / Secret deleted
- [ ] Node group deleted
- [ ] Cluster `lec07-eks` deleted
- [ ] Build instance `lec08-build` terminated
- [ ] VPC `notes-k8s` deleted (or noted why Delete is grey)
