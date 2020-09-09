import turtle
def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)
		some_turtle.color("purple")

def draw_star(star):
	star = turtle.Turtle()
	for i in range(50):
		star.forward(100)
		star.right(144)
		star.color("pink")
		star.speed(8)
def draw_art():
	window = turtle.Screen()
	window.bgcolor("yellow")
	brad = turtle.Turtle()
	brad.shape("turtle")
	draw_star(brad)
	draw_square(brad)

draw_art()
