import unittest

from sample_app import greet


class TestSampleApp(unittest.TestCase):
    def test_greet_returns_expected_message(self):
        self.assertEqual(greet("CI/CD"), "Hello, CI/CD!")


if __name__ == "__main__":
    unittest.main()
