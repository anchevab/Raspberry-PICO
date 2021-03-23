# -- Display rotary encoder value on I2C driven ssd_SH1106 OLED display
# ---- BYALA ROBOTS CLUB ---
# ---- author: A.Anchev  ---

from machine import Pin, I2C
from sh1106 import SH1106_I2C
import framebuf
import utime
from bmp180 import BMP180
from time import sleep
# --- BMP180 object
bus =  I2C(1,scl=Pin(15), sda=Pin(14), freq=200000)   
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101400                  # задава се налагането на морското равнище в момента (ВАРНА)
# --- OLED object
WIDTH  = 128                                           # oled display width
HEIGHT = 64                                            # oled display height

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)       # Init I2C using pins GP6 & GP7 (I2C1 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SH1106_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.rotate(True)

while True:
    tempC = round(bmp180.temperature,2)
    press = round((bmp180.pressure)/100,2)
    altitude = int(bmp180.altitude)    
#     print("Temp:",tempC,"   Pressure:", press,"   Altitude:", altitude)
    oled.fill(0)
    # --- Add data from sensor BMP-180
    oled.text("Sensor BMP-180",7,5)
    oled.hline(0, 17, 128, 1)
    oled.text("Temp= ",7,25)
    oled.text(str(tempC),49,25)
    oled.text("Press= ",7,37)
    oled.text(str(press),57,37)
    oled.text("Altitude= ",7,49)
    oled.text(str(altitude),80,49)
    oled.show()
    utime.sleep(1)
