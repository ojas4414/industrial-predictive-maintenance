import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "factory/machine1/sensors"

client = mqtt.Client()
client.connect(BROKER, PORT)

while True:

    sensor_data = {
        "setting1": random.random(),
        "setting2": random.random(),
        "setting3": 100,
        "sensor1": random.uniform(500,550),
        "sensor2": random.uniform(600,650),
        "sensor3": random.uniform(1500,1600),
        "sensor4": random.uniform(1300,1400),
        "sensor5": random.uniform(10,20),
        "sensor6": random.uniform(20,30),
        "sensor7": random.uniform(500,600),
        "sensor8": 2388,
        "sensor9": random.uniform(800,900),
        "sensor10": random.uniform(1,2),
        "sensor11": random.uniform(40,50),
        "sensor12": random.uniform(500,550),
        "sensor13": 2388,
        "sensor14": random.uniform(8000,9000),
        "sensor15": random.uniform(8,9),
        "sensor16": random.uniform(0,0.1),
        "sensor17": random.uniform(380,420),
        "sensor18": 2388,
        "sensor19": 100,
        "sensor20": random.uniform(35,45),
        "sensor21": random.uniform(20,30)
    }

    client.publish(TOPIC, json.dumps(sensor_data))
    print("Sent sensor data")

    time.sleep(2)