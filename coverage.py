import unittest
from unittest.mock import patch
from random import randint
from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

class TestRollDice(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        FlaskInstrumentor().instrument_app(self.app)
        self.configure_opentelemetry()

    def configure_opentelemetry(self):
        trace.set_tracer_provider(
            TracerProvider(
                resource=Resource.create(attributes={"service.name": "rolldice-service"})
            )
        )
        otlp_exporter = OTLPSpanExporter(endpoint="opentelemetrycollector.elastic-stack.svc.cluster.local:4317", insecure=True)
        span_processor = BatchSpanProcessor(otlp_exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)

    def test_roll_dice(self):
        with patch('random.randint', return_value=3):
            response = self.client.get('/rolldice')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), '3')

if __name__ == '__main__':
    unittest.main()