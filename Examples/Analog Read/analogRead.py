# Raspberry Pi Pico Analog Input Test
# analog-input.py

# POT - Pico GPIO 26 ADC0 - Pin 32

# DroneBot Workshop 2021
# https://dronebotworkshop.com


import machine
import utime

potentiometer = machine.ADC(26)

while True:
    print(potentiometer.read_u16())
    utime.sleep(2)