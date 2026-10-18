# Lecture 2 command cheat sheet

Run in Git Bash, WSL, or Linux. GitHub steps need a browser.

## See Git

| Command | Purpose |
|---|---|
| `git --version` | Is Git installed? |
| `git status` | What changed? What is staged? |
| `git diff` | Unstaged changes in files |
| `git diff --staged` | What you are about to commit |
| `git log --oneline` | Short history |

## Save work

| Command | Purpose |
|---|---|
| `git clone URL` | Copy a GitHub repo to your laptop (already done for this course) |
| `git add file` | Put that file in staging |
| `git add .` | Stage everything — look at `status` first |
| `git commit -m "Clear message"` | Save a snapshot |
| `git restore file` | Throw away uncommitted edits to that file |

## Branches

| Command | Purpose |
|---|---|
| `git branch` | List branches |
| `git checkout -b my-feature` | Create and switch to a branch |
| `git checkout main` | Go back to main |
| Merge | Do this in the GitHub UI: Pull request → Merge |

## Talk to GitHub

| Command | Purpose |
|---|---|
| `git remote -v` | Show `origin` (the GitHub URL) |
| `git remote add origin URL` | Attach GitHub the first time |
| `git pull origin main` | Download and merge latest `main` |
| `git fetch` | Download, but do not merge yet |
| `git push -u origin my-feature` | Upload your branch |

## Do not commit

`.env`, passwords, API keys, `*.pem`, `.venv/`, `node_modules/`

Commit `.env.example` (fake values). Never commit `.env`.

## Pull request (browser)

1. Push your **branch** (not a secret).
2. GitHub → Compare & pull request.
3. Write what changed and why.
4. Request a review.
5. Merge into `main` after review.
6. Delete the feature branch.

## Not today

`rebase`, `push --force`, GitHub Actions, Docker, AWS.
