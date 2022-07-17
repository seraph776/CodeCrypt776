#!/usr/bin/env python3
"""project: , created:1/18/2022, author:seraph★776"""

from random import choice


class Virus:
    virus_types = ('bacteria', 'virus', 'fungus', 'parasite', 'prion', 'nano-virus', 'bio-weapon')
    viral_load = 0

    def __init__(self, name, *symptoms):
        self.virus_type = choice(Virus.virus_types)
        self.name = name
        self.symptoms = symptoms
        Virus.viral_load += 1

    def display_symptoms(self):
        print(f"The {('symptom', 'symptoms')[Virus.viral_load < 1]} of {self.name.title()} {('is', 'are')[len(self.symptoms) > 1]} {', '.join(self.symptoms)}!")

    def is_mutating(self):
        print(f"The {self.name.title()} {self.virus_type} has mutated into a new city!")

    def is_spreading(self):
        print(f"{Virus.viral_load} {('strain', 'strains')[Virus.viral_load > 1]} of the {self.name.title()} strain has spread to a new city!")


if __name__ == '__main__':
    lv426 = Virus('lv426', 'rotting flesh')
    lv426.display_symptoms()
    lv426.is_spreading()
    lv426.is_mutating()
