# --- Raspberry Pico with sensor BMP280 ---
# --- Byala Robots Club ---
# --- author.A.Anchev -----

from machine import I2C, Pin              # създаване на I2C обект
from bmx280 import BMX280
from time import sleep

bus =  I2C(1,scl=Pin(15), sda=Pin(14), freq=200000)
bmp = BMX280(bus, 0x76)                # --- създаване на виртуален обект BMP280
bmp.baseline = 101800                  # задава се налягането на морското равнище в момента (ВАРНА)
while True:
    tempC = bmp.temperature
    pressure = round((bmp.pressure/100),1)
    altitude = int(bmp.altitude)
    print("Temperature:",tempC,"Pressure:",pressure,"Altitude:",altitude)
    sleep(2)
    