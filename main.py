from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

mysnake= Snake()
food = Food()
score = Score()
screen.update()

screen.listen()


running = True
while running:
   

    screen.update()
    time.sleep(0.1)
    screen.onkey(mysnake.up,"Up")
    screen.onkey(mysnake.down,"Down")
    screen.onkey(mysnake.left,"Left")
    screen.onkey(mysnake.right,"Right")
    mysnake.move()
    #detect collision
    if mysnake.head.distance(food)<15:
            food.random_move()
            score.update_score()
            mysnake.extend()
            
    #detect collision with wall
    if mysnake.head.xcor()>280 or mysnake.head.xcor()<-300 or mysnake.head.ycor()<-280 or mysnake.head.ycor()>310:
        running = False
        score.game_over()
    for segment in mysnake.segments:
        if segment==mysnake.head:
            pass
        elif mysnake.head.distance(segment)<10:
            running = False
            score.game_over()
            
    
   
    
        
screen.exitonclick()