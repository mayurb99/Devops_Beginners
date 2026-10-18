# Lecture 2 — Git and GitHub

75-minute teaching pack. Module 1: Foundations.

**Curriculum:** version control, Git vs GitHub, commits, branches, clone/push/pull, pull requests, protecting `main`, never commit secrets.

**Bonus in the same PowerPoint:** Waterfall, Agile, Scrum, Kanban, Agile vs DevOps.

Do not teach GitHub Actions, Docker, or AWS today.

## The PowerPoint is written for students to read

`presentation/lec-02-git-github.pptx` explains Git on the slides. The bonus section covers process models with diagrams.

## Learning objectives

1. Explain Git vs GitHub without mixing the two.
2. Use working tree → staging → commit.
3. Read `git status`, `git diff`, and `git log`.
4. Create a branch, push it, and open a pull request in the GitHub UI.
5. Name what must never be committed.
6. Tell Waterfall from Agile, and Agile from DevOps.

## Lab

Do this **in the course repo** (already on GitHub). Do not create a new repo.

Follow `codebase/git-demo-instructions.txt` line by line.

Merge is a **pull request in the GitHub website**, not `git merge` in the terminal.

## Folder structure

```text
lec-02/
├── README.md
├── presentation/lec-02-git-github.pptx
├── codebase/
│   ├── git-demo-instructions.txt
│   └── notes-api/
└── resources/
    ├── commands-cheatsheet.md
    └── interview-questions.md
```
