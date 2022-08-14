from re import L
from pygame import mixer

class Sound():
    def __init__(self):
        mixer.pre_init(22050, -16, 1, 64)
        mixer.init()
        self.ball_hit1 = mixer.Sound('./wav/ball_hit1.wav')
        self.ball_hit1.set_volume(0.08)
        self.ball_hit2 = mixer.Sound('./wav/ball_hit2.wav')
        self.ball_hit2.set_volume(0.08)
        self.ball_hit3 = mixer.Sound('./wav/ball_hit3.wav')
        self.ball_hit3.set_volume(0.08)
        self.ball_hit4 = mixer.Sound('./wav/ball_hit4.wav')
        self.ball_hit4.set_volume(0.08)
        
        self.collision_sound_list = [self.ball_hit1, self.ball_hit2, self.ball_hit3, self.ball_hit4]