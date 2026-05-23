# PowerShell script to push project to GitHub
# Run from project root: .\github_upload\push_windows.ps1

# Option A: create repo using GitHub CLI (recommended if installed)
# gh must be authenticated (run `gh auth login` first)

# Replace REPO_NAME with desired repo name (e.g., pdf_project)
$REPO_NAME = "REPO_NAME"
# Create remote repo and push
# gh repo create $REPO_NAME --public --source . --remote origin --push

# Option B: manual steps (works if you created a repo on github.com)
# Replace <USERNAME> and <REPO> with your GitHub username and repository name.
# git init
# git add .
# git commit -m "Initial commit"
# git branch -M main
# git remote add origin https://github.com/<USERNAME>/<REPO>.git
# git push -u origin main

Write-Host "Edit this file and follow the commented commands. If you want, paste your repo URL and I can attempt a push for you."