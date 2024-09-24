import turtle
turtle.Screen().bgcolor("Silver")
turtle.Screen().setup(500,700)
Polygon=turtle.Turtle()
Sides=6
L=150
Angle=360/Sides
for r in range(Sides):
   Polygon.forward(L)
   Polygon.right(Angle)