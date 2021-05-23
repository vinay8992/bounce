from turtle import Turtle
ALIGN="center"
FONT=("Arial", 24, "bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 360)
        self.write(f"Score {self.lscore}", align=ALIGN, font=FONT)
        self.goto(-100, 360)
        self.write(f"Score {self.rscore}", align=ALIGN, font=FONT)

    def l_point(self):
        self.lscore+=1
        self.update_scoreboard()
    def r_point(self):
        self.rscore+=1
        self.update_scoreboard()

