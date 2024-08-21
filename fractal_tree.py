import turtle as T
from random import gauss, uniform
from PIL.Image import open
from matplotlib.image import imread, imsave
from os import remove

T.tracer(False)
T.speed(0)
T.pensize(1)

def grow(length, decrease, angle, noise=0):
    if length > 5:
        T.forward(length)

        new_length = length * decrease

        if noise > 0:
            new_length *= uniform(0.9, 1.1)

        angle_left = angle + gauss(0, noise)
        angle_right = angle + gauss(0, noise)

        T.left(angle_left)
        grow(new_length, decrease, angle, noise)
        T.right(angle_left)

        T.right(angle_right)
        grow(new_length, decrease, angle, noise)
        T.left(angle_right)

        T.backward(length)

T.penup()
T.goto(0, -400)
T.left(90)
T.pendown()

grow(length=150, decrease=0.8, angle=30, noise=0)

# dummy_file_name = "tmp.ps"
# T.getscreen().getcanvas().postscript(file=dummy_file_name)
# image = open(dummy_file_name)

T.done()