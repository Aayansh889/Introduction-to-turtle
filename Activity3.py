import turtle
spiral=turtle.Turtle()
size=0

while True:
    for i in range(4):
        spiral.forward(size+1)
        spiral.right(90)
        size-=5
    size+=1