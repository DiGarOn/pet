from __future__ import annotations
# from Food import Food
from Window import Window
import random
import pygame

# from Food import Food


green = (0, 255, 0)


class Snake:
    def __init__(self, w: Window):
        self.data = [w.size_x/2, w.size_y/2]
        self.block_size = 10
        self.speed = 15
        self.size = 1
        self.direction = 'left'

    def check_callaps(self, w: Window):
        if (self.data[0][1] >= w.size_y) or (self.data[0][0] >= w.size_x) or (self.data[0][1] <= 0) or (self.data[0][0] <= 0):
            return True
        for i in range(1, self.size):
            if self.data[0][0] == self.data[i][0] and self.data[0][1] == self.data[i][1]:
                return True
        return False

    def check_eat(self, food: Food, w: Window):
        if self.data[0][0] == food.foodx and self.data[0][1] == food.foody:
            self.size += 1
            food.update(w)

    def move(self):
        if len(self.data) != self.size:
            self.data.append([])

        for i in range(self.size-1, 0, -1):
            self.data[i] = self.data[i-1]
        if self.direction == 'left':
            self.data[0][0] -= self.speed
        elif self.direction == 'right':
            self.data[0][0] += self.speed
        elif self.direction == 'up':
            self.data[0][1] += self.speed
        elif self.direction == 'down':
            self.data[0][1] -= self.speed

    def change_direction(self, new_direction):
        if new_direction in ['left', 'right', 'up', 'down']:
            self.direction = new_direction


class Food:
    def __init__(self, w: Window, s: Snake):
        self.foodx = round(random.randrange(0, w.size_x - s.block_size) / 10.0) * 10.0
        self.foody = round(random.randrange(0, w.size_y - s.block_size) / 10.0) * 10.0
        self.size = s.block_size

    def draw(self, w: Window):
        pygame.draw.rect(w.dis, green, [self.foodx, self.foody, self.size, self.size])

    def update(self, w: Window):
        self.foodx = round(random.randrange(0, w.size_x - self.size) / 10.0) * 10.0
        self.foody = round(random.randrange(0, w.size_y - self.size) / 10.0) * 10.0