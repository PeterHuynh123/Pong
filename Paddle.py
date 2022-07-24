import pygame as pg 

class Paddle():
    def __init__(self, settings, screen, x, y):
        self.width = settings.paddle_width
        self.height = settings.paddle_height
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.color = "#ffffff"
        
        self.speed = settings.paddle_speed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.screen = screen
        
    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)