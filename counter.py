import machine
import os
import ujson
from machine import Pin

IMPULS_TO_M3 = 0.001


class Counter(object):
    def __init__(self, p_hot_water, p_cold_water, config):
        self.cold_water = machine.Pin(p_cold_water, machine.Pin.IN, machine.Pin.PULL_UP)
        self.hot_water = machine.Pin(p_hot_water, machine.Pin.IN, machine.Pin.PULL_UP)
        self.cold_water.irq(trigger=Pin.IRQ_FALLING, handler=self.add_cold)
        self.hot_water.irq(trigger=Pin.IRQ_FALLING, handler=self.add_hot)
        self.hot_counter = config['hot']
        self.cold_counter = config['cold']

    def add_hot(self):
        self.hot_counter += IMPULS_TO_M3

    def add_cold(self):
        self.cold_counter += IMPULS_TO_M3

    def get_counter(self):
        return self.hot_counter, self.cold_counter

    def correct_counter(self, hot, cold):
        self.hot_counter = hot
        self.cold_counter = cold


