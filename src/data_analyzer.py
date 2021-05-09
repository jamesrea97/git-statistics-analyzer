"""This module contains data handling logic"""
import os
from datetime import datetime
import uuid
from git_objects import (
    Repo, Repos
)
from event import Event


def analyze(load: dict[str, str]):
    topic = load['topic']

    # TODO Add commit topics, etc as needed
    if topic == os.getenv('KAFKA_REPO_SANITIZED_TOPIC'):
        return _analyze_repos(load)


def _analyze_repos(repos_load: dict[str, str]) -> Event:
    request_id = repos_load['id_']
    load = repos_load['load']

    repos = []
    for json_repo in load:
        owner = json_repo['owner']
        name = json_repo['name']
        created_at = json_repo['created_at']
        updated_at = json_repo['updated_at']
        default_branch = json_repo['default_branch']
        language = json_repo['language']
        git_url = json_repo['git_url']

        repo = Repo(owner=owner,
                    name=name,
                    created_at=datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S'),
                    updated_at=datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S'),
                    default_branch=default_branch,
                    language=language,
                    git_url=git_url)
        repos.append(repo)
    
    repos_analyzed = Repos(repos=repos)

    return Event(
        id_=uuid.UUID(request_id),
        topic=os.getenv('KAFKA_REPO_ANALYZED'),
        timestamp=datetime.utcnow(),
        load=repos_analyzed
    )
