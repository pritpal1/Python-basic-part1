import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range(9):
    for colors in['red','blue','pink','cyan','green','yellow','orange','white']:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(5)
turtle.exitonclick()