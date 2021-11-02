import turtle
turtle.shape('turtle')
turtle.speed(10)
for i in range(10000):
    turtle.forward(i * 0.001)
    turtle.left(1)
turtle.speed(10)