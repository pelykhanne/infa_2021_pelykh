import turtle

turtle.speed(0)
s = str(input())
a = 20
digits = [int(d) for d in s]  # строка чисел


def jump():
    turtle.penup()
    turtle.forward(a)
    turtle.pendown()


d0 = [(a, 90), (2 * a, 90), (a, 90), (2 * a, 90), (a, 0)]
d1 = [(0, 0), (0, 90), (a, 225), (1, 1), (a * 2 ** 0.5, 135), (2 * a, 180), (2 * a, 90)]
d2 = [(a, 90), (a, 45), (a * 2 ** 0.5, -135), (a, -90), (0, 0), (2 * a, 90), (1, 1)]
d3 = [(a, 135), (a * 2 ** 0.5, -135), (a, 135), (a * 2 ** 0.5, -135), (0, 0), (a, -90), (2 * a, 90), (1, 1)]
d4 = [(0, 90), (a, -90), (a, 90), (a, 180), (2 * a, 90)]
d5 = [(0, 90), (a, -90), (a, 90), (a, 90), (a, 90), (0, 0), (2 * a, 90), (1, 1), (a, 0)]
d6 = [(0, 90), (0, 0), (a, -90), (1, 1), (a, 90), (a, 90), (a, 90), (a, 45), (a * 2 ** 0.5, 45)]
d7 = [(a, 135), (a * 2 ** 0.5, -45), (a, 180), (0, 0), (2 * a, 90), (a, 0), (1, 1)]
d8 = [(a, 90), (2 * a, 90), (a, 90), (2 * a, 90), (a, 90), (a, 90), (a, 90), (a, 90), (a, 0)]
d9 = [(a, 90), (a, 45), (a * 2 ** 0.5, 180), (a * 2 ** 0.5, -135), (a, 90), (a, 90), (a, 0)]

dfont = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

for i in digits:
    for length, angle in dfont[i]:
        if (length == 0) and (angle == 0):
            turtle.penup()
        elif (length == 1) and (angle == 1):
            turtle.pendown()
        else:
            turtle.forward(length)
            turtle.right(angle)
    jump()
