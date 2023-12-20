import sys
import paho.mqtt.client as paho

def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = paho.Client()
client.on_message = message_handling

if client.connect("192.168.100.14", 1890, 60) != 0:
    print("Couldn't connect to the mqtt broker.\n")
    sys.exit(1)

client.subscribe("temperature_topic")

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except Exception:
    print("Caught an exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()