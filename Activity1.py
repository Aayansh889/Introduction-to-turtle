import turtle
turtle.Screen().bgcolor("Orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

sides=int(input("Enter number of sides:"))
length=int(input("Enter the length you need:"))
angle=int(360/sides)

for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()