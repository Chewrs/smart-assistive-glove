from machine import Pin, I2C
import sh1106

#connect the SCL= D22, SDA = D21
class OLEDDisplay:
    def __init__(self, width=128, height=64, scl=22, sda=21, addr=0x3C, rotate=True):
        self.i2c = I2C(0, scl=Pin(scl), sda=Pin(sda))
        self.oled = sh1106.SH1106_I2C(width, height, self.i2c, addr=addr)
        if rotate:
            self.oled.rotate(True)
        self.oled.fill(0)
        self.oled.show()

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def show_text(self, text, x=0, y=0):
        self.oled.fill(0)
        self.oled.text(text, x, y)
        self.oled.show()

    def draw_text(self, text, x=0, y=0):
        self.oled.text(text, x, y)

    def update(self):
        self.oled.show()
        
