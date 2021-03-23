# -- Display rotary encoder value on I2C driven ssd_SH1106 OLED display
# ---- BYALA ROBOTS CLUB ---
# ---- author: A.Anchev  ---

from machine import Pin, I2C
from sh1106 import SH1106_I2C
import framebuf
import utime

WIDTH  = 128                                           # oled display width
HEIGHT = 64                                            # oled display height

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=200000)       # Init I2C using pins GP6 & GP7 (I2C1 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SH1106_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.rotate(True)
# Raspberry Pi logo as 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

while True:
    # Clear the oled display in case it has junk on it.
    oled.fill(0)
    # Blit the image from the framebuffer to the oled display
    oled.blit(fb, 1, 0)
    # Draw a horizontal line, starting from 0, 35 (x, y), 128 pixels wide
    oled.hline(0, 35, 128, 1)
    # Draw a vertical line, starting from 50, 40 (x, y), 15 pixels high
    oled.vline(50, 40, 15, 1)
    oled.fill_rect(10, 40, 15, 15, 1)
    # Draw an unfilled rectangle of 15x15 pixels, starting at 70,40
    oled.rect(70, 40, 15, 15, 1)
    # Draw an line starting at 40,0 to 65,25
    oled.line(40, 0, 65, 25, 1)
    oled.show()
    utime.sleep(1)