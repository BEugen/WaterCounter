from machine import Pin, SPI
import ili9341
from rgb import color565
import rgb_text


class Screen(object):

    def __init__(self, config):
        spi = SPI(1, baudrate=32000000)
        self.display = ili9341.ILI9341(spi, cs=Pin(15), dc=Pin(2), rst=Pin(16))
        self.config = config

    def write_display(self):
        self.display.fill(ili9341.color565(255, 255, 255))
        self.display.fill_rectangle(2, 2, 236,  105, ili9341.color565(255, 0, 0))
        self.display.fill_rectangle(2, 109, 236, 105, ili9341.color565(0, 0, 255))
        self.display.fill_rectangle(2, 216, 236, 102, ili9341.color565(0, 0, 0))

    def clear_reg(self):
        self.display.fill_rectangle(90, 50, 15, 8, ili9341.color565(255, 0, 0))
        self.display.fill_rectangle(90, 155, 15, 8, ili9341.color565(0, 0, 255))

    def write_data(self):
        self.display.text(str(self.config['p']['hot']), 90, 50, background=ili9341.color565(255, 0, 0))
        self.display.text(str(self.config['p']['cold']), 90, 155, background=ili9341.color565(0, 0, 255))
        self.display.text('l=' + str(self.config['p']['l']), 65, 260)

