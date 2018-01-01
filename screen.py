from machine import Pin, SPI
import ili9341
import rgb_text


class Screen(object):

    def __init__(self, config):
        spi = SPI(1, baudrate=32000000)
        self.display = ili9341.ILI9341(spi, cs=Pin(15), dc=Pin(2), rst=Pin(16))
        self.config = config
        self.rgbt = rgb_text.rgbtext(self.display)

    def write_display(self):
        self.display.fill(ili9341.color565(255, 255, 255))
        self.display.fill_rectangle(2, 2, 236,  105, ili9341.color565(255, 0, 0))
        self.display.fill_rectangle(2, 109, 236, 105, ili9341.color565(0, 0, 255))
        self.display.fill_rectangle(2, 216, 236, 102, ili9341.color565(0, 0, 0))

    def clear_reg(self):
        self.display.fill_rectangle(90, 50, 15, 8, ili9341.color565(255, 0, 0))
        self.display.fill_rectangle(90, 155, 15, 8, ili9341.color565(0, 0, 255))

    def write_data(self):
        txt = str(round(self.config['p']['hot'], 3))
        x = int(self.display.width/2 - self.rgbt.len_pix(txt)/2)
        self.display.fill_rectangle(2, 40, 236, 30, ili9341.color565(255, 0, 0))
        self.rgbt.text(txt, x, 40, background=ili9341.color565(255, 0, 0))
        txt = str(round(self.config['p']['cold'], 3))
        x = int(self.display.width / 2 - self.rgbt.len_pix(txt) / 2)
        self.display.fill_rectangle(2, 147, 236, 30, ili9341.color565(0, 0, 255))
        self.rgbt.text(txt, x, 147, background=ili9341.color565(0, 0, 255))
        self.write_level()

    def write_level(self):
        txt = 'l=' + str(round(self.config['p']['l'], 1))
        x = int(self.display.width / 2 - self.rgbt.len_pix(txt) / 2)
        self.display.fill_rectangle(10, 260, 224, 30, ili9341.color565(0, 0, 0))
        self.rgbt.text(txt, x, 260)

    def hot_indication(self, on):
        if not on:
            self.display.fill_rectangle(2, 216, 236, 102, ili9341.color565(0, 255, 0))
            self.display.fill_rectangle(6, 220, 228, 94, ili9341.color565(0, 0, 0))
            self.write_level()
        else:
            self.display.fill_rectangle(2, 216, 236, 102, ili9341.color565(0, 0, 0))
            self.write_level()
