import random
from turtle import Turtle, Screen

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Who you think will win? pick a color")
colors = ["red", "yellow", "green", "purple", "blue", "orange", "pink", "cyan", "grey"]
turtles= []

for i in range(9):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=-100+i*30)


if user_bet:
    race_on = True


while race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} is the winner!")
            else:
                print(f"You've lost! The {win_color} is the winner!")


screen.exitonclick()
