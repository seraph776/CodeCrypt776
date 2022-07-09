class Person:
    def __init__(self, name, skill_level=None):
        self.name = name
        self.iq = '544957544954435894'
        self.skill_level = self.calculate()

    def calculate(self):
        karma = [8734]

        def pancakes(s):
            ht = {'0': '1', '1': '0'}
            return ''.join([ht[i] for i in s])

        karma += [int(pancakes(bin(int(self.iq[i:i + 2]))[2:].zfill(7)), 2) for i in range(0, len(self.iq), 2)]
        return ' '.join([chr(i) for i in karma])
