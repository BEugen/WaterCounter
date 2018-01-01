import os
import ujson

FILE_NAME = 'cfg.txt'


class Config(object):
    def __init__(self):
        self.hot = 0.0
        self.cold = 0.0

    def load_config(self):
        rs = {}
        if FILE_NAME in os.listdir():
            f = open(FILE_NAME, 'r')
            rs = ujson.loads(f.read())
            f.close()
        else:
            rs = {'p': {'hot': 3.899, 'cold': 41.936, 'l': 0.0, 'pw': False},
                  't': {'10f8adae02080072': {'t': 0.0, 'id': 1, 'min': 0.0, 'max': 0.0},
                    '1046e4ae0208007c': {'t': 0.0, 'id': 2, 'min': 0.0, 'max': 0.0},
                    '10bbaeae02080010': {'t': 0.0, 'id': 3, 'min': 0.0, 'max': 0.0},
                    '1041c5ae020800cc': {'t': 0.0, 'id': 4, 'min': 0.0, 'max': 0.0},
                    '10478bae02080035': {'t': 0.0, 'id': 5, 'min': 0.0, 'max': 0.0},
                    '10dbbfae02080062': {'t': 0.0, 'id': 6, 'min': 0.0, 'max': 0.0},
                    '10cac74c010800f7': {'t': 0.0, 'id': 0, 'min': 0.0, 'max': 0.0}}}
        self.hot = rs['p']['hot']
        self.cold = rs['p']['cold']
        return rs

    def save_config(self, data):
        if self.hot != data['p']['hot'] or self.cold != data['p']['cold']:
            dt = ujson.dump(data)
            f = open(FILE_NAME, 'w')
            f.write(dt)
            f.close()
        self.hot = data['p']['hot']
        self.cold = data['p']['cold']