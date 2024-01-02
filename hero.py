import pygame
from animations import anim_fight, anim_stay, anim_run, user_screen_width, user_screen_height
from constants_for_hero import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, fight_cool_down, *groups, direction='right'):
        super().__init__(*groups)
        self.anim_stay = [pygame.transform.scale(el, (0.09 * user_screen_width, 0.28 * user_screen_height))\
                          for el in anim_stay]
        self.anim_stay_l = [pygame.transform.flip(el, True, False) for el in self.anim_stay]

        self.anim_fight = [pygame.transform.scale(el, (0.17 * user_screen_width, 0.28 * user_screen_height))\
                           for el in anim_fight]
        self.anim_fight_l = [pygame.transform.flip(el, True, False) for el in self.anim_fight]

        self.anim_run = [pygame.transform.scale(el, (0.15 * user_screen_width, 0.28 * user_screen_height))\
                         for el in anim_run]
        self.anim_run_l = [pygame.transform.flip(el, True, False) for el in self.anim_run]

        self.cur_frame_stay = 0
        self.cur_frame_fight = 0
        self.cur_frame_run = 0
        self.is_run = False
        self.is_fight = False
        self.is_jump = False
        self.is_squat = False

        if direction == 'left':
            self.left = True
            self.right = False
        else:
            self.left = False
            self.right = True

        self.image = self.anim_stay[self.cur_frame_stay] if self.right else self.anim_stay_l[self.cur_frame_stay]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.fight_enabled = True

        self.speed = speed

        self.clock = pygame.time.Clock()

        self.fight_cool_down = fight_cool_down
        self.last_fight_time = 0

    def frame_swap(self):
        self.cur_frame_stay = (self.cur_frame_stay + 1) % len(self.anim_stay)
        self.cur_frame_run = (self.cur_frame_run + 1) % len(self.anim_run)
        if self.is_fight:
            self.cur_frame_fight += 1
            if self.cur_frame_fight == len(self.anim_fight):
                self.cur_frame_fight = 0
                self.is_fight = False

    def image_swap(self):
        if self.is_fight:
            self.image = self.anim_fight[self.cur_frame_fight] if self.right\
                else self.anim_fight_l[self.cur_frame_fight]
        elif self.is_jump:
            pass
        elif self.is_squat:
            pass
        elif self.is_run:
            self.image = self.anim_run[self.cur_frame_run] if self.right else self.anim_run_l[self.cur_frame_run]
        else:
            self.image = self.anim_stay[self.cur_frame_stay] if self.right else self.anim_stay_l[self.cur_frame_stay]

    def process_events(self, flags):
        current_time = pygame.time.get_ticks()

        if RUN in flags:
            self.is_run = True
        else:
            self.is_run = False

        # далее непрерываемые процессы
        # if JUMP in flags:
        #     self.is_jump = True
        #
        # if SQUAT in flags:
        #     self.is_squat = True

        # проверка возможности атаки
        if current_time - self.last_fight_time >= self.fight_cool_down:
            self.fight_enabled = True
        if FIGHT in flags and self.fight_enabled:
            self.fight_enabled = False
            self.last_fight_time = current_time
            self.is_fight = True

        # направления
        if LEFT in flags:
            self.left = True
            self.right = False

        if RIGHT in flags:
            self.left = False
            self.right = True

    def move(self):
        if self.is_run:
            if self.left:
                if self.rect.x - self.speed > 0:
                    self.rect = self.rect.move(-self.speed, 0)
                else:
                    self.rect.x = 0
            else:
                if self.rect.x + self.rect.width + self.speed < user_screen_width:
                    self.rect = self.rect.move(self.speed, 0)
                else:
                    self.rect.x = user_screen_width - self.rect.width

    def update(self):
        self.frame_swap()
        self.image_swap()
