from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

ALIGNMENT = "left"
FONT = ("Arial", 24, "normal")
COLOR = "black"

class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.goto(-SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self): 
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self): 
        self.level += 1
        self.update_scoreboard()

    # def game_over(self): 
    #     self.goto(0, 0)
    #     self.color(COLOR)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)