import os 
from git import Repo

class GitClient: 
    def __init__(self, RepoDir): 
        self.repo = Repo(RepoDir)
    def commit_repo_changes(self, commit_message:str = "Updating code", files_to_add: list = ["*"]):
        if self.repo.is_dirty(untracked_files=True):
            print('Changes detected.')
        self.repo.index.add(files_to_add)
		# Provide a commit message
        self.repo.index.commit(f"commit_message")

    def pull_newest_changes(self): 
        result = self.repo.remotes.origin.pull()
        return result

    def push_newest_changes(self):
        response = self.repo.remotes.origin.push()
        return response
		
