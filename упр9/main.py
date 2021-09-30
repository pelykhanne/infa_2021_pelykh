import turtle
import math
turtle.shape ('turtle')
def mugol(n):
    a=10*(n-2)
    turtle.left(180-0.5*(n-2)*180/n)
    for i in range (1,n+1,1):
        turtle.forward(10*n)
        turtle.left(180-(n-2)*180/n)
    turtle.right(180-0.5*(n-2)*180/n)

for i in range (3,11,1):
    mugol(i)
    turtle.penup()
    turtle.forward(i*3.3)
    turtle.pendown()


