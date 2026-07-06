import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Square Drawing Project")
pen = turtle.Turtle()
pen.pensize(3)
pen.color("darkblue")
for i in range(4):
    pen.forward(100)
    pen.right(90)
screen.mainloop()