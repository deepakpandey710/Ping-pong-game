from turtle import Turtle


class Ball(Turtle):

    def _init_(self):
        super()._init_()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 0.12
        self.y_move = 0.12
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.01

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.01

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()