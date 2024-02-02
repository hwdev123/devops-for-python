#!/bin/env python3

from git import Repo

# We will initialize the repo the init method also creates a folder if it does not exist
repo = Repo.init("test_git")

# For an existing repo
# repo = Repo("../test_git")
