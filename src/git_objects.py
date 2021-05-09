"""This module contains the git_objects of this service"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Repo:
    owner: str
    name: str
    created_at: datetime
    updated_at: datetime
    default_branch: str
    language: str
    git_url: str

    def to_json(self):
        return {
            "owner": self.owner,
            "name": self.name,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "default_branch": self.default_branch,
            "language": self.language,
            "git_url": self.git_url,
        }


@dataclass
class Repos:
    repos: list[Repo]
    language_count: str

    @staticmethod
    def get_language_count(repos):
        languages = {}
        for repo in repos:
            if not languages.get(repo.language):
                languages[repo.language] = 1
            else:
                languages[repo.language] += 1

        return languages

    def __init__(self, repos):
        self.repos = repos
        self.language_count = Repos.get_language_count(repos)

    def to_json(self):
        return {
            "repos": [repo.to_json() for repo in self.repos],
            "language_count": self.language_count
        }
