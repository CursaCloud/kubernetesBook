FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates /app/templates

EXPOSE 5001

CMD ["python", "app.py"]
