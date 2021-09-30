import turtle
turtle.shape('turtle')
turtle.speed(0)

def st(n):
    for i in range(1,n+1,1):
        turtle.right(180-180/n)
        turtle.forward(50)



st(15)
turtle.done()