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

## Failure table

| What you see | HTTP started? | Typical cause |
|---|---|---|
| Connection refused | No | Nothing listening on that port |
| Timed out | No | Dropped / filtered / dead IP |
| 403 | Yes | Authenticated or not, not allowed |
| 404 | Yes | Wrong path |
| 401 | Yes | Missing or wrong key (lecture 2) |

## Not today

AWS console, VPC, EC2, Docker, Kubernetes.
