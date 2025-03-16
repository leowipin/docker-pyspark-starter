FROM python:3.12-slim

WORKDIR /app

COPY test1/saludo2.py .

CMD ["python", "saludo2.py"]