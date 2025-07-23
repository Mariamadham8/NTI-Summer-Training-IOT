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
TOPIC_Sub = b"ledOnOff"
BETA = 3950

def connect_wifi():
    print("Connecting to Wi-Fi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.1)
    print("Connected:", wlan.ifconfig())

def mqtt_callback(topic, msg):
    print("Topic:", topic, "Message:", msg)
    if msg == b'on':
        Relay.on()
    elif msg == b'off':
        Relay.off()

def main():
    connect_wifi()
    client = MQTTClient("wokwi-esp32", MQTT_BROKER)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(TOPIC_Sub)
    print("MQTT connected and subscribed")

    last_heartbeat = time.ticks_ms()

    while True:
        analog_read = adc.read()
        celsius = 1 / (math.log(1 / (1023. / analog_read - 1)) / BETA + 1.0 / 298.15) - 273.15
        
        client.check_msg()  

        if time.ticks_diff(time.ticks_ms(), last_heartbeat) > 10000:
            message = "Temperature: {:.2f}°C".format(celsius)
            client.publish(TOPIC_PUB, message.encode())
            print("Published:", message)
            last_heartbeat = time.ticks_ms()
        
        time.sleep(0.1)

main()
