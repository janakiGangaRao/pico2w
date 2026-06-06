from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)
#print("[app] running v1 — slow blink")

while True:
    led.toggle()
    sleep(0.01)
    


