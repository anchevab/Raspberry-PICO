# Raspberry Pi Pico TEMT600 analog light sensor
# TEMT600 - Pico GPIO 28 ADC2 - Pin 34

import machine
import utime

temt600 = machine.ADC(28)
conversion_factor = 3.3 / (65535)

while True:
    sensor_value = temt600.read_u16()
    volt = sensor_value * conversion_factor
    print(volt)
    utime.sleep(1)