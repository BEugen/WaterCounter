import time
import machine
import onewire, ds18x20
from machine import Pin


class Temperature(object):

    def __init__(self, ow_pin, wh_en_pin, config):
        self.config = config
        self.ds = ds18x20.DS18X20(onewire.OneWire(Pin(ow_pin)))
        self.wh_en_pin = machine.Pin(wh_en_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.wh_en_pin.irq(trigger=Pin.IRQ_RISING, handler=self.waterheat_end)

    def scan(self):
        return self.ds.scan()

    def temperature(self):
        roms = self.ds.scan()
        self.ds.convert_temp()
        time.sleep_ms(750)
        for rom in roms:
            key = ''.join('{:02x}'.format(x) for x in rom)
            self.config[key]['t'] = self.ds.read_temp(rom)
            if self.config[key]['id'] == 6 and self.config[key]['min'] > self.config[key]['t']:
                self.watercold_end()


    def waterheat_end(self):
        for x in range(6):
            d = self.config['t' + str(x)]
            d['max'] = d['t']

    def watercold_end(self):
        for x in self.config.keys():
            if '10' in x:
                self.config[x]['min'] = self.config[x]['t']

    def temp_scaling(self, min, max, val):
        if min != 0.0 and max != 0.0:
            return 100 * ((val - min) / (max - min))
        else:
            return 0.0

    def temp_level(self):
        val = 0.0
        for x in range(6):
            d = self.config['t' + str(x)]
            val += 16.67 * self.temp_scaling(d['min'], d['max'], d['t'])
        return val if val <= 100.0 else 100.0
