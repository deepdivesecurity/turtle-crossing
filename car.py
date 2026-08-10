from turtle import Turtle
import random

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

    # def move(self): 
    #     new_x = self.xcor() + self.x_move
    #     new_y = self.ycor() + self.y_move
    #     self.goto(new_x, new_y)

    # def bounce_x(self): 
    #     self.x_move *= -1

    # def bounce_y(self): 
    #     self.y_move *= -1

    # def reset(self): 
    #     self.penup()
    #     self.goto(0,0)
    #     self.move()
        