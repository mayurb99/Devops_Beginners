# Lecture 2 interview questions

Speak in your own words. Do not claim you built production APIs if you only called notes-api on a laptop.

---

## 1. What is an API?

**Full answer:** An API (Application Programming Interface) is a contract: you send a request in an agreed shape, and the other program sends a response. In this course we mean a REST API over HTTP.

**Spoken:** “An API is how one program asks another program to do something, using a documented URL, method, and JSON body, then reading the status code and body that come back.”

**Example:** `GET /health` on notes-api returns `{"status":"ok"}`.

---

## 2. What is REST?

**Full answer:** REST is a style for HTTP APIs. You use URLs for resources (`/notes`) and HTTP methods for actions (GET to read, POST to create). You do not need to recite Roy Fielding.

**Spoken:** “REST APIs expose resources as URLs and use GET, POST, PUT, PATCH, DELETE instead of inventing custom verbs for every action.”

---

## 3. HTTP vs HTTPS?

**Spoken:** “HTTP is the protocol. HTTPS is HTTP inside TLS, so the path is encrypted. Browsers and AWS APIs use HTTPS. Our class API is HTTP on localhost because it never leaves the laptop.”

**Trap:** “HTTPS is a different language than HTTP.” No. Same messages, encrypted transport.

---

## 4. What is in an HTTP request?

**Spoken:** “Method, URL, headers, and sometimes a body. Example: POST /notes with Content-Type application/json and a JSON body.”

---

## 5. What is in an HTTP response?

**Spoken:** “A status code, headers, and usually a body. I always read the status before I trust the body.”

---

## 6. GET vs POST vs PUT vs PATCH vs DELETE?

**Spoken:** “GET reads and should not change data. POST creates. PUT replaces the whole resource. PATCH changes part of it. DELETE removes it.”

**Ops angle:** A load balancer health check is almost always GET. A deploy webhook is often POST.

---

## 7. 200 vs 201 vs 400 vs 401 vs 403 vs 404?

**Spoken:** “200 is OK. 201 is created. 400 means my request was malformed. 401 means I did not authenticate. 403 means I authenticated but I am not allowed. 404 means that URL is not there.”

**Trap:** Mixing 401 and 403. Missing API key is 401. Valid user, wrong role is 403.

---

## 8. 500 vs 502 vs 503?

**Spoken:** “500 is the server itself crashed. 502 is a proxy in front got a bad answer from behind it. 503 means the service is up but cannot take work — overloaded or draining.”

---

## 9. What is JSON?

**Spoken:** “JavaScript Object Notation. Text with keys and values, curly braces for objects, square brackets for lists. APIs use it because every language can parse it.”

---

## 10. What is an API key? What is a bearer token?

**Spoken:** “An API key is a secret string I send in a header, like X-API-Key. A bearer token is usually a short-lived token in the Authorization header: Bearer …. Both prove who I am. I never commit them to Git.”

---

## 11. Why does a DevOps engineer care about APIs?

**Spoken:** “Everything we automate is an API: AWS CLI, Terraform, kubectl, GitHub Actions. If I cannot read a 403 JSON error, I cannot debug a pipeline.”

---

## 12. How do you call an API from the terminal?

**Spoken:** “curl. I use -i to see the status, -H for headers, -d for a body, -X for the method.”

---

## 13. The health check passed but users still fail. What might be true?

**Spoken:** “/health only proves the process can answer. It may not prove the database, IAM, or a downstream API. I still read application logs and a real user request.”
