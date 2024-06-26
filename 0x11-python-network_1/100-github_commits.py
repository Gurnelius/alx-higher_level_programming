#!/usr/bin/python3
'''
    List 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”
    Uses the GitHub API (Doc: https://developer.github.com/v3/repos/commits/)
    Print all commits by: `<sha>: <author name>` (one by line)
'''

import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Failed to fetch commits. Status code:", response.status_code)
