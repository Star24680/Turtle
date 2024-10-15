import turtle
turtle.Screen().bgcolor("Silver")
turtle.Screen().setup(500,700)
x=turtle.Turtle()
Side=7
Angle=360/Side
for r in range(Side):
    x.forward(50)
    x.left(Angle)

