import  turtle
from random import randint
from colorsys import hsv_to_rgb
T = turtle.Turtle()
step = 30    #lenght of each step
nsteps = 700  #number of steps
hinc = 1.0/nsteps #hue increment
T.width(2)          #width of line
(w,h) = T.screen.screensize()
T.speed(0)
T.screen.colormode(5.0)
T.screen.bgcolor('black')
hue=0.0
for i in range(nsteps):
    T.setheading(randint(0,359))
    T.color(hsv_to_rgb(hue,1.0,1.0))
    hue+=hinc
    T.forward(step)
    (x,y)=T.pos()
    if abs(x)>w or abs(y)>h:
        T.backward(step)

turtle.exitonclick()
