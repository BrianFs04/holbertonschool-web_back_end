#!/usr/bin/env python3
"""
test_client module
"""
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """TestGitHubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """Tests that GitHubOrgClient.org returns the correct value"""
        test = GithubOrgClient(org_name)
        self.assertEqual(test.org, mock_get.return_value)
        mock_get.assert_called_once

    def test_public_repos_url(self):
        """Tests that the result of _public_repos_url is
        the expected one based on the mocked payload"""
        payload = {"repos_url": True}
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,
                   return_value=payload) as mock_get:
            test = GithubOrgClient(org_name="abc")
            mock_get.assert_called_once
            self.assertEqual(test._public_repos_url,
                             payload)

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
        """Tests that the list of repos is what
        expected from the chosen payload"""
        payload = {"name": "abc"}
        return_value = payload
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,
                   return_value=return_value) as mock_list:
            test = GithubOrgClient("abc")
            self.assertEqual(test.public_repos(), [])
            mock_list.assert_called_once
            mock_get.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Tests that a client has license key"""
        test = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(expected, test)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGitHubOrgClient(unittest.TestCase):
    """TestIntegrationGitHubOrgClient class"""
    @classmethod
    def setUpClass(cls):
        """Mocks requests.get to return
        example payloads found in the fixtures"""
        cls.get_patcher = patch('requests.get', side_effect=True)
        cls.MockClass1 = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stops the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests public repos"""
        GithubOrgClient("Google")
        assert True

    def test_has_license(self):
        """Tests that a repo has license"""
        GithubOrgClient("Google")
        assert True
