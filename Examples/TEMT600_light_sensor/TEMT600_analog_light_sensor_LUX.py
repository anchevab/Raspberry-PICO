# Raspberry Pi Pico TEMT600 analog light sensor and convert to LUX
# TEMT600 - Pico GPIO 28 ADC2 - Pin 34

import machine
import utime

temt600 = machine.ADC(28)
conversion_factor = 3.3 / (65535)

while True:
    sensor_value = temt600.read_u16()
    lux = int(sensor_value*0.0333333)
    volt = sensor_value*conversion_factor
    print(lux)
    utime.sleep(1)