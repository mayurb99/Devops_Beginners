#!/usr/bin/env bash
# Beginner Linux commands for DevOps students.
# Run with: bash linux-basics.sh

echo
echo "=================================================="
echo "1. Who am I?"
echo "=================================================="
whoami
id

echo
echo "=================================================="
echo "2. Where am I?"
echo "=================================================="
pwd
echo "Current directory contents:"
ls -lah

echo
echo "=================================================="
echo "3. Create a folder and a log file"
echo "=================================================="
mkdir -p devops-linux-demo
cd devops-linux-demo

echo "INFO Application started" > app.log
echo "INFO Connected to database" >> app.log
echo "ERROR Could not reach payment service" >> app.log
echo "INFO Retry scheduled" >> app.log
echo "ERROR Request timed out" >> app.log

echo "Created folder and sample log:"
pwd
ls -l

echo
echo "=================================================="
echo "4. Read a file"
echo "=================================================="
echo "--- whole file ---"
cat app.log
echo "--- first 2 lines ---"
head -n 2 app.log
echo "--- last 2 lines ---"
tail -n 2 app.log

echo
echo "=================================================="
echo "5. Search a file"
echo "=================================================="
echo "Lines containing ERROR:"
grep ERROR app.log
echo "Number of lines:"
wc -l app.log

echo
echo "=================================================="
echo "6. Copy and rename"
echo "=================================================="
cp app.log app-backup.log
mv app-backup.log app-copy.log
ls -l

echo
echo "=================================================="
echo "7. Add a new line to the log"
echo "=================================================="
echo "ERROR Disk is getting full" >> app.log
echo "New ERROR lines:"
grep ERROR app.log

echo
echo "=================================================="
echo "8. Disk and system"
echo "=================================================="
df -h
hostname
uname

echo
echo "=================================================="
echo "9. Processes"
echo "=================================================="
echo "First few process rows:"
ps aux | head

echo
echo "=================================================="
echo "10. Useful shell values"
echo "=================================================="
echo "Home directory: $HOME"
echo "Current user: $(whoami)"
echo "Current date/time:"
date

echo
echo "=================================================="
echo "Demo complete"
echo "=================================================="
echo "Sample files are in: $(pwd)"
echo "This demo created devops-linux-demo/app.log and app-copy.log."
echo "Remove the folder later if you do not need it:"
echo "  cd .."
echo "  rm -rf devops-linux-demo"
