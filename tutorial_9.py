import turtle

loadWindow = turtle.Screen()
turtle.speed(14)
loadWindow.bgcolor("black")
for i in range(100):
	turtle.color("red")
	turtle.circle(5 * i)
	turtle.color("yellow")
	turtle.circle(-5 * i)
	turtle.left(i)
	
turtle.exitonclick()

