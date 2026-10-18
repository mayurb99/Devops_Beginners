# Lecture 2 interview questions

Speak in your own words. Do not claim you ran production GitHub if you only used this lab.

---

## Git and GitHub

### 1. What is Git? What is GitHub?

**Full answer:** Git is the version-control tool on your computer. It stores snapshots (commits) of files. GitHub is a website that hosts Git repositories so a team can share them, review pull requests, and protect `main`.

**Spoken:** “Git is local history. GitHub is the shared copy plus PRs and permissions. GitLab and Azure Repos do a similar job.”

**Trap:** “Git and GitHub are the same.” — No.

---

### 2. What is a commit?

**Spoken:** “A commit is a snapshot of the project with a message, an author, and a pointer to the previous commit. It is not a zip email. You can go back to it.”

---

### 3. What is staging (`git add`)?

**Spoken:** “Staging is the waiting room. `git add` chooses which changes go into the *next* commit. I do not always `git add .` — I look at `git status` first so a secret or a junk file does not go in.”

---

### 4. Branch vs merge vs pull request?

**Spoken:** “A branch is a line of work. Merge brings that line into another branch. A pull request is a GitHub request: please review my branch and then merge it into `main`. I do not push straight to `main` on a team.”

---

### 5. clone vs pull vs fetch vs push?

**Spoken:** “Clone copies the repo the first time. Fetch downloads new commits. Pull is fetch plus merge. Push uploads my commits to GitHub.”

---

### 6. Fork vs clone?

**Spoken:** “Clone copies a repo I can already push to, or a local copy to work in. A fork is a copy *under my GitHub account* of someone else’s repo, so I can open a PR back to them.”

---

### 7. What should never be committed?

**Spoken:** “Passwords, API keys, cloud keys, private SSH keys, `.env`. I use `.gitignore` and I commit `.env.example` with fake values. If I commit a secret, I rotate the key — deleting the file in a later commit is not enough, because history still has it.”

---

### 8. Why protect `main`?

**Spoken:** “So nobody force-pushes or merges without a review. Production should come from `main`. Broken experiments stay on branches.”

---

### 9. How do you undo a local edit you have not committed?

**Spoken:** “`git restore filename` throws away uncommitted changes to that file. I do not rewrite history that other people already pulled.”

---

### 10. What does a merge conflict mean?

**Spoken:** “Two branches changed the same lines. Git will not guess. I open the file, keep the right text, `git add`, and commit.”

---

## Bonus — ways of working

### 11. Waterfall vs Agile?

**Spoken:** “Waterfall is long phases and one late release. Agile is short cycles and frequent working software. Waterfall fits a fixed legal scope. Agile fits learning as you build.”

---

### 12. Scrum vs Kanban?

**Spoken:** “Scrum uses time-boxed sprints and a sprint goal. Kanban uses a board and limits work in progress, with no required sprint length.”

---

### 13. Is Agile the same as DevOps?

**Spoken:** “No. Agile is how we plan and build in small slices. DevOps is how we test, release, run, and monitor. You can be Agile and still deploy by hand once a quarter.”

