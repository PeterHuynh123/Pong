import pygame as pg

class Score:
    def __init__(self, screen, game_setting):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.p1_score = 0
        self.p1_score_draw_pos = game_setting.score_paddle1_score_draw_pos
        
        self.p2_score = 0
        self.p2_score_draw_pos = game_setting.score_paddle2_score_draw_pos
        
        self.text_color = (50, 50, 50)
        self.bg_color = (200, 200, 200)
        self.font = pg.font.Font(None, 48)