#!/usr/bin/env python3
"""Generic utilities for github org client."""
import unittest
from parameterized import parameterized, parameterized_class
from typing import Dict
from unittest.mock import patch, Mock, PropertyMock, MagicMock
from requests.exceptions import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test github org client"""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, expected: Dict,
                 mock_get_json: MagicMock) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected
        test_class = GithubOrgClient(org)
        self.assertEqual(test_class.org, expected)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """Test that the result of _public_repos_url is the expected one
        based on the mocked payload"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Return payload of choice from mocked_get_json"""

        test_payload = {
            'repos_url': 'https://api.github.com/users/google/repos',
            'repos': [
                {
                    "id": 9065917,
                    "name": "firmata.py",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/firmata.py",
                    "created_at": "2013-03-27T23:20:35Z",
                    "updated_at": "2019-09-23T11:54:02Z",
                    "has_issues": True,
                    "forks": 46,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload['repos_url']
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "firmata.py",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

        @parameterized.expand([
            ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
            ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
        ])
