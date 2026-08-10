from turtle import Screen, Turtle
from car import Car
from scoreboard import Scoreboard
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import time

def main(): 
    screen = Screen()
    screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Turtle Crossing")
    screen.tracer(0)

    scoreboard = Scoreboard()

    player = Player()
    car = Car()

    screen.listen()
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")

    game_on = True
    while game_on: 
        time.sleep(0.1)
        # car.move()
        screen.update()

        # Check if turtle made it to the other side
        

        # Check for collision with a car
        if car.distance(player) < 20: 
            pass            

        
    screen.exitonclick()

if __name__ == "__main__":
    main()