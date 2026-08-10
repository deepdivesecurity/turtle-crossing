from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self): 
        super().__init__()
        self.create_player()

    def create_player(self): 
        self.shape("turtle")
        self.color("white")
        self.right(270)
        self.penup()
        self.goto(0, -SCREEN_HEIGHT / 2 - 20)

    def up(self): 
        self.goto(self.xcor(), self.ycor() + 10)
