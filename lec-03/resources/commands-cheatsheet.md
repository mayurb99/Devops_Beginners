# Lecture 3 cheat sheet

There is no required lab. These are names and examples from the PowerPoint.

## Path of a URL

DNS (name → IP) → that computer → a port (door) → HTTP.

If the URL is `https://`, the path is encrypted. Same HTTP as lecture 2.

404 means HTTP started. “Could not resolve host” means DNS failed. Connection refused means the port is closed.

## Words you need

| Word | Meaning | Example |
|---|---|---|
| DNS | Name → IP | example.com → 93.184.216.34 |
| IP | Address of a computer | `127.0.0.1` is this laptop |
| Private IP | Only inside the network / VPC | `10.0.1.25`, `192.168.1.10` |
| Public IP | Reachable from the internet | EC2 public IPv4 in lecture 4 |
| Port | Door on that IP | 22 SSH, 80 HTTP, 443 HTTPS, 8080 class API |
| `0.0.0.0/0` | The whole internet | Never open SSH to it |

## Failure names

| What you see | HTTP started? |
|---|---|
| Could not resolve host | No — DNS |
| Connection refused | No — nothing on that port |
| Timed out | No — drop / dead / blocked |
| 401 / 403 / 404 / 5xx | Yes |

ping = “does this IP answer?” (often blocked in cloud). traceroute / `tracert` = which stop went quiet.

## Cloud network (same picture, different names)

CIDR examples: VPC `10.0.0.0/16` (the house), subnet `10.0.1.0/24` (one room). Public vs private is the **route**, not the number.

| Idea | AWS | Azure | GCP |
|---|---|---|---|
| Isolated network | VPC | VNet | VPC |
| Slice | Subnet | Subnet | Subnet |
| Door in | Internet Gateway | Internet | Internet gateway |
| Private outbound | NAT Gateway (billed) | NAT Gateway | Cloud NAT |
| Firewall on VM | Security group | NSG | VPC firewall |
| Firewall on subnet | NACL | NACL-like | Firewall policies |
| Sticky public IP | Elastic IP | Public IP | External IP |
| Cloud DNS | Route 53 | Azure DNS | Cloud DNS |
| Load balancer | ALB / NLB | LB / App Gateway | Cloud Load Balancing |
| Private path to a service | VPC endpoint / PrivateLink | Private Endpoint | Private Service Connect |
| Packet diary | VPC Flow Logs | NSG flow logs | VPC Flow Logs |
| HTTP-layer firewall | AWS WAF | Azure WAF | Cloud Armor |

Public subnet = route to Internet Gateway. Private subnet = needs NAT to call out. **We do not create NAT.**

AWS: one subnet lives in one Availability Zone.

Security group is the firewall on the VM (this course). NACL is on the subnet (name only). WAF reads HTTP; security group only sees IP and port.

## Optional commands (home only)

```bash
curl -v http://127.0.0.1:8080/health
curl -v --max-time 15 https://example.com
ping 8.8.8.8
tracert example.com
```
