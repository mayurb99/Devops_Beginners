# Lecture 3 interview questions

Speak in your own words. No lab is required.

---

## 1. What happens after you type a URL?

**Spoken:** “DNS turns the name into an IP. Then that computer, then a port, then HTTP. If it is HTTPS, the path is encrypted. I read the status code.”

---

## 2. What is DNS?

**Spoken:** “The phone book. example.com becomes a number. If DNS fails I never reach HTTP — that is not a 404.”

---

## 3. What is an IP? Public vs private?

**Spoken:** “An IP is the address of a computer. 127.0.0.1 is this laptop. A public IP can be reached from the internet. A private IP (10.x or 192.168.x) stays inside the home network or the VPC.”

---

## 4. What is a port?

**Spoken:** “A numbered door on an IP. 443 is HTTPS. 22 is SSH. 8080 was our class API. A security group decides which doors are allowed.”

---

## 5. Connection refused vs timeout vs 403?

**Spoken:** “Refused: the IP answered, nothing is listening on that port. Timeout: no answer, often a firewall. 403: HTTP worked, the server said you are not allowed.”

---

## 6. ping vs traceroute?

**Spoken:** “ping asks if an IP answers. Many clouds block ping, so a failed ping is not proof the app is down. traceroute lists stops on the path; stars mean that stop did not reply.”

---

## 7. What is a VPC? What is CIDR?

**Spoken:** “A virtual private cloud: my isolated network. Azure calls it a VNet. CIDR is how we write a block of IPs: 10.0.0.0/16 is the VPC, 10.0.1.0/24 is a subnet inside it.”

---

## 8. Public subnet vs private subnet?

**Spoken:** “Public vs private is the route, not the number. Public has a path to an Internet Gateway so a VM can have a public IP. Private has no direct internet; to call out it needs NAT, which is billed, so this course puts one micro in a public subnet and locks the security group.”

---

## 9. Internet Gateway vs NAT Gateway?

**Spoken:** “IGW is the door on the VPC for a public subnet. NAT lets a private subnet call out without being reachable in. NAT is billed, so we do not create it.”

---

## 10. Security group vs NACL vs WAF?

**Spoken:** “A security group is a firewall on the instance: IP and port. A NACL is a firewall on the subnet. A WAF reads the HTTP and blocks attacks like SQL injection. In class we design the security group.”

---

## 11. What is PrivateLink / a VPC endpoint?

**Spoken:** “A private path from my VPC to a cloud service, without the public internet.”

---

## 12. What are VPC flow logs?

**Spoken:** “A diary of accepted and rejected packets. I read them when SSH times out and I suspect a security group. We do not turn them on in class.”

---

## 13. How do two VPCs talk, or an office talk to the cloud?

**Spoken:** “Peering connects two VPCs privately. A VPN encrypts office or laptop traffic over the internet. Direct Connect, ExpressRoute, or Interconnect is private fibre — names only.”

---

## 14. Firewall vs reverse proxy vs load balancer?

**Spoken:** “A firewall allows or blocks a port. A reverse proxy sits in front and forwards. A load balancer spreads traffic across healthy servers.”
