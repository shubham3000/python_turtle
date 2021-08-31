import turtle

turtle.bgcolor("black")
turtle.speed(60)
turtle.pensize(1)
colors=("cyan","red")

for i in range(200):
    turtle.forward(i*4)
    turtle.right(91)
    turtle.color(colors[i%2])
    for j in range(2):
        turtle.forward(j*4)
        turtle.right(91)
        for k in range(2):
            turtle.forward(k*4)
            turtle.right(91)
            for l in range(500):
                turtle.forward(l*4)
                turtle.right(89)

turtle.done()