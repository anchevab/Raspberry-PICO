from bmp180 import BMP180
from time import sleep
from machine import I2C, Pin              # създаване на I2C обект

bus =  I2C(1,scl=Pin(15), sda=Pin(14), freq=200000)   
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101400                  # задава се налагането на морското равнище в момента (ВАРНА)

while True:
    tempC = round(bmp180.temperature,2)
    press = round((bmp180.pressure)/100,2)
    altitude = int(bmp180.altitude)    
    print("Temp:",tempC,"   Pressure:", press,"   Altitude:", altitude)
    sleep(2)
    