from machine import Pin, I2C  # ESP32 hardware
import ssd1306				  # OLED driver
import time					  # Time lib
 
# init OLED
# using default address 0x3C
#i2c = I2C(sda=Pin(4), scl=Pin(5))
i2c = I2C(1, scl = Pin(22), sda = Pin(21), freq = 400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.text('Firmware updated',0,0,1)
 
display.show()
