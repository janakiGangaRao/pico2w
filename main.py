# This is a test file of the OTA code

import ugit
import time

# Use "LED" as the pin name for Pico W / Pico 2 W
led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.value(1)  # Turn LED on
    time.sleep(1)
    led.value(0)  # Turn LED off
    time.sleep(1)


