import turtle as t



def up ():
    t.setheading(90)



def down ():
    t.setheading(-90)


def left ():
    t.setheading(180)


def right ():
    t.setheading(0)
    


t.listen()
t.shape(name="turtle")
snake = True

while snake:
    t.penup()
    t.forward(0.5)
    t.onkey(up,"Up")
    t.onkey(down,"Down")
    t.onkey(left,"Left")
    t.onkey(right,"Right")

t.mainloop()
