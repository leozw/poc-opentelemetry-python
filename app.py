from random import randint
from flask import Flask
import os
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

def configure_opentelemetry():
    if os.environ.get("TEST_ENV"):  # Se estiver em ambiente de teste, retorne
        return

    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource.create(attributes={"service.name": "rolldice-service"})
        )
    )
    otlp_exporter = OTLPSpanExporter(endpoint="opentelemetrycollector.default.cluster.local:4317", insecure=True)
    span_processor = BatchSpanProcessor(otlp_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

def roll_dice():
    return str(roll())

def roll():
    return randint(1, 6)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route("/rolldice")
def rolldice_route():
    return roll_dice()

if __name__ == '__main__':
    configure_opentelemetry()
    app.run(host='0.0.0.0')
