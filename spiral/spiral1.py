import turtle

turtle.bgcolor("black")
turtle.speed(70)
turtle.pensize(1)
colors=("cyan","red")

for i in range(400):
    turtle.forward(i*4)
    turtle.right(91)
    turtle.color(colors[i%2])

turtle.done()