#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Percentage Graph 
metadoc: None
license: None
"""


def red_color(text):
    return '\033[1;91m' + text + '\033[0m'


def graph_bar(part, whole=100):
    return f'{red_color("|" * part)} {part / whole:.2f}%'

  if __name__ == '__main__':
    

      print(graph_bar(5))   # ||||| 0.05%
      print(graph_bar(10))  # |||||||||| 0.10%
      print(graph_bar(20))  # |||||||||||||||||||| 0.20%
      print(graph_bar(30))  # |||||||||||||||||||||||||||||| 0.30%
      print(graph_bar(40))  # |||||||||||||||||||||||||||||||||||||||| 0.40%
      print(graph_bar(50))  # |||||||||||||||||||||||||||||||||||||||||||||||||| 0.50%
      print(graph_bar(60))  # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 0.60%
      print(graph_bar(70))  # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 0.70%
