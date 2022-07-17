#!/usr/bin/env python3
"""project:Snow Challenge, created:1/17/2022, author:seraph★776"""


import turtle


def main():
    my_pen = turtle.Turtle()
    my_pen.shape('turtle')
    my_pen.speed(500)
    my_pen.pensize(2)

    my_pen.color('#0033FF')
    my_pen.left(90)

    for i in range(0, 6):
        my_pen.forward(100)
        my_pen.forward(-40)
        my_pen.left(40)
        my_pen.forward(30)
        my_pen.forward(-30)
        my_pen.right(80)
        my_pen.forward(30)
        my_pen.forward(-30)
        my_pen.left(40)
        my_pen.forward(-60)
        my_pen.right(60)        



if __name__ == '__main__':
    main()
