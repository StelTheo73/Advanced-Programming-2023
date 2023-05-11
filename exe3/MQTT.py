""" Simple MQTT Publisher and Subscriber """

import random
import time
import paho.mqtt.client as client

CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
BROKER_ADDRESS = "test.mosquitto.org"
PUBLISHER_ID = "".join(random.sample(CHARACTERS, 16))
CLIENT_ID = "".join(random.sample(CHARACTERS, 16))
TOPIC = "steltheo73/exe3"
MESSAGE = "Hello world!"

def on_message(_, __, message):
    decoded_message = str(message.payload.decode("utf-8"))
    topic = message.topic
    print(f"Received message: {decoded_message}")
    print(f"Topic: {topic}")
    return decoded_message, topic

class Publisher(client.Client):
    """ Simple MQTT Publisher Class """

    def __init__(self, publisher_id: str, broker_address: str):
        super().__init__(publisher_id)
        print(f"Publisher ID: {publisher_id}")
        print(f"Publisher connecting to broker: {broker_address}...")
        self.connect(broker_address)
        print("Publisher connected!")

    def publish_message(self, topic: str, message: str):
        """ Publishes a message to a topic. """
        self.publish(topic, message)

class Subscriber(client.Client):
    """ Simple MQTT Subscriber Class """

    def __init__(self, client_id: str, broker_address: str, on_message_callback):
        super().__init__(client_id)
        print(f"Client ID: {client_id}")
        self.on_message = on_message_callback
        print(f"Client connecting to broker: {broker_address}...")
        self.connect(broker_address)
        print("Client connected!")

    def subscribe_to_topic(self, topic: str):
        """ Subscribes to a topic. """
        self.subscribe(topic)

publisher = Publisher(PUBLISHER_ID, BROKER_ADDRESS)
subscriber = Subscriber(CLIENT_ID, BROKER_ADDRESS, on_message)

subscriber.loop_start()
subscriber.subscribe_to_topic(TOPIC)

time.sleep(5) # wait for the subscriber to subscribe to the topic
publisher.publish(TOPIC, MESSAGE)
time.sleep(5) # wait for the subscriber to receive the message

subscriber.loop_stop()
