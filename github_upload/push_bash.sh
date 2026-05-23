#!/bin/bash
# Bash script to push project to GitHub
# Run from project root: ./github_upload/push_bash.sh

# Option A: using GitHub CLI (recommended)
# Replace REPO_NAME and run:
# REPO_NAME="pdf_project"
# gh auth login
# gh repo create $REPO_NAME --public --source . --remote origin --push

# Option B: manual
# git init
# git add .
# git commit -m "Initial commit"
# git branch -M main
# git remote add origin https://github.com/<USERNAME>/<REPO>.git
# git push -u origin main

echo "Edit this file and run the commands. Use gh CLI for simpler workflow."