import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light yellow")
drawing_board.title("Interactive Drawing")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angel_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
    #turtle_instance.right(10)

def rotate_angel_left():
    turtle_instance.setheading(turtle_instance.heading()+10)
    #turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.home()
    turtle_instance.penup()
    turtle_instance.pendown()

def pen_up():
    turtle_instance.penup()

def pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=rotate_angel_right, key="Up")
drawing_board.onkey(fun=rotate_angel_left, key="Down")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=return_home, key="h")
drawing_board.onkey(fun=pen_up, key="u")
drawing_board.onkey(fun=pen_down, key="d")

turtle.mainloop()