from turtle import Turtle
import random
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

COLORS = ["white", "red", "green", "blue", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle): 
    def __init__(self): 
        super().__init__()
        self.create_car()

    def create_car(self): 
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.goto(SCREEN_WIDTH // 2, random.randrange(-SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2, 20))
        self.speed = STARTING_MOVE_DISTANCE

    def move(self): 
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())

    def increase_speed(self): 
        self.speed += MOVE_INCREMENT
        