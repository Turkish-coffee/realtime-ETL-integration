from confluent_kafka import Producer
import socket

conf = {
    'bootstrap.servers': 'kafka:9092',
    'client.id': socket.gethostname()
}

producer = Producer(**conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

i=0
while True:
    # this 
    producer.produce('test-topic', key=str(i), value=f'message-{i}', callback=delivery_report)
    producer.poll(1)
    i+=1