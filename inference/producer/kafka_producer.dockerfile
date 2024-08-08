# Use an official Python runtime as a parent image
FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir confluent-kafka

CMD ["python", "producer_middleware.py"]