class Animal:
    def __init__(self, color, species):
        self.species = species
        self.color = color

    def __repr__(self):
        return f'({self.color} {self.species})'


class CuteFuzzyAnimal(Animal):
    def __init__(self, color, species):
        super().__init__(color, species)


class Serpent(Animal):
    def __init__(self, color, species):
        super().__init__(color, species)
        self.stomach = []

    def check_digestion(self):
        if len(self.stomach) > 1:
            return f'I have consume the following animals: {self.stomach}'
        return self.stomach

    def eat_meal(self, *animals):
        if len(self.stomach) >= 6:
            print('Stomach is full. Initiating digestion')
            print('Defecating:')
            for i in range(len(self.stomach)):
                self.digest_meal()
        else:
            print('Consuming:')
            for animal in animals:
                print(f'\t{chr(128013)}{animal}')
                self.stomach.append(animal)

    def digest_meal(self):
        poop = self.stomach.pop()
        print(f'\t{chr(128169)} {poop}')


if __name__ == '__main__':
    seraph = Serpent('black', 'snake')
    rabbit = Animal('white', 'rabbit')
    guinea_pig = Animal('brown', 'guinea pig')
    rodent = Animal('brown', 'rodent')

    seraph.eat_meal(rabbit, rodent, guinea_pig, rodent, rabbit, rabbit, rabbit, rabbit, rabbit)
    seraph.eat_meal(rabbit)
