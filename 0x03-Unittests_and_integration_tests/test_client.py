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
