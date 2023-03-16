# main.py -- put your code here!
import time
import machine
import ssd1306
import math
from ens import ENS160  # import the device driver
import aht

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(64, 48, i2c)
# CO2 sensor
ens160 = ENS160(i2c, temperature=22, humidity=35)   # Initialise the ENS160 module
# temp. and humidity sensor
aht21 = aht.AHT2x(i2c, crc=True)

display.fill(0)
display.text('Start', 0, 0, 1)
display.show()
state = 0

while True:
    # Read from the sensor
    aqi = ens160.aqi
    tvoc = ens160.tvoc
    eco2 = ens160.eco2
    hum = aht21.humidity
    temp = aht21.temperature

    print(eco2.value)

    display.fill(0)
    if state % 3 == 0:
        display.text("Temp:", 0, 0, 1)
        display.text(str(temp), 0, 20, 1)
    elif state % 3 == 1:
        display.text("Humidity:", 0, 0, 1)
        display.text(str(hum), 0, 20, 1)
    elif state % 3 == 2:
        display.text("C02:", 0, 0, 1)
        display.text(str(eco2.value), 0, 20, 1)
    state += 1
    display.show()

    time.sleep(2)
