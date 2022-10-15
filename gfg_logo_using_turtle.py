import turtle

tut = turtle.Screen()

tut.bgcolor("black")

pen = turtle.Turtle()

pen.speed(200)

pen.color("Green")

pen.width(20)
tut = turtle.Screen()

for x in range(180):
    pen.forward(1)
    pen.right(1)

pen.right(90)
pen.forward(50)

pen.right(90)
pen.forward(130)

pen.right(90)
pen.forward(50)
pen.left(90)

for x in range(180):
    pen.backward(1)
    pen.right(1)

turtle.done()
