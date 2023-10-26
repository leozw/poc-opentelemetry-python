import unittest
from unittest.mock import patch
from flask import Flask
from app import app as flask_app

class TestRollDice(unittest.TestCase):
    def setUp(self):
        self.app = flask_app
        self.app.testing = True  # Configura o Flask em modo de teste
        self.client = self.app.test_client()

    def test_roll_dice(self):
        with patch('app.roll', return_value='3'):  # Patch the roll function in app
            response = self.client.get('/rolldice')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), '3')

if __name__ == '__main__':
    unittest.main()
