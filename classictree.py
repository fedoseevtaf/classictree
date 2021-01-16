import turtle as tp

tp.left(90)
tp.speed(0)
tp.penup()
tp.sety(-200)
tp.pendown()

angle = 15
lenbranch = 80
count = 8

def tree(n, a, c):
    if c > count:
        pass
    else:
        c += 1
        tp.forward(n)
        tp.left(a / 2)
        tree(n * 0.8, a, c)
        tp.right(a)
        tree(n * 0.8, a, c)
        tp.left(a / 2)
        tp.backward(n)

tree(lenbranch, angle, 0)
