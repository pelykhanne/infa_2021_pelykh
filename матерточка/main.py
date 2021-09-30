import turtle
turtle.shape('turtle')
turtle.speed(0)
turtle.forward(600)
turtle.backward(600)


ay=-9.81
Vx=13
Vy=70
V0y=Vy
V0x=Vx
x=0
y=0
for i in range (1,437,1):
    turtle.goto(x,y)
    dt=0.0005*i
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    if y<0:
        Vy=V0y-10
        V0y=Vy
        Vx=V0x-0.5
        V0x=Vx
