import unittest
import sys
import os

# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.create_repo import create_repository

class TestCreateRepo(unittest.TestCase):

    def test_create_repository_success(self):
        # Mock the GitHub API response for a successful repository creation
        response = create_repository("test-repo", "This is a test repository.")
        self.assertEqual(response['name'], "test-repo")
        self.assertEqual(response['description'], "This is a test repository.")
        self.assertTrue(response['private'])

    def test_create_repository_failure(self):
        # Mock the GitHub API response for a failed repository creation
        with self.assertRaises(Exception):
            create_repository("", "This should fail due to empty repo name.")

if __name__ == '__main__':
    unittest.main()