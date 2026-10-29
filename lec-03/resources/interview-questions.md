# Lecture 3 interview questions

Speak in your own words.

---

## 1. What happens after you type a URL?

**Spoken:** “DNS turns the name into an IP. TCP connects to a port. If it is HTTPS, TLS encrypts. Then HTTP: method, path, headers, body. I read the status code.”

---

## 2. What is DNS?

**Spoken:** “Domain Name System. It maps example.com to an IP address so humans do not memorise numbers.”

---

## 3. What is a port?

**Spoken:** “A numbered door on an IP. 443 is HTTPS. 22 is SSH. 8080 is our class API. Two programs on one machine use different ports.”

---

## 4. Connection refused vs timeout vs 403?

**Spoken:** “Refused: the IP answered, nothing is listening on that port. Timeout: no answer, often a firewall drop. 403: HTTP worked, the server said you are not allowed.”

---

## 5. Public IP vs private IP?

**Spoken:** “A public IP can be reached from the internet. A private IP is only inside a VPC or a home network. 127.0.0.1 is this laptop.”

---

## 6. What is a security group?

**Spoken:** “AWS’s firewall on a resource. It allows or denies ports. If SSH is closed, I get timeout or refuse, not an SSH prompt.”

---

## 7. Load balancer vs reverse proxy vs firewall?

**Spoken:** “A load balancer spreads traffic across servers. A reverse proxy sits in front and forwards. A firewall allows or blocks. They can be separate products or one box doing more than one job.”

---

## 8. Why does this course use a public subnet?

**Spoken:** “A private subnet needs a NAT Gateway to reach the internet. NAT is billed. For Free Tier we put one micro EC2 in a public subnet with a public IP, and lock the security group.”

---

## 9. HTTP vs HTTPS again?

**Spoken:** “Same HTTP messages. HTTPS wraps them in TLS so the path is encrypted. Port 443.”
