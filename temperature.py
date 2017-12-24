import time
import machine
import onewire, ds18x20
from machine import Pin



class Temperature(object):

    def __init__(self, ow_pin, wh_en_pin, config):
        self.config = config
        dat = machine.Pin(ow_pin)
        self.ds = ds18x20.DS18X20(onewire.OneWire(dat))
        self.wh_en_pin = machine.Pin(wh_en_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.wh_en_pin.irq(trigger=Pin.IRQ_RISING, handler=self.waterheat_end)

    def scan(self):
        return self.ds.scan()

    def temperature(self):
        roms = self.ds.scan()
        for i in range(7):
            print('temperatures:', end=' ')
            self.ds.convert_temp()
            time.sleep_ms(750)
            for rom in roms:
                print(self.ds.read_temp(rom), end=' ')
            print()

    def waterheat_end(self):
        for x in range(6):
            d = self.config['t' + str(x)]
            d['max'] = d['t']


    def temp_scaling(self, min, max, val):
        if min != 0.0 and max != 0.0:
            return 100 * ((val - min) / (max - min))
        else
            return 0.0

    def temp_level(self):
        val = 0.0
        for x in range(6):
            d = self.config['t' + str(x)]
            val += 16.67*self. temp_scaling(d['min'], d['max'], d['t'])
        return val if val <= 100.0 else 100.0