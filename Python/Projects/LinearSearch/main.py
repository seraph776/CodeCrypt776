#!/usr/bin/env python3
"""
project:
created:2022-1-1
@author:seraph1001100
email:seraph1001100@gmail.com
"""


def linear_search(lst, target):
    if target in lst:
        return target
    return False

  
def main():
    Alist = list(range(21))
    print(linear_search(Alist, 6))
    print(linear_search(Alist, 100))
    

if __name__ == '__main__':
    main()
