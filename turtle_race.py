from turtle import Turtle, Screen
from random import randint

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink']

y_positions = [-100, -60, -20, 20, 60, 100]
ALIGNMENT = 'right'
FONT = ("Courier", 7, 'bold')

screen = Screen()
screen.setup(700,400)
screen.bgcolor("white")
user_bet =screen.textinput("make your bet", "Which turtle will win the race? ")
if user_bet not in colors:
    tim = Turtle()
    tim.write(f"Your bet is not in the race ", align = 'center', font = FONT)
    tim.hideturtle()
else:
 all_turtles = []
 for turtle_index in range(6):
  new_turtle = Turtle("turtle")
  new_turtle.color(colors[turtle_index])    
  new_turtle.penup()
  new_turtle.goto(-350, y_positions[turtle_index]) 
  all_turtles.append(new_turtle)  

 is_race_on = True
 while is_race_on:
     for new_turtle in all_turtles:
         if new_turtle.xcor() >313 :
           is_race_on = False
           if user_bet == new_turtle.pencolor():
             new_turtle.write(f"You've won! {new_turtle.pencolor()} is the winner! ", align = ALIGNMENT, font = FONT )
           else:
              new_turtle.write(f"You've lost! {new_turtle.pencolor()} is the winner! ", align = ALIGNMENT, font = FONT)
         random_move = randint(0,10)
         new_turtle.forward(random_move)
      
screen.exitonclick()      