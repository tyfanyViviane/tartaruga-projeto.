import turtle

leo = turtle.Turtle()
tartaruga = turtle.Turtle()
leo.shape("turtle")
leo.speed(1)
leo.speed(1)
leo.pensize(3)

for _ in range(6):  
    for _ in range(6):  
        leo.forward(50) 
        leo.right(60)    
    leo.right(60)
    
turtle.exitonclick()    