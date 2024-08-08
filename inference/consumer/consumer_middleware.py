from confluent_kafka import Consumer, KafkaException, KafkaError, TopicPartition

conf = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}
topic_name = 'test-topic'
consumer : Consumer = Consumer(**conf)
consumer.subscribe([topic_name])
# --> assign the paritions, otherwise, consumer will only consider the first seen partition
consumer.assign([TopicPartition(topic_name, p) for p in [0,1]])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            print("skipping ...")
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        print(f'Received message: {msg.value().decode("utf-8")} from topic {msg.topic()} [{msg.partition()}]')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
