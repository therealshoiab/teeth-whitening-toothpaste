import json
import subprocess
import os

with open(r'C:\Users\Baha\.gemini\config\mcp_config.json', 'r') as f:
    cfg = json.load(f)

token = cfg['mcpServers']['github-mcp-server']['env']['GITHUB_PERSONAL_ACCESS_TOKEN']
user = 'therealshoiab'
repo = 'teeth-whitening-toothpaste'
remote_url = f'https://{user}:{token}@github.com/{user}/{repo}.git'

def run(cmd_list):
    print("Running:", " ".join(cmd_list[:3]))
    res = subprocess.run(cmd_list, capture_output=True, text=True)
    if res.stdout:
        print("STDOUT:", res.stdout[:200])
    if res.stderr:
        print("STDERR:", res.stderr[:200])
    return res.returncode

# 1. Git init
run(["git", "init"])
run(["git", "config", "user.name", "therealshoiab"])
run(["git", "config", "user.email", "therealshoiabmushtaq@gmail.com"])
run(["git", "branch", "-M", "main"])

# Set remote origin
subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
run(["git", "remote", "add", "origin", remote_url])

# Add files and commit
run(["git", "add", "."])
run(["git", "commit", "-m", "Initial commit: Teeth Whitening Toothpaste Shopify theme & GH Pages demo"])

# Push main
code = run(["git", "push", "-u", "origin", "main", "--force"])
print("Push main exit code:", code)

# Create and push gh-pages branch
run(["git", "checkout", "-B", "gh-pages"])
code_gh = run(["git", "push", "-u", "origin", "gh-pages", "--force"])
print("Push gh-pages exit code:", code_gh)

# Checkout back to main
run(["git", "checkout", "main"])
