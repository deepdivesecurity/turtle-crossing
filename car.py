from turtle import Turtle
import random
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

COLORS = ["white", "red", "green", "blue", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(): 
    def __init__(self): 
        self.all_cars = []
        self.create_car()

    def create_car(self): 
        random_chance = random.randint(1,6)
        if random_chance == 1: 
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(SCREEN_WIDTH // 2, random.randrange(-SCREEN_HEIGHT // 2 + 20, SCREEN_HEIGHT // 2, 20))
            new_car.speed = STARTING_MOVE_DISTANCE
            self.all_cars.append(new_car)

    def move(self): 
        for car in self.all_cars: 
            new_x = car.xcor() - car.speed
            car.goto(new_x, car.ycor())

    def increase_speed(self): 
        for car in self.all_cars: 
            car.speed += MOVE_INCREMENT
        