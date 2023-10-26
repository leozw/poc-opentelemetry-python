import unittest
from unittest.mock import patch
from flask import Flask
from app import app as flask_app
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

class TestRollDice(unittest.TestCase):
    def setUp(self):
        self.app = flask_app  # Use a app importada
        self.client = self.app.test_client()

    def test_roll_dice(self):
        with patch('random.randint', return_value=3):
            response = self.client.get('/rolldice')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), '3')

if __name__ == '__main__':
    unittest.main()