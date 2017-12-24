import os
import ujson

FILE_NAME = 'cfg.txt'


class Config(object):

    def load_config(self):
        if FILE_NAME in os.listdir():
            f = open(FILE_NAME, 'r')
            rs = ujson.loads(f.read())
            f.close()
            return rs
        else:
            return {'hot': 0.0, 'cold': 0.0, 'l': 0.0, 't0': {'t': 0.0, 'id': 0, 'min': 0.0, 'max': 0.0},
                    't1': {'t': 0.0, 'id': 0, 'min': 0.0, 'max': 0.0},
                    't2': {'t': 0.0, 'id': 0, 'min': 0.0, 'max': 0.0},
                    't3': {'t': 0.0, 'id': 0, 'min': 0.0, 'max': 0.0},
                    't4': {'t': 0.0, 'id': 0, 'min': 0.0, 'max': 0.0},
                    't5': {'t': 0.0, 'id': 0, 'min': 0.0, 'max': 0.0},
                    't6': {'t': 0.0, 'id': 0, 'min': 0.0, 'max': 0.0}}

    def save_config(self, data):
        dt = ujson.dump(data)
        f = open(FILE_NAME, 'w')
        f.write(dt)
        f.close()
