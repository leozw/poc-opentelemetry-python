FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip cache purge

EXPOSE 5000

CMD ["python", "./app.py"]