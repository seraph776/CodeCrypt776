#!/usr/bin/env python3
"""
created: 2022-07-17 15:37:14
@author: seraph★776
contact: admin@codexguru.com
project: Egg Encoder
metadoc:https://www.101computing.net/egg-code-stamp-decoder/
"""


class EggCodeDecoder:
    FARM_METHOD = {'0': 'organic', '1': 'free range', '2': 'barn', '3': 'cage'}
    COUNTRY_ID = {'UK': 'united kingdom', 'NL': 'netherlands', 'FR': 'france', 'BE': 'belgium', 'DE': 'germany',
                  'ES': 'spain'}

    def __init__(self, code):
        self.code = code
        self.farm_method = EggCodeDecoder.FARM_METHOD.get(code[:1])
        self.country = EggCodeDecoder.COUNTRY_ID.get(code[1:3])
        self.farm_id = code[3:]

    def calculate(self):
        if self.country not in EggCodeDecoder.COUNTRY_ID:
            raise ValueError('Invalid Country code!')
        elif self.farm_method not in EggCodeDecoder.FARM_METHOD:
            raise ValueError('Invalid Farming Method')
        return f'Farming Method: {self.farm_method}\nCountry of Origin: {self.country}\nFarm ID: {self.farm_id}\n'


egg1 = EggCodeDecoder("1UK54321")
egg2 = EggCodeDecoder("0NL6789")
egg3 = EggCodeDecoder("9ES02468")

print(egg1.calculate())
print(egg2.calculate())
print(egg3.calculate())
