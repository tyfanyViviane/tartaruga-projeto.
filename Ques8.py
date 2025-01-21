import turtle
leo = turtle.Turtle()

def desenhe_uma_flor():
    for _ in range(6):  
        for _ in range(8): 
            leo.shape("turtle") 
            leo.pensize(2)  
            leo.forward(20)
            leo.right(30)
        leo.right(60) 


for _ in range(3):  
    desenhe_uma_flor()
    leo.penup()
    leo.forward(150)  
    leo.pendown()

turtle.exitonclick()    