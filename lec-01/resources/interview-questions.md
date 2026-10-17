# Lecture 1 interview questions

Use this file to revise. The slides show the short spoken answer. Here you get the full answer, a 20–30 second spoken version, a practical example, and follow-ups.

Speak in your own words. Do not claim you ran production AWS if you only ran this laptop lab.

---

## 1. What is DevOps?

**Full answer:** DevOps is a way of working where the people who build software and the people who run it share one delivery loop: plan, code, build, test, release, deploy, operate, and monitor. It is culture plus practice plus tools. It is not a job title by itself and not an AWS product.

**Spoken:** “DevOps means the team that writes the code is also responsible for shipping it and keeping it healthy. We shorten the path from commit to production, with automated checks, so we can release often without heroics.”

**Example:** A notes API is not ‘finished’ when a developer runs it on a laptop. It is finished when it is deployed, logged, and recoverable.

**Follow-up / trap:** “So DevOps is a tool?” — No. Jenkins or GitHub Actions support DevOps; they are not DevOps.

---

## 2. Why was DevOps needed?

**Full answer:** Historically developers threw code over a wall to operations. Releases were slow, environments differed, and failures turned into blame. Businesses needed smaller, safer, more frequent changes.

**Spoken:** “Developers optimised for new features, operations optimised for stability, and they met only on release night. DevOps removes that wall so change and stability are the same team’s problem.”

**Example:** A Friday night release that only one person knows how to roll back.

**Follow-up:** “Is DevOps only for startups?” — No. Banks use it too; they just add more controls.

---

## 3. What is the software development life cycle (SDLC)?

**Full answer:** SDLC is the path from idea to a running system and back: requirements, design, implementation, test, deploy, operate, and improve. DevOps does not replace SDLC; it makes the later stages continuous instead of a one-off project phase.

**Spoken:** “SDLC is the whole journey of a feature. DevOps is how we keep repeating the last parts of that journey safely.”

**Example:** “Add a /notes endpoint” goes through design, code, test, deploy, then monitors error rate.

---

## 4. What is the DevOps loop?

**Full answer:** plan → code → build → test → release → deploy → operate → monitor, then back to plan. If you stop at deploy, you are not operating.

**Spoken:** “I think of eight stages from plan to monitor. The point is that production signals feed the next plan.”

**Trap:** Listing only CI/CD tools instead of the loop.

---

## 5. CI vs Continuous Delivery vs Continuous Deployment

**Full answer:**

- **Continuous Integration (CI):** every commit is automatically built and tested.
- **Continuous Delivery:** every good build is *releasable*. A human usually clicks to produce.
- **Continuous Deployment:** every good build *goes* to production automatically.

**Spoken:** “CI is automated verification of every commit. Continuous Delivery means we *could* release any good build. Continuous Deployment means we actually do, without a manual gate.”

**Example:** GitHub Actions runs tests on a pull request (CI). Staging deploys automatically; production waits for approval (Delivery). A team that ships to prod on every green main is doing Deployment.

**Follow-up:** “Which one should we use?” — Start with CI plus Delivery. Full Deployment needs excellent tests and rollback.

---

## 6. Why do DevOps engineers care about Linux?

**Full answer:** Most servers, containers, and CI runners are Linux. Cloud VMs in AWS, Azure, and GCP are usually Linux images. If something fails at 2 a.m., you debug it with `ps`, `df`, and log files — not with a GUI.

**Spoken:** “Linux is the operating system under almost every service I will run. Cloud consoles don’t replace the ability to read a log and a process list.”

**Example:** Today’s lab: open `app.log` and `grep ERROR`.

**Trap:** “I only need Windows because I develop on Windows.” — You may *write* code on Windows. You will *run* it on Linux.

---

## 7. A service is down. What do you do first?

**Full answer:** Do not reinstall. Check: is the process running (`ps`), is the disk full (`df -h`), what do the logs say (`cat` / `grep`)? Ask what changed.

**Spoken:** “I check whether the process is alive, whether the disk is full, and I search the log for ERROR. I avoid random reboots.”

**Scenario:** Users report a payment failure. `grep ERROR app.log` shows the payment service could not be reached. That is evidence, not a guess.

**Follow-up:** “What if the disk is 100% full?” — Logs and databases cannot write; `df -h` is why we taught it today.

---

## 8. What is a process vs a service?

**Full answer:** A process is a running program with a PID. A service is a process you start and leave running so the app stays up.

**Spoken:** “A process is ‘this program is running now’. A service is ‘this program should keep running’.”

**Example:** Anything in `ps aux` is a process. A service is a process that should keep running.

---

## 9. You get `Permission denied`. What does that mean?

**Full answer:** The user running the process lacks the required `r`, `w`, or `x` bit on that file or directory. Directories need execute permission to enter. Fix the bits or the owner; do not chmod 777 as a habit.

**Spoken:** “The process is not allowed to read, write, or enter that path. I look at `ls -l`, then `chmod` or `chown` with the least privilege that works.”

**Trap:** “Just use sudo everywhere.” — That hides the real owner problem and is dangerous.

---

## 10. What is the difference between stdout and a log file?

**Full answer:** stdout is the stream you see in the terminal. A log file is the same events persisted on disk so you can read them after the terminal is gone. Production systems almost always persist logs (files or a log service).

**Spoken:** “If I only look at the terminal, I lose history when the session ends. The log file is the record I actually debug from.”

**Example:** `app.log` in today’s lab.

---

## 11. Scenario: it works on my laptop but not on the server

**Spoken path:** Compare the folder you are in (`pwd`), the files (`ls`), the log (`grep ERROR`), disk (`df -h`), and which programs are running (`ps`).

**Do not say:** “The server is broken” without evidence.

---

## 12. Is DevOps the same as AWS?

**Full answer:** No. AWS, Azure, and GCP are platforms where you *run* the loop. EC2, Azure Virtual Machines, and Compute Engine are just Linux computers you did not rack yourself. DevOps skills transfer; product names change.

**Spoken:** “DevOps is how we ship and run software. AWS is one place we host it. I can describe the idea without naming a product, then map it: EC2, Azure VM, or GCE for a Linux server.”

**Trap:** Reciting a list of AWS services for a Linux question.

---

## Extra practice (not on the slides)

- What does `df -h` tell you in an incident?
- What is the difference between `>` and `>>`?
- How do you find ERROR lines in a log?
- How would you explain CI to a hiring manager in one sentence?
