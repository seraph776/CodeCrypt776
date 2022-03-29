#!/usr/bin/env python3
"""
created: 2022-03-25 20:50:18
@author: seraph★776
contact: seraph776@gmail.com
details: Convert to camel_case
"""

import re


def split_upper(s):
    s = list(filter(None, re.split("([A-Z][^A-Z]*)", s)))
    return '_'.join(s).lower()


word = 'MyFunctionName'
print(split_upper(word))
