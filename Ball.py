import pygame as pg
import random

class Ball:
    def __init__(self, settings, screen):
        self.x = settings.ball_spawn_x
        self.y = settings.ball_spawn_y
        self.radius = settings.ball_radius
        self.diameter = self.radius*2
        self.screen = screen
        self.speed = settings.ball_speed
        self.direction_x = 0
        self.direction_y = 0
        
    def draw(self):
        pg.draw.circle(self.screen, (255, 255, 255), [self.x, self.y], self.radius)
        
    def get_direction(self):
        while self.direction_x == 0 or self.direction_y == 0:
            self.direction_x = random.randint(-1,1)
            self.direction_y = random.randint(-1,1)
        
    def update(self):
        # if self.direction_x > 4:
        #     self.direction_x = 4
        # if self.direction_y > 4:
        #     self.direction_y = 4
        # if self.direction_x < -4:
        #     self.direction_x = -4
        # if self.direction_y < -4:
        #     self.direction_y = -4
        self.x += self.speed*self.direction_x
        self.y += self.speed*self.direction_y
        pg.draw.circle(self.screen, (255, 255, 255), [self.x, self.y], self.radius)