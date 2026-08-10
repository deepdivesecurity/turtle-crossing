from turtle import Screen
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

    game_on = True
    while game_on: 
        time.sleep(0.1)
        car.move()
        screen.update()

        # Check if turtle made it to the other side
        if player.ycor() > SCREEN_HEIGHT // 2 - 20: 
            # Reset game, increase level, and increase speed of cars
            player.reset()
            car.increase_speed()
            scoreboard.increase_level()

        # Check for collision with a car
        if car.distance(player) < 35: 
            scoreboard.game_over()
            game_on = False
        
    screen.exitonclick()

if __name__ == "__main__":
    main()