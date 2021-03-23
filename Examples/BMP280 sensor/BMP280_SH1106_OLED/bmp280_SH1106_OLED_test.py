# --- Raspberry Pico with sensor BMP280 ---
# --- Byala Robots Club ---
# --- author.A.Anchev -----

from machine import I2C, Pin              # създаване на I2C обект
from bmx280 import BMX280
from sh1106 import SH1106_I2C
from time import sleep
# ---- SH1106 OLED object
WIDTH  = 128                                           # широчина на дисплея
HEIGHT = 64                                            # височина на дисплея

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)       # Init I2C using pins GP6 & GP7 (I2C1 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SH1106_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.rotate(True)
# ---- sensor BMP280 object
bus =  I2C(1,scl=Pin(15), sda=Pin(14), freq=200000)
bmp = BMX280(bus, 0x76)                # --- създаване на виртуален обект BMP280
bmp.baseline = 101800                  # задава се налягането на морското равнище в момента (ВАРНА)


while True:
    oled.fill(0)
    tempC = bmp.temperature
    pressure = round((bmp.pressure/100),1)
    altitude = int(bmp.altitude)
    print("Temperature:",tempC,"Pressure:",pressure,"Altitude:",altitude)
    oled.text("Sensor BMP-280",7,5)
    oled.hline(0, 17, 128, 1)
    oled.text("Temp= ",7,25)
    oled.text(str(tempC),49,25)
    oled.text("Press= ",7,37)
    oled.text(str(pressure),57,37)
    oled.text("Altitude= ",7,49)
    oled.text(str(altitude),80,49)
    oled.show()
    sleep(2)
    