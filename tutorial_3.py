import turtle
def draw_Square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_triangle(some_turtle):
	for i in range(3):
		some_turtle.forward(100)
		some_turtle.left(120)
		some_turtle.forward(100)
		
	
def draw_art():
	window = turtle.Screen()
	window.bgcolor("green")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	draw_Square(brad)
	draw_triangle(brad)
	
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)
	window.exitonclick()

draw_art()

