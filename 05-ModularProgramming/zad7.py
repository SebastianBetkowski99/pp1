import turtle
pen=turtle.Turtle()
for s in range(8):
    if s % 2 == 0:
        pen.forward(100)
    else:
        pen.right(90)     

turtle.done()