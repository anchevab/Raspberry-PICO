# -- Display temperature from internal sensor on I2C driven ssd_SH1106 OLED display
# ---- BYALA ROBOTS CLUB ---
# ---- author: A.Anchev  ---

import machine
from machine import Pin, I2C
from sh1106 import SH1106_I2C
import framebuf
import utime
# --- OLED SH1106
WIDTH  = 128                           # oled display width
HEIGHT = 64                            # oled display height
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=200000)       # Init I2C using pins GP6 & GP7 (I2C1 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SH1106_I2C(WIDTH, HEIGHT, i2c)                   # Init oled display
oled.rotate(True)
# ---- temp sensor 
sensor_temp = machine.ADC(4)
conversion_factor = 3.3/(65535)
# ---------------
while True:
    reading = sensor_temp.read_u16()*conversion_factor
    temperature = 27-(reading - 0.706)/0.001721
    print(round(temperature,2))
    oled.fill(0)
    # Add some text
    oled.text("BYALA ROBOTS",15,8)
    oled.text("CLUB",50,25)
    oled.hline(0, 40, 128, 1)
    oled.text("Temp =",15,50)
    oled.text(str(round(temperature,2)),70,50)
    # Finally update the oled display so the image & text is displayed
    oled.show()
    utime.sleep(0.2)