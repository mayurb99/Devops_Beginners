# Lecture 3 command cheat sheet

## See the path of a request

```bash
curl -v http://127.0.0.1:8080/health
curl -v --max-time 15 https://example.com
```

`-v` = verbose. Read DNS, connect, TLS, then HTTP.

## Failure demos

```bash
curl -v --max-time 5 http://127.0.0.1:9          # refused
curl -v --max-time 5 http://192.0.2.1:80         # timeout
curl -i --max-time 15 https://httpbin.org/status/403   # HTTP 403
```

## Optional DNS lookup

```bash
nslookup example.com
```

## Cloud network (same picture, different names)

| Idea | Meaning | AWS | Azure | GCP |
|---|---|---|---|---|
| Your private cloud network | Isolated IP space | VPC | Virtual Network (VNet) | VPC |
| Slice of that network | Where VMs live | Subnet | Subnet | Subnet |
| Address block | Size of the network | CIDR e.g. 10.0.0.0/16 | CIDR | CIDR |
| Who can leave to the internet | Route to a gateway | Route table | Route table | Routes |
| Door to the internet | Public subnet path | Internet Gateway | Internet | Internet gateway / default internet |
| Private subnet → internet | Outbound only | NAT Gateway (billed) | NAT Gateway | Cloud NAT |
| Firewall on the VM | Allow/deny ports | Security group | NSG | VPC firewall |
| Firewall on the subnet | Extra layer | NACL | NACL-like / Azure Firewall | Firewall policies |
| Sticky public IP | IP that does not change | Elastic IP | Public IP | External IP |
| One door, many VMs | Spread traffic | ALB / NLB | Load Balancer / App Gateway | Cloud Load Balancing |
| DNS in the cloud | Name → IP | Route 53 | Azure DNS | Cloud DNS |
| Two networks talk | Private link between VPCs | VPC peering | VNet peering | VPC peering |
| Office → cloud | Encrypted over internet | Site-to-Site VPN | VPN Gateway | Cloud VPN |
| Private fibre | Not a lab | Direct Connect | ExpressRoute | Cloud Interconnect |
| Hub for many VPCs | Skip for beginners | Transit Gateway | Virtual WAN | Network Connectivity Center |

Public subnet = route to the Internet Gateway. VM can have a public IP.  
Private subnet = no direct internet. Needs NAT to call out. **We do not create NAT in this course.**

AWS: one subnet lives in one Availability Zone. Azure subnet is in the VNet. GCP VPC can be global; subnet is regional.

`0.0.0.0/0` means the whole internet. Never open SSH to it.

CIDR examples: VPC `10.0.0.0/16`, public subnet `10.0.1.0/24`, private subnet `10.0.2.0/24`.

## Names to remember

| Word | Meaning |
|---|---|
| DNS | Name → IP |
| IP | Address of a computer on a network |
| Port | Door on that computer (80 HTTP, 443 HTTPS, 8080 class API, 22 SSH) |
| TCP | Reliable connection to a port |
| TLS | Encryption around HTTP (HTTPS) |
| Public IP | Reachable from the internet |
| Private IP | Only inside the network (10.x, 172.16–31.x, 192.168.x, 127.0.0.1) |
| Security group | AWS firewall on an instance or ENI: allow/deny ports |
| Firewall | Same idea, not only AWS |
| Load balancer | One public door in front of many servers |
| Proxy | A hop in the middle (forward or reverse) |
| NAT Gateway | Lets private subnets reach the internet. **Costs money. We do not create it.** |
| CIDR | A block of IPs. `/16` is the VPC. `/24` is a subnet. |
| Route table | Next hop: local, Internet Gateway, or NAT |
| NACL | Stateless firewall on the subnet. Know the name. |
| Elastic IP | Sticky public IPv4. Do not leave a spare allocated. |
| Peering / VPN | Two networks, or office to cloud. Names only. |

## Failure table

| What you see | HTTP started? | Typical cause |
|---|---|---|
| Connection refused | No | Nothing listening on that port |
| Timed out | No | Dropped / filtered / dead IP |
| 403 | Yes | Authenticated or not, not allowed |
| 404 | Yes | Wrong path |
| 401 | Yes | Missing or wrong key (lecture 2) |

## Not today

Creating NAT, a load balancer, or EC2 (lecture 4). Docker, Kubernetes.
