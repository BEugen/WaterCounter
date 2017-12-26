import machine

import ili9341
from rgb import color565
import rgb_text


class Screen(object):

    def __init__(self, config):
        spi = machine.SPI(1, baudrate=32000000)
        self.display = ili9341.ILI9341(spi, cs=machine.Pin(0), dc=machine.Pin(15))
        self.config = config

    def write_display(self):
        self.display.fill(color565(255, 255, 255))
        self.display.fill_rectangle(2, 2, 238, 105, color565(255, 0, 0))
        self.display.fill_rectangle(2, 107, 238, 105, color565(0, 0, 255))
        self.display.fill_rectangle(2, 213, 238, 105, color565(0, 0, 0))
        rgb_text.text(self.display, str(self.config['hot']), 20, 50)
        rgb_text.text(self.display, str(self.config['cold']), 20, 155)
        rgb_text.text(self.display, str(self.config['l']), 20, 260)
