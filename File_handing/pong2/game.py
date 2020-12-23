# main.py
# !/bin/env python3


#game.py
import random




# game.py
import random


class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.__ball_pos = (0, 0)
        self.__ball_delta_x = 1
        self.__ball_delta_y = 1

        self.paddle_a_pos = (-self.width / 2 + 50, 0)
        self.paddle_b_pos = (self.width / 2 - 50, 0)

        self.paddle_height = self.height * 0.25
        self.paddle_width = 20

        self.points_a = 0
        self.points_b = 0

        self.game_over = False

    def tick(self):
        if self.points_a >= 5 or self.points_b >= 5:
            self.game_over = True
            return
        self.__perform_border_checking()
        self.__perform_paddle_hit_checking()
        x, y = self.__ball_pos
        self.__ball_pos = (x + self.__ball_delta_x, y + self.__ball_delta_y)

    def __perform_border_checking(self):
        x, y = self.__ball_pos
        if abs(y) >= (self.height / 2):
            self.__ball_delta_y *= -1

        if x <= -(self.width / 2):
            self.points_b += 1
            self.__ball_pos = (0, 0)
            self.__ball_delta_x *= random.choice([-1, 1])

        if x >= (self.width / 2):
            self.points_a += 1
            self.__ball_pos = (0, 0)
            self.__ball_delta_x *= random.choice([-1, 1])

    def __perform_paddle_hit_checking(self):
        x, y = self.__ball_pos

        a_x, a_y = self.paddle_a_pos
        hit_paddle_a = (a_x + self.paddle_width) == x and (
                    (a_y - self.paddle_height / 2) <= y <= (a_y + self.paddle_height / 2))

        b_x, b_y = self.paddle_b_pos
        hit_paddle_b = (b_x - self.paddle_width) == x and (
                    (b_y - self.paddle_height / 2) <= y <= (b_y + self.paddle_height / 2))

        if hit_paddle_a or hit_paddle_b:
            self.__ball_delta_x *= -1

    def ball_pos(self):
        return self.__ball_pos

    def paddle_a_up(self):
        x, y = self.paddle_a_pos
        if (y + 40) < (self.height / 2):
            self.paddle_a_pos = (x, y + 40)

    def paddle_a_down(self):
        x, y = self.paddle_a_pos
        if (y - 40) > -(self.height / 2):
            self.paddle_a_pos = (x, y - 40)

    def paddle_b_up(self):
        x, y = self.paddle_b_pos
        if (y + 40) < (self.height / 2):
            self.paddle_b_pos = (x, y + 40)

    def paddle_b_down(self):
        x, y = self.paddle_b_pos
        if (y - 40) > -(self.height / 2):
            self.paddle_b_pos = (x, y - 40)
