FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install flask \
    opentelemetry-api==1.20.0 \
    opentelemetry-distro==0.41b0 \
    opentelemetry-exporter-otlp==1.20.0 \
    opentelemetry-exporter-otlp-proto-common==1.20.0 \
    opentelemetry-exporter-otlp-proto-grpc==1.20.0 \
    opentelemetry-exporter-otlp-proto-http==1.20.0 \
    opentelemetry-instrumentation==0.41b0 \
    opentelemetry-instrumentation-aws-lambda==0.41b0 \
    opentelemetry-instrumentation-dbapi==0.41b0 \
    opentelemetry-instrumentation-flask==0.41b0 \
    opentelemetry-instrumentation-logging==0.41b0 \
    opentelemetry-instrumentation-requests==0.41b0 \
    opentelemetry-instrumentation-sqlite3==0.41b0 \
    opentelemetry-instrumentation-urllib==0.41b0 \
    opentelemetry-instrumentation-urllib3==0.41b0 \
    opentelemetry-instrumentation-wsgi==0.41b0 \
    opentelemetry-propagator-aws-xray==1.0.1 \
    opentelemetry-proto==1.20.0 \
    opentelemetry-sdk==1.20.0 \
    opentelemetry-semantic-conventions==0.41b0 \
    opentelemetry-util-http==0.41b0 && \
    pip cache purge

EXPOSE 5000

CMD ["python", "./app.py"]
