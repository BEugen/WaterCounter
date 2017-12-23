import machine
from machine import Pin

IMPULS_TO_M3 = 0.001


class Counter(object):
    def __init__(self, p_hot_water, p_cold_water):
        self.cold_water = machine.Pin(p_cold_water, machine.Pin.IN, machine.Pin.PULL_UP)
        self.hot_water = machine.Pin(p_hot_water, machine.Pin.IN, machine.Pin.PULL_UP)
        self.cold_water.irq(trigger=Pin.IRQ_FALLING, handler=self.add_cold)
        self.hot_water.irq(trigger=Pin.IRQ_FALLING, handler=self.add_hot)
        self.hot_counter = 0.0
        self.cold_counter = 0.0

    def add_hot(self):
        self.hot_counter += IMPULS_TO_M3

    def add_cold(self):
        self.cold_counter += IMPULS_TO_M3

    def load_data(self):
        pass
