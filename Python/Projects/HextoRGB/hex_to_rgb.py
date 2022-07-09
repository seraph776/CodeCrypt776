#!/usr/bin/env python3
"""
created: 2022-06-04 23:06:01
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Snippets
metadoc: Hex to RGB
license: None
"""


def hex_to_rgb(hex_value):
    return tuple(int(hex_value[i: i + 2], 16) for i in (0, 2, 4))
