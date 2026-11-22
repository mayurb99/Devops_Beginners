# Lecture 8 — answers you can say

**Why replicas 2 if lecture 7 already ran the app?**  
To keep two copies. Each Pod has its own memory. One Service URL does not make one list.

**Why did my extra note vanish?**  
Add landed on Pod A. Show landed on Pod B. B never saw A’s Python list. There is still no database.

**ConfigMap vs image?**  
The image is the program. The ConfigMap is settings (today: the page title). Change the ConfigMap, restart the Pods, no new docker build.

**Secret vs ConfigMap?**  
Same idea: data injected as env. The app reads both and (in class) prints both. ConfigMap is the heading. Secret is a dummy token. Kubernetes stores the Secret as base64 — that is not encryption. A real app would not print a Secret on the page.

**ImagePullBackOff?**  
The node could not pull the image. Wrong tag, wrong Region, or the node role cannot read ECR.

**CrashLoopBackOff?**  
The container starts, then the process exits, then kubelet tries again. Read `kubectl logs`.

**Pending?**  
The Pod has not started yet. Today: the memory request did not fit the node. It is waiting, not crashing.

**rollout undo?**  
A Deployment keeps the previous ReplicaSet. Undo points traffic back at that one.

**Helm?**  
A packaging tool for the same YAML. Optional today. Not a second Kubernetes.

**Liveness vs readiness?**  
Liveness: kubelet restarts a container that will not answer /health. Readiness: keep the process, but take it out of the Service until it is ready.

**requests vs limits?**  
Request is how much seat the scheduler reserves. Too big → Pending. Limit is a cap. Over memory limit → kubelet kills the container.

**RBAC?**  
Who may do which kubectl verb. Lecture 7 access entry made me admin. A Role can allow get pods and deny delete. IAM is AWS. RBAC is the Kubernetes API.

**Helm?**  
A package of the same YAML. values.yaml is the IMAGE blank. helm install is one apply. Teams use it for notes-api and for tools (Prometheus, Ingress) so they do not copy 30 files from GitHub. Not a second cluster.

**Does the project use EKS?**  
No. Lecture 11 is one EC2 + GitHub Actions. This cluster is class-only. Delete it.
