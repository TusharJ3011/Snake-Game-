from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.score_board = Turtle()
        self.score_board.hideturtle()
        self.score_board.penup()
        self.score_board.color('white')
        self.score_board.sety(280)

    def update(self):
        read_hscore = open('high_score.txt')
        h_score = read_hscore.read()
        read_hscore.close()
        self.score_board.clear()
        self.score_board.write(arg=f'Score: {self.score}, High Score: {h_score}', move=False, align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.score_board.sety(0)
        self.score_board.clear()
        self.score_board.write(arg='Game Over', move=False, align="center", font=("Arial", 24, "normal"))
        self.score_board.sety(-30)
        self.score_board.write(arg=f'\nScore: {self.score}', move=False, align="center", font=("Arial", 24, "normal"))

    def high_score(self):
        read_hscore = open('high_score.txt')
        h_score = read_hscore.read()
        read_hscore.close()
        h_score = int(h_score)
        if self.score > h_score:
            write_hscore = open('high_score.txt', mode='w')
            score_new = str(self.score)
            write_hscore.write(score_new)
            write_hscore.close()


