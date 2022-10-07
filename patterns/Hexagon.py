# import the turtle modules
import turtle


# define the function
# for hexagon
def form_hex(side):
	for i in range(6):
		my_pen.fd(side)
		my_pen.left(300)
		side -= 2


# Forming the window screen
tut = turtle.Screen()
tut.bgcolor("green")
tut.title("Turtle")

my_pen = turtle.Turtle()
my_pen.color("orange")

tut = turtle.Screen()

# for different sizes
side = 120

for i in range(5):
	form_hex(side)
	side -= 12
