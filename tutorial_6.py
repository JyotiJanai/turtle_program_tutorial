import turtle
def draw_triangle(some_turtle):
	for i in range(1, 4):
		some_turtle.forward(100)
		some_turtle.left(120)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("green")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(8)
	for i in range(1, 37):
		draw_triangle(brad)
		brad.circle(100)
		brad.right(10)

draw_art()
