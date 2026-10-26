import unittest
from app import greet

class TestGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(
            greet("Student"),
            "Hello, Student! Welcome to ASDD."
        )

if __name__ == "__main__":
    unittest.main()
