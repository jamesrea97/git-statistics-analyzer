"""This module contains Kafka handling logic"""
import json
from kafka import KafkaProducer, KafkaConsumer


async def publish(bootstrap_server: str, topic: str, value: dict[str, str]):
    producer = KafkaProducer(bootstrap_servers=bootstrap_server,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    return producer.send(topic=topic, value=value)


async def consume(bootstrap_server: str, topic: str, consumer_group: str):

    consumer = KafkaConsumer(topic,
                             bootstrap_servers=bootstrap_server,
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             group_id=consumer_group)
    for message in consumer:
        yield message.value
