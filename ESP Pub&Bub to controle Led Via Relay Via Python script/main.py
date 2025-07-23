import paho.mqtt.client as mqtt

MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
Topic_Sub = "heartbeat"
Topic_Pub = "ledOnOff"


def on_connected(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(Topic_Sub)
    print(f"Subscribed to {Topic_Sub}")


def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")


client = mqtt.Client("labtop")
client.on_connect = on_connected
client.on_message = on_message
client.connect(MQTT_Broker, MQTT_Port, 60)

client.loop_start()

try:
    while True:
        msg = input("Enter 'on' or 'off' to control LED (or 'q' to quit): ")
        if msg.lower() == 'q':
            break
        client.publish(Topic_Pub, msg)
        print(f"Published successfully '{msg}' to {Topic_Pub}")
except KeyboardInterrupt:
    print("User Interrupted :)")
finally:
    client.loop_stop()
    client.disconnect()
    print("Disconnected :(")
