from turtle import Turtle

FONT = ("Courier", 24, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.penup()
        self.goto(0, 260)
        self.user_score = 0
        self.write(f"Score: {self.user_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

    def points_to_score(self):
        self.user_score += 1
        if self.user_score > self.high_score:
            self.high_score = self.user_score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
        self.write(f"Score: {self.user_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)





