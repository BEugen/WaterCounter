TEXT_WIDTH_KOEFF = 0.5
CHAR_OFFESET_KOEFF = 0.16
POINT_SIZE_KOEFF = 0.16


class rgbtext(object):
    def __init__(self, display):
        self.display = display

    def half_char(self, f_size, line):
        return int(f_size / 2) - int(line / 2)

    def char_0(self, x, y, f_size, x_size, line, color):
        self.display.fill_rectangle(x, y, x_size, line, color)
        self.display.fill_rectangle(x, y, line, f_size, color)
        self.display.fill_rectangle(x, y + f_size - line, x_size, line, color)
        self.display.fill_rectangle(x + x_size - line, y, line, f_size, color)

    def char_1(self, x, y, f_size, x_size, line, color):
        self.display.fill_rectangle(x + x_size - line, y, line, f_size, color)

    def char_2(self, x, y, f_size, x_size, line, color):
        h_x = self.half_char(f_size, line)
        self.display.fill_rectangle(x, y, x_size, line, color)
        self.display.fill_rectangle(x, y + h_x, x_size, line, color)
        self.display.fill_rectangle(x, y + f_size - line, x_size, line, color)
        self.display.fill_rectangle(x + x_size - line, y, line, h_x, color)
        self.display.fill_rectangle(x, y + h_x, line, h_x, color)

    def char_3(self, x, y, f_size, x_size, line, color):
        h_x = self.half_char(f_size, line)
        self.display.fill_rectangle(x, y, x_size, line, color)
        self.display.fill_rectangle(x, y + h_x, x_size, line, color)
        self.display.fill_rectangle(x, y + f_size - line, x_size, line, color)
        self.display.fill_rectangle(x + x_size - line, y, line, f_size, color)

    def char_4(self, x, y, f_size, x_size, line, color):
        h_x = self.half_char(f_size, line)
        self.char_1(x, y, f_size, x_size, line, color)
        self.display.fill_rectangle(x, y + h_x, x_size, line, color)
        self.display.fill_rectangle(x, y, line, h_x, color)

    def char_5(self, x, y, f_size, x_size, line, color):
        h_x = self.half_char(f_size, line)
        self.display.fill_rectangle(x, y, x_size, line, color)
        self.display.fill_rectangle(x, y + h_x, x_size, line, color)
        self.display.fill_rectangle(x, y + f_size - line, x_size, line, color)
        self.display.fill_rectangle(x, y, line, h_x, color)
        self.display.fill_rectangle(x + x_size - line, y + h_x, line, h_x, color)

    def char_6(self, x, y, f_size, x_size, line, color):
        h_x = self.half_char(f_size, line)
        self.display.fill_rectangle(x, y, line, f_size, color)
        self.display.fill_rectangle(x, y + h_x, x_size, line, color)
        self.display.fill_rectangle(x, y + f_size - line, x_size, line, color)
        self.display.fill_rectangle(x + x_size - line, y + h_x, line, h_x, color)

    def char_7(self, x, y, f_size, x_size, line, color):
        self.char_1(x, y, f_size, x_size, line, color)
        self.display.fill_rectangle(x, y, x_size, line, color)

    def char_8(self, x, y, f_size, x_size, line, color):
        h_x = self.half_char(f_size, line)
        self.char_0(x, y, f_size, x_size, line, color)
        self.display.fill_rectangle(x, y + h_x, x_size, line, color)

    def char_9(self, x, y, f_size, x_size, line, color):
        h_x = self.half_char(f_size, line)
        self.char_1(x, y, f_size, x_size, line, color)
        self.display.fill_rectangle(x, y, x_size, line, color)
        self.display.fill_rectangle(x, y + h_x, x_size, line, color)
        self.display.fill_rectangle(x, y, line, h_x, color)

    def char_point(self, x, y, f_size, color):
        size = int(f_size * POINT_SIZE_KOEFF)
        self.display.fill_rectangle(x, y + f_size - size, size, size, color)

    def char_eq(self, x, y, f_size, x_size, line, color):
        h_x = self.half_char(f_size, line) - line
        self.display.fill_rectangle(x, y + h_x, x_size, line, color)
        self.display.fill_rectangle(x, y + h_x + line*2, x_size, line, color)

    def char_l(self, x, y, f_size, x_size, line, color):
        self.display.fill_rectangle(x, y, line, f_size, color)
        self.display.fill_rectangle(x, y + f_size - line, x_size, line, color)

    def dispatch(self, value, x, y, f_size, x_size, line, color):
        method_name = 'char_' + str(value)
        method = getattr(self, method_name)
        return method(x, y, f_size, x_size, line, color)

    def text(self, text, x=0, y=0, f_size=30, line=2, color=0xffff, background=0x0000):
        x_size = int(f_size * TEXT_WIDTH_KOEFF)
        char_offset = int(f_size * CHAR_OFFESET_KOEFF)
        for char in text:
            self.display.fill_rectangle(x, y, x_size, f_size, background)
            if char == '.':
                self.char_point(x, y, f_size, color)
                x += int(f_size * POINT_SIZE_KOEFF) + char_offset
                continue
            elif char == '=':
                self.dispatch('eq', x, y, f_size, x_size, line, color)
            else:
                self.dispatch(char, x, y, f_size, x_size, line, color)
            x += x_size + char_offset
            if (x + x_size) > self.display.width:
                continue

    def len_pix(self, text, f_size=30):
        x = 0
        x_size = int(f_size * TEXT_WIDTH_KOEFF)
        char_offset = int(f_size * CHAR_OFFESET_KOEFF)
        for char in text:
            if char == '.':
                x += int(f_size * POINT_SIZE_KOEFF) + char_offset
            else:
                x += x_size + char_offset
        return x
