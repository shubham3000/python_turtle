import turtle

turtle.bgcolor("black")
turtle.pensize(1.5)
turtle.speed(0)

for i in range(6):
    for colours in ["red","blue","yellow","orange","green","purple","cyan"]:
        turtle.color(colours)
        turtle.circle(100) #radius of circle
        turtle.left(10)  #angle shift for each circle

turtle.hideturtle()
turtle.done()