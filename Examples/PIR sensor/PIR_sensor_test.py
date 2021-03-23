# ---------- PIR sensor test
from machine import Pin
import utime
led = Pin(28, Pin.OUT)
pir = Pin(16, Pin.IN, Pin.PULL_UP)
led.low()
utime.sleep(3)
while True:
   print(pir.value())
   if pir.value() == 0:
       print("LED On")
       led.high()
       utime.sleep(5)
   else:
       print("Waiting for movement")
       led.low()
utime.sleep(0.2)