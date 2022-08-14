import pygame as pg

class Score:
    def __init__(self, screen, game_setting):
        self.screen = screen
        
        self.offset = game_setting.score_offset
        
        self.p1_score = 0
        self.p2_score = 0

        
        self.text_color = (50, 50, 50)
        self.bg_color = (200, 200, 200)
        self.font = pg.font.Font(None, 48)
        
        self.render_p1_score()
        self.render_p2_score()
        
    def draw(self):
        self.screen.blit(self.rendered_p1_score, self.rendered_p1_score_rect)
        self.screen.blit(self.rendered_p2_score, self.rendered_p2_score_rect)       
        
    def render_p1_score(self):
        self.rendered_p1_score = self.font.render(str(self.p1_score), True, self.text_color, self.bg_color)
        self.rendered_p1_score_rect = self.rendered_p1_score.get_rect()
        self.rendered_p1_score_rect.left = self.offset
        self.rendered_p1_score_rect.top = self.offset
        
    def render_p2_score(self):
        self.rendered_p2_score = self.font.render(str(self.p2_score), True, self.text_color, self.bg_color)
        self.rendered_p2_score_rect = self.rendered_p2_score.get_rect()
        self.rendered_p2_score_rect.right = self.screen.get_width() - self.offset
        self.rendered_p2_score_rect.top = self.offset
    
    def update(self):
        self.render_p1_score()
        self.render_p2_score()
        self.draw()