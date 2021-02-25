 # Display Image & text on I2C driven ssd1306 OLED display 
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
import framebuf

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c = I2C(0)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
#print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
#print("I2C Configuration: "+str(i2c))                   # Display I2C config


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

# Clear the oled display in case it has junk on it.
oled.fill(0)
oled.contrast(1)

# Load the book
book = open("book.txt")

# Read 16 chars at a time
while True:
    oled.fill(0)
    for x in range(8):
        currentLine = ""
        for y in range(16):
            currentChar = book.read(1)
            if currentChar == '\n':
                break
            else:
                currentLine = currentLine + currentChar
        oled.text(currentLine,0,x*8)
    oled.show()
    utime.sleep(5)


