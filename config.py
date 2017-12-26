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
            return {'hot': 0.0, 'cold': 0.0, 'l': 0.0, '10f8adae02080072': {'t': 0.0, 'id': 0, 'min': 0.0, 'max': 0.0},
                    '1046e4ae0208007c': {'t': 0.0, 'id': 1, 'min': 0.0, 'max': 0.0},
                    '10bbaeae02080010': {'t': 0.0, 'id': 2, 'min': 0.0, 'max': 0.0},
                    '1041c5ae020800cc': {'t': 0.0, 'id': 3, 'min': 0.0, 'max': 0.0},
                    '10478bae02080035': {'t': 0.0, 'id': 4, 'min': 0.0, 'max': 0.0},
                    '10dbbfae02080062': {'t': 0.0, 'id': 5, 'min': 0.0, 'max': 0.0},
                    't6': {'t': 0.0, 'id': 6, 'min': 0.0, 'max': 0.0}}

    def save_config(self, data):
        dt = ujson.dump(data)
        f = open(FILE_NAME, 'w')
        f.write(dt)
        f.close()
