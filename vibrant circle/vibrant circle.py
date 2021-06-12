import turtle

turtle.bgcolor("black")
turtle.pencolor("green")
turtle.pensize(1.5)
turtle.speed(0)
turtle.penup()
turtle.goto(0,200)  #for position shifting
turtle.pendown()

a=0
b=0
while True:
    turtle.forward(a)
    turtle.right(b)
    a+=3
    b+=1
    if b==210:
        break
    turtle.hideturtle()
turtle.done()