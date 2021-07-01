import turtle

turtle.bgcolor("black")
turtle.pensize(1.5)
turtle.speed(0)
turtle.pencolor("red")

def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-4

def drawdesign():
    for i in range(2):
        for colours in ["red", "blue", "yellow", "orange", "green"]:
            turtle.color(colours)
            drawcircle(135)
            turtle.right(36)

drawdesign()
turtle.done()