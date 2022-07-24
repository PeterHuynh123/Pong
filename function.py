import random
import pygame as pg
import sys

def check_input_events(screen, paddle1, paddle2, settings):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        # print('a')
    keys_pressed = pg.key.get_pressed()
    
    if keys_pressed[pg.K_DOWN]:
        paddle_movement(paddle2, 1)
    if keys_pressed[pg.K_UP]:
        paddle_movement(paddle2, -1)
    if keys_pressed[pg.K_w]:
        paddle_movement(paddle1, -1)
    if keys_pressed[pg.K_s]:
        paddle_movement(paddle1, 1)
    if keys_pressed[pg.K_SPACE]:
        reset_ball(settings)

def reset_ball(ball, settings):
    ball.get_direction()
    ball.x = settings.ball_spawn_x
    ball.y = settings.ball_spawn_y
    ball.update()
    
def paddle_movement(paddle, direction):
    paddle.y += paddle.speed*direction
    paddle.rect.y = paddle.y
    
def paddle_wall_colision_check(paddle, settings):
    if paddle.y < 0:
        paddle.y = 0
        paddle.rect.y = paddle.y
    if paddle.y > settings.screen_height - paddle.height:
        paddle.y = settings.screen_height - paddle.height
        paddle.rect.y = paddle.y
    
def draw_obj(paddle1, paddle2, ball):
    paddle1.draw()
    paddle2.draw()
    ball.draw()
    
def ball_collision_check_wall(ball, settings):
    if ball.x < 0 or ball.x + ball.radius > settings.screen_width:
        ball.direction_x = -ball.direction_x
        # ball.direction_y += random.randint(-15, 15)//40
    if ball.y < 0 or ball.y + ball.radius > settings.screen_height:
        print(ball.direction_y)
        ball.direction_y = -ball.direction_y
        # ball.direction_x += random.randint(-15, 1/5)//40
        
def ball_collision_check_paddle(ball, paddle1, paddle2):
    if (ball.x < paddle1.x + paddle1.width) and (ball.x + ball.radius > paddle1.x) and (ball.y < paddle1.y + paddle1.height) and (ball.y + ball.radius > paddle1.y):
        ball.direction_x = -ball.direction_x
        # print("collision detected")
        # ball.direction_y += random.randint(-45, 45)//300
    
    if (ball.x < paddle2.x + paddle2.width) and (ball.x + ball.radius > paddle2.x) and (ball.y < paddle2.y + paddle2.height) and (ball.y + ball.radius > paddle2.y):
        # print("collision detected")
        ball.direction_x = -ball.direction_x
        # ball.direction_y += random.randint(-45, 45)//300
    
    # if(ball.x < settings.screen_width 
    #    or ball.x + ball.radius*2 > settings.screen_width
    #    or ball.y < settings.screen_height 
    #    or ball.y + ball.radius*2 > settings.screen_height):
    #     ball.direction_x = -ball.direction_x
    #     ball.direction_y = -ball.direction_y