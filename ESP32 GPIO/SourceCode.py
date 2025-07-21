from machine import Pin
from time import sleep

button = Pin(34, Pin.IN, Pin.PULL_UP)
button2 = Pin(13, Pin.IN, Pin.PULL_UP)

led = Pin(5, Pin.OUT)
led1 = Pin(19, Pin.OUT)
led2 = Pin(18, Pin.OUT)
led3 = Pin(17, Pin.OUT)

while True:
    if button.value() == 0:  
        while True:
            led.on()
            sleep(0.1)
            led.off()
            sleep(0.1)

            led1.on()
            sleep(0.1)
            led1.off()
            sleep(0.1)

            led2.on()
            sleep(0.1)
            led2.off()
            sleep(0.1)

            led3.on()
            sleep(0.1)
            led3.off()
            sleep(0.1)

            if button2.value() == 0:
                led.off()
                led1.off()
                led2.off()
                led3.off()
                break 


    while button.value() == 0 or button2.value() == 0:
        sleep(0.01)
