from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Turtle race',prompt='Wie gaat er winnen? kies een kleur:')
color = ['red','green','blue','yellow','orange','purple','black']
all_turtles = []

counter = 30
for t in range(0,6):
    i = t
    t = Turtle(shape='turtle')
    t.penup()
    t.goto(x=-230,y=(-70 + (counter*i)))
    t.color(color[i])
    t.pendown()
    all_turtles.append(t)

race = True

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race = False
            print(f'{turtle.pencolor()} heeft gewonnen!')
        r = random.randint(0,10)
        turtle.forward(r)    

screen.exitonclick()