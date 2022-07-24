import pygame as pg
from Score import Score
from game_settings import Settings
import sys
from function import *
from Paddle import *
from Ball import *
def main():
    
    clock = pg.time.Clock()
    settings = Settings()
    
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Pong")
    
    score = Score(screen, settings)
    paddle1 = Paddle(settings, screen, settings.paddle1_x_offset, settings.paddle_y_offset_spawn_pos)
    paddle2 = Paddle(settings, screen, settings.paddle2_x_offset, settings.paddle_y_offset_spawn_pos)
    ball = Ball(settings, screen)
    ball.get_direction()
    while True:
        
        check_input_events(screen, paddle1, paddle2, settings)
        paddle_wall_colision_check(paddle1, settings)
        paddle_wall_colision_check(paddle2, settings)
        ball_collision_check_paddle(ball, paddle1, paddle2)
        ball_collision_check_wall(ball, settings)
        ball.update()
        # ball_collision_check_wall(ball, settings)
        # ball_collision_check_paddle(ball, paddle1, paddle2)
        # print("hello")
        draw_obj(paddle1, paddle2, ball)
        clock.tick(144)
        pg.display.flip()
        screen.fill("#000000")
        
        
    
    
if __name__ == '__main__':    
    main()