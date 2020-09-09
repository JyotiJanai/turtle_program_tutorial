import turtle
def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(150)
		some_turtle.right(90)
		
def draw_art():
	window = turtle.Screen()
	window.bgcolor("yellow")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(8)
	brad1 = turtle.Turtle()
	brad1.shape("triangle")
	brad1.color("blue")
	brad2 = turtle.Turtle()
	brad2.color("green")
	for i in range(1, 37):
		draw_square(brad2)
		brad.circle(100)
		brad1.circle(150)
		brad.right(10)
		brad1.right(10)
		brad2.right(10 )
draw_art()
