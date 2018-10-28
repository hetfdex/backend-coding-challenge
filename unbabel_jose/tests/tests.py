import unittest
from flask import current_app
from flask_testing import TestCase
from app import index
from unbabel_jose import app, uapi
from unbabel_jose.tasks import post_translation

class Test(TestCase):
    def create_app(self):
        return app

    def test_app(self):
        self.assertFalse(current_app is None)

    def test_unbabel(self):
        response = uapi.post_translations("This is a test")

        self.assertIn("This is a test", response.text)

        self.assertTrue(response.uid)

        self.assertEqual(response.status, "new")
        self.assertEqual(response.target_language, "es")
        self.assertEqual(response.source_language, "en")

if __name__ == '__main__':
    unittest.main()
