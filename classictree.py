#==============================================================#
generationsCount = 10

angle = 30
lenbranch = 100

randomKoef = 0.16

#==============================================================#
def angleChanger(angle):
    return angle

def lenChanger(lenbranch):
    return lenbranch


def stableLenChanger(lenbranch):
    return int(lenbranch * 0.8)

def randomLenChanger(lenbranch):
    return int((random() ** randomKoef) * (1 - randomKoef) * lenbranch)

lenChanger = stableLenChanger

#==============================================================#
import turtle as tp
from random import random

#==============================================================#
tp.left(90)
tp.speed(0)
tp.penup()
tp.sety(-200)
tp.pendown()

#==============================================================#
def tree(angle, lenbranch, *skipArgs, count = 0, **skipKeyargs):
    if count >= generationsCount:
        pass
    else:
        tp.forward(lenbranch)
        tp.left(angle / 2)

        newangle = angleChanger(angle)
        newlen = lenChanger(lenbranch)
        tree(newangle, newlen, count = count + 1)
        
        tp.right(angle)

        newangle = angleChanger(angle)
        newlen = lenChanger(lenbranch)
        tree(newangle, newlen, count = count + 1)
        
        tp.left(angle / 2)
        tp.backward(lenbranch)

tree(angle, lenbranch)
