class Settings():
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 768
        
        self.paddle1_x_offset = 60
 
        self.paddle_width = 10
        self.paddle_height = 80
        self.paddle_y_offset_spawn_pos = self.screen_height//2 - self.paddle_height//2
        self.paddle2_x_offset = self.screen_width-60-self.paddle_width//2
        self.paddle_speed = 8
        
        self.ball_radius = 8
        self.ball_spawn_x = self.screen_width//2 - 5
        self.ball_spawn_y = self.screen_height//2 - 5
        self.ball_speed = 2
        
        self.score_paddle1_score_draw_pos = 30, 30 
        self.score_paddle2_score_draw_pos = self.screen_width - 30, self.screen_height - 30