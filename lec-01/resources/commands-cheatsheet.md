# Lecture 1 command cheat sheet

Run in **Git Bash, WSL, or Linux**.

```bash
cd lec-01/codebase
bash linux-basics.sh
```

## Who / where

| Command | Purpose |
|---|---|
| `whoami` | Your username |
| `id` | Your user id |
| `pwd` | Which folder you are in |
| `ls -lah` | List files |
| `hostname` | This computer’s name |
| `uname` | What kind of system this is |
| `date` | Date and time |

## Files

| Command | Purpose |
|---|---|
| `mkdir devops-linux-demo` | Make a folder |
| `cd devops-linux-demo` | Go into the folder |
| `echo text > app.log` | Create / replace a file |
| `echo text >> app.log` | Add a line at the end |
| `cat app.log` | Show the whole file |
| `head -n 2 app.log` | First 2 lines |
| `tail -n 2 app.log` | Last 2 lines |
| `grep ERROR app.log` | Lines that contain ERROR |
| `wc -l app.log` | Count lines |
| `cp app.log app-copy.log` | Copy |
| `mv app-copy.log other.log` | Rename / move |
| `rm -rf devops-linux-demo` | Delete the practice folder |

## Machine

| Command | Purpose |
|---|---|
| `df -h` | Disk space |
| `ps aux \| head` | Running programs (short list) |

`>` replaces a file. `>>` adds to it. DevOps people use that all day on log files.

