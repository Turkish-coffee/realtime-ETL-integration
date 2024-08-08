FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install confluent-kafka pyspark

CMD ["python", "consumer_middleware.py"]
