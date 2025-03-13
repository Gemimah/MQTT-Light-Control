import paho.mqtt.client as mqtt

# MQTT Broker details
BROKER = "test.mosquitto.org"
TOPIC = "/student_group/light_control"

def on_message(client, userdata, msg):
    command = msg.payload.decode()
    if command == "ON":
        print("💡 Light is TURNED ON")
    elif command == "OFF":
        print("💡 Light is TURNED OFF")

# MQTT client setup
client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

print("Listening for MQTT messages...")
client.loop_forever()
