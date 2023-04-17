# main.py -- put your code here!
import time
import machine
import ssd1306

i2c = machine.I2C(scl=machine.Pin(1), sda=machine.Pin(2), freq=100000)
display = ssd1306.SSD1306_I2C(64, 48, i2c)

display.fill(0)
display.text('Start', 0, 0, 1)
display.show()


while True:
    time.sleep(1)
    display.fill(0)
    display.fill_rect(20, 0, 25, 10, 1)
    display.vline(33, 10, 20, 1)  # y=35
    display.line(33, 30, 10, 45, 1)
    display.line(33, 30, 56, 45, 1)
    display.line(33, 20, 10, 10, 1)
    display.line(33, 20, 56, 10, 1)
    display.show()
