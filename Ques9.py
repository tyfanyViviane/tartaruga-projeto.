import turtle
leo = turtle.Turtle()

def desenhe_forma():
    for i in range(6):
        leo.shape("turtle")
        leo.forward(25)
        leo.right(60)
        leo.pensize(3)

def pule(pixels):
    leo.penup()
    leo.forward(pixels)
    leo.pendown()


for i in range(6):
    for i in range(2):
        for i in range(4):
            desenhe_forma()
            pule(75)
        pule(-25)
        leo.right(60)
        pule(25)
        leo.right(120)
    pule(-25)
    leo.left(60)
    pule(50)
    leo.right(60)
    
turtle.exitonclick()  