#!/usr/bin/python

import turtle
import random
random.seed()
turtle.shape("turtle")
turtle.resizemode("user")
turtle.shapesize(0.75,0.75,0.5)
turtle.penup()


def caught(x,y):
    turtle.ht()
    turtle.home()
    turtle.right(random.randrange(361))
    turtle.st()


while 1: 
    turtle.fd(2)
    turtle.delay(10)
    turtle.right(33 - random.randrange(64))
    turtle.onclick(caught)


