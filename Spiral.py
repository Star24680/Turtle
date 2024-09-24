import turtle
turtle.Screen().bgcolor("Silver")
turtle.Screen().setup(500,700)
x=turtle.Turtle()
side=20
while True:
    for i in range(4):
        x.forward(side+1)
        x.left(90)
        side=side-5
    side=side+1   
