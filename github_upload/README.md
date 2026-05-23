This folder contains instructions and scripts to upload this project to GitHub.

Files:
- push_windows.ps1 - PowerShell script with commands to create a GitHub repo (using gh) or push to an existing remote.
- push_bash.sh - Bash script with commands for Linux/macOS.

How to use (manual):
1. Create a new repository on GitHub (https://github.com/new) or use the GitHub CLI `gh repo create`.
2. From the project root (one level above this folder), run one of the scripts below depending on your OS.

Note: These scripts do not run automatically. They are templates showing the exact commands to run in your terminal. You must have Git installed and authenticated with GitHub (via `gh auth login` or SSH keys) to push.
