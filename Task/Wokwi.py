import time
import network
import machine
import math
from umqtt.simple import MQTTClient

adc = machine.ADC(machine.Pin(34))
adc.atten(machine.ADC.ATTN_11DB)
adc.width(machine.ADC.WIDTH_10BIT)

Relay = machine.Pin(13, machine.Pin.OUT)

SSID = "Wokwi-GUEST"
PASSWORD = ""
MQTT_BROKER = "test.mosquitto.org"
TOPIC_PUB = b"heartbeat"
TOPIC_Sub = b"esp32/relay_cmd"
BETA = 3950
mode = ""


def connect_wifi():
    print("Connecting to Wi-Fi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.1)
    print("Connected:", wlan.ifconfig())


def mqtt_callback(topic, msg):
    global mode
    print("Topic:", topic, "Message:", msg)
    msg_str = msg.decode().lower()

    if "manual on" in msg_str:
        Relay.on()
        mode = 'manual'
    elif "manual off" in msg_str:
        Relay.off()
        mode = 'manual'
    elif "automatic" in msg_str:
        mode = 'auto'
        check()


def check():
    analog_read = adc.read()
    celsius = 1 / (math.log(1 / (1023. / analog_read - 1)) /
                   BETA + 1.0 / 298.15) - 273.15
    if mode == 'auto':
        if celsius > 50:
            Relay.on()
        else:
            Relay.off()
    return celsius


def main():
    connect_wifi()
    client = MQTTClient("wokwi-esp32", MQTT_BROKER)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(TOPIC_Sub)
    print("MQTT connected and subscribed")

    last_heartbeat = time.ticks_ms()

    while True:
        temp = check()
        client.check_msg()

        if time.ticks_diff(time.ticks_ms(), last_heartbeat) > 2000:
            message = "Temperature: {:.2f}°C".format(temp)
            client.publish(TOPIC_PUB, message.encode())
            print("Published:", message)
            last_heartbeat = time.ticks_ms()

        time.sleep(0.1)


main()
