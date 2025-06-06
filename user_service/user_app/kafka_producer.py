from confluent_kafka import Producer
import environ

env = environ.Env()
environ.Env.read_env()

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()}')

def send_kafka_message(topic, message):
    p = Producer({'bootstrap.servers': env('KAFKA_BROKER')})
    p.produce(topic, message.encode('utf-8'), callback=delivery_report)
    p.flush()