from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(0, 250)
        self.write(arg=f"{self.player_1_score} : {self.player_2_score}", align="center", font=("Arial", 40, "normal"))

    def increase_score(self, player_who_scored):
        if player_who_scored == "p1":
            self.player_1_score += 1
        else:
            self.player_2_score += 1
        self.write(arg=f"{self.player_1_score} : {self.player_2_score}", align="center", font=("Arial", 40, "normal"))

    def check_win(self):
        player = 0
        if self.player_1_score == 11:
            if self.player_2_score < 11:
                player = 2
        elif self.player_2_score == 11:
            if self.player_1_score < 11:
                player = 1
        if player != 0:
            self.hideturtle()
            self.color("white")
            self.penup()
            self.setposition(0, 0)
            self.write(arg=f"Player {player} is the winner!", align="center",
                       font=("Arial", 30, "normal"))
