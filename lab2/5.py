import turtle
turtle.shape('turtle')
side = 4
for i in range(10):

    for sides in range(1,5):
        turtle.forward(20 + i * 20)
        turtle.right(90)
    turtle.penup()
    turtle.left(135)
    turtle.forward(14)
    turtle.right(135)
    turtle.pendown()