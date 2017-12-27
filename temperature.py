import time
import machine
import onewire, ds18x20
from machine import Pin


class Temperature(object):

    def __init__(self, ow_pin, wh_en_pin, config):
        self.config = config
        self.ds = ds18x20.DS18X20(onewire.OneWire(Pin(ow_pin)))
        self.wh_en_pin = machine.Pin(wh_en_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.wh_en_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.waterheat_end)

    def scan(self):
        return self.ds.scan()

    def temperature(self):
        roms = self.ds.scan()
        self.ds.convert_temp()
        time.sleep_ms(750)
        t = self.config['t']
        for rom in roms:
            key = ''.join('{:02x}'.format(x) for x in rom)
            t[key]['t'] = self.ds.read_temp(rom)
            if t[key]['id'] == 0 and (t[key]['max'] - t[key]['min']) > 20.0:
                self.watercold_end()

    def waterheat_end(self, p):
        if p.value():
            for x in self.config['t']:
                if self.config['t'][x]['id'] != 0:
                    self.config['t'][x]['max'] = self.config['t'][x]['t']
            self.config['p']['pw'] = False
        else:
            self.config['p']['pw'] = True

    def watercold_end(self):
        for x in self.config['t']:
            if self.config['t'][x]['id'] != 0:
                self.config['t'][x]['min'] = self.config['t'][x]['t']

    def temp_scaling(self, min, max, val):
        if (max - min) != 0.0:
            return (val - min) / (max - min)
        else:
            return 0.0

    def temp_level(self):
        val = 0.0
        for x in self.config['t']:
            if self.config['t'][x]['id'] != 0:
                val += 16.67 * self.temp_scaling(self.config['t'][x]['min'], self.config['t'][x]['max'],
                                                 self.config['t'][x]['t'])
        return val if val <= 100.0 else 100.0

