#!usr/bin/env python3
from git import Repo
from git import CommandError
from common.functions import get_user_input

# Clone the repo from the URL to our specified directory
def repo_clone(repo_url, repo_dir):
    try:
        Repo.clone_from(repo_url,to_path=repo_dir)
        print("Repo was succefully cloned")
    except CommandError as e:
        # convert the error message to a string and then check if the substring exists
        if "already exists" in str(e.args):
            print(f"The directory already exists.")
            

if __name__ == '__main__':
    repo_url = get_user_input()
    repo_dir = 
    try:
        repo_clone(repo_url=)
    