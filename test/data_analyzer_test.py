"""Module contains unit tests for data_analyzer module"""
import unittest
from uuid import UUID
from datetime import datetime

import context

import data_analyzer

from test_data import (
    REPO_EXAMPLE
)


class DataHandlerShould(unittest.TestCase):

    def test_sanitize_repo_returns_valid_event(self):
        repos_event = data_analyzer.analyze(REPO_EXAMPLE)

        self.assertEqual(repos_event.id_, UUID('6960ef42-36bc-47d7-9bee-a955e0757602'))
        self.assertEqual(repos_event.topic, 'repo-analyzed')
        self.assertIsNotNone(repos_event.timestamp)

        repos = repos_event.load

        self.assertEqual(len(repos.repos), 20)
        self.assertEqual(repos.language_count['Python'], 7)


if __name__ == "__main__":

    unittest.main()
