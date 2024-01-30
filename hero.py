import pygame
from animations import *
from constants_for_hero import *

# Инициализация Pygame
pygame.init()
user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

screen = pygame.display.set_mode((user_screen_width, user_screen_height))  # Задаём разрешение основного окна


class Hero(pygame.sprite.Sprite):
    '''
    Класс персонаж
    '''
    def __init__(self, x, ground, speed, power, throw_back_power, jump_power, fight_cool_down, *groups,
                 direction=RIGHT, character=DED_MAXIM):
        '''
        :param x: координата х левого верхнего угла
        :param ground: у координата земли
        :param speed: скорость персонажа за одну итерацию
        :param power: сила удара
        :param throw_back_power: сила откидывания противника
        :param jump_power: начальная скорость прыжка в пикселях
        :param fight_cool_down: время в миллисекундах, которое игрок не сможет атаковать после использования атаки
        :param enemy_group: группа спрайтов противников
        :param groups: группы спрайтов
        :param direction: направление персонажа. Константа программы constants_for_hero
        '''
        super().__init__(*groups)
        if character == DED_MAXIM:
            self.anim_stay = [pygame.transform.scale(el, (0.09 * user_screen_width, 0.28 * user_screen_height))
                              for el in ded_maxim_stay]
            self.anim_stay_l = [pygame.transform.flip(el, True, False) for el in self.anim_stay]
            self.masks_stay = [pygame.mask.from_surface(im) for im in self.anim_stay]
            self.masks_stay_l = [pygame.mask.from_surface(im) for im in self.anim_stay_l]

            self.anim_fight = [pygame.transform.scale(el, (0.2 * user_screen_width, 0.28 * user_screen_height))
                               for el in ded_maxim_fight]
            self.anim_fight_l = [pygame.transform.flip(el, True, False) for el in self.anim_fight]
            self.masks_fight = [pygame.mask.from_surface(im) for im in self.anim_fight]
            self.masks_fight_l = [pygame.mask.from_surface(im) for im in self.anim_fight_l]

            self.anim_run = [pygame.transform.scale(el, (0.15 * user_screen_width, 0.28 * user_screen_height))
                             for el in ded_maxim_run]
            self.anim_run_l = [pygame.transform.flip(el, True, False) for el in self.anim_run]
            self.masks_run = [pygame.mask.from_surface(im) for im in self.anim_run]
            self.masks_run_l = [pygame.mask.from_surface(im) for im in self.anim_run_l]

            self.anim_jump = [pygame.transform.scale(el, (0.22 * user_screen_width, 0.28 * user_screen_height))
                              for el in ded_maxim_jump]
            self.anim_jump_l = [pygame.transform.flip(el, True, False) for el in self.anim_jump]
            self.masks_jump = [pygame.mask.from_surface(im) for im in self.anim_jump]
            self.masks_jump_l = [pygame.mask.from_surface(im) for im in self.anim_jump_l]

            self.anim_squat = [pygame.transform.scale(el, (0.2 * user_screen_width, 0.28 * user_screen_height))
                               for el in ded_maxim_squat]
            self.anim_squat_l = [pygame.transform.flip(el, True, False) for el in self.anim_squat]
            self.masks_squat = [pygame.mask.from_surface(im) for im in self.anim_squat]
            self.masks_squat_l = [pygame.mask.from_surface(im) for im in self.anim_squat_l]
        elif character == VURDALAK:
            self.anim_stay = [pygame.transform.scale(el, (0.12 * user_screen_width, 0.32 * user_screen_height))
                              for el in vurdalak_stay]
            self.anim_stay_l = [pygame.transform.flip(el, True, False) for el in self.anim_stay]
            self.masks_stay = [pygame.mask.from_surface(im) for im in self.anim_stay]
            self.masks_stay_l = [pygame.mask.from_surface(im) for im in self.anim_stay_l]

            self.anim_fight = [pygame.transform.scale(el, (0.12 * user_screen_width, 0.35 * user_screen_height))
                               for el in vurdalak_fight]
            self.anim_fight_l = [pygame.transform.flip(el, True, False) for el in self.anim_fight]
            self.masks_fight = [pygame.mask.from_surface(im) for im in self.anim_fight]
            self.masks_fight_l = [pygame.mask.from_surface(im) for im in self.anim_fight_l]

            self.anim_run = [pygame.transform.scale(el, (0.14 * user_screen_width, 0.32 * user_screen_height))
                             for el in vurdalak_run]
            self.anim_run_l = [pygame.transform.flip(el, True, False) for el in self.anim_run]
            self.masks_run = [pygame.mask.from_surface(im) for im in self.anim_run]
            self.masks_run_l = [pygame.mask.from_surface(im) for im in self.anim_run_l]

            self.anim_jump = [pygame.transform.scale(el, (0.16 * user_screen_width, 0.26 * user_screen_height))
                              for el in vurdalak_jump]
            self.anim_jump_l = [pygame.transform.flip(el, True, False) for el in self.anim_jump]
            self.masks_jump = [pygame.mask.from_surface(im) for im in self.anim_jump]
            self.masks_jump_l = [pygame.mask.from_surface(im) for im in self.anim_jump_l]

            self.anim_squat = [pygame.transform.scale(el, (0.2 * user_screen_width, 0.28 * user_screen_height))
                               for el in vurdalak_squat]
            self.anim_squat_l = [pygame.transform.flip(el, True, False) for el in self.anim_squat]
            self.masks_squat = [pygame.mask.from_surface(im) for im in self.anim_squat]
            self.masks_squat_l = [pygame.mask.from_surface(im) for im in self.anim_squat_l]

        self.is_enemy_hit = False  # флаг для того, чтобы нельзя было одним ударом нанести урон несколько раз
        self.hiten = 0  # флаг был ли ударен персонаж для кратковременной смены цвета.
        # Численно равен количеству перекрашенных кадров анимации

        self.cur_frame_stay = 0
        self.cur_frame_fight = 0
        self.cur_frame_run = 0
        self.cur_frame_jump = 0
        self.cur_frame_squat = 0

        self.is_run = False
        self.is_fight = False
        self.is_jump = False
        self.is_squat = False

        if direction == LEFT:
            self.left = True
            self.right = False
        else:
            self.left = False
            self.right = True

        self.image = self.anim_stay[self.cur_frame_stay] if self.right else self.anim_stay_l[self.cur_frame_stay]
        self.mask = self.masks_stay[self.cur_frame_stay] if self.right else self.masks_stay_l[self.cur_frame_stay]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, ground - self.rect.height
        self.ground = ground

        self.fight_enabled = True

        self.speed = speed
        self.power = power
        self.jump_power = jump_power
        self.throw_back_power = throw_back_power

        self.jump_speed = 0
        self.jump_enable = True

        self.fight_cool_down = fight_cool_down
        self.last_fight_time = 0

    def set_enemy(self, enemy, health_dict):
        '''
        Назначить врага персонажа
        :param enemy: враг, объект pygame.Sprite
        :return:
        '''
        self.enemy = enemy
        self.health_dict = health_dict

    def hit(self, n_frames):
        '''
        Назначить количество кадров анимации, которое персонаж будет перекрашен
        :param n_frames: количество кадров
        :return:
        '''
        self.hiten = n_frames

    def move_back(self, n_pix):
        '''
        Метод откидывает персонажа
        :param n_pix: количество пикселей по х
        :return:
        '''
        self.rect = self.rect.move(n_pix, 0)

    def frame_swap(self):
        '''
        Метод, который сменяет счетчики анимаций
        :return:
        '''
        self.cur_frame_stay = (self.cur_frame_stay + 1) % len(self.anim_stay)
        self.cur_frame_run = (self.cur_frame_run + 1) % len(self.anim_run)
        if self.is_fight:
            self.cur_frame_fight += 1
            if self.cur_frame_fight == len(self.anim_fight):
                self.cur_frame_fight = 0
                self.is_fight = False
        if self.is_jump:
            self.cur_frame_jump += 1
            if self.cur_frame_jump == len(self.anim_jump):
                self.cur_frame_jump = 0
        if self.is_squat:
            self.cur_frame_squat += 1
            if self.cur_frame_squat == len(self.anim_squat):
                self.cur_frame_squat = 0
                self.is_squat = False

        if self.hiten:
            self.image = self.image.copy()
            self.image.set_alpha(200)
            self.hiten -= 1

    def image_swap(self):
        '''
        Метод присваивает спрайту картинку и маску в зависимости от счетччика анимаций и флагов состояния персонажа
        :return:
        '''
        # размеры предыдущей картинки для того, чтобы отцентрировать по ширине и оставить низ на той же высоте у новой
        last_image_width = self.image.get_width()
        last_image_height = self.image.get_height()
        if self.is_fight:
            self.image = self.anim_fight[self.cur_frame_fight] if self.right\
                else self.anim_fight_l[self.cur_frame_fight]
            self.mask = self.masks_fight[self.cur_frame_fight] if self.right\
                else self.masks_fight_l[self.cur_frame_fight]
        elif self.is_jump:
            self.image = self.anim_jump[self.cur_frame_jump] if self.right\
                else self.anim_jump_l[self.cur_frame_jump]
            self.mask = self.masks_jump[self.cur_frame_jump] if self.right \
                else self.masks_jump_l[self.cur_frame_jump]
        elif self.is_squat:
            self.image = self.anim_squat[self.cur_frame_squat] if self.right \
                else self.anim_squat_l[self.cur_frame_squat]
            self.mask = self.masks_squat[self.cur_frame_squat] if self.right \
                else self.masks_squat_l[self.cur_frame_squat]
        elif self.is_run:
            self.image = self.anim_run[self.cur_frame_run] if self.right else self.anim_run_l[self.cur_frame_run]
            self.mask = self.masks_run[self.cur_frame_run] if self.right \
                else self.masks_run_l[self.cur_frame_run]
        else:
            self.image = self.anim_stay[self.cur_frame_stay] if self.right else self.anim_stay_l[self.cur_frame_stay]
            self.mask = self.masks_stay[self.cur_frame_stay] if self.right \
                else self.masks_stay_l[self.cur_frame_stay]

        new_image_width = self.image.get_width()
        new_image_height = self.image.get_height()

        # выравниваем новый кадр анимации
        self.rect = self.rect.move((last_image_width - new_image_width) / 2, 0)

    def process_events(self, flags):
        '''
        Метод для обработки событий
        :param flags: список из констант, содержащихся в программе constants_for_hero
        :return:
        '''
        current_time = pygame.time.get_ticks()

        if RUN in flags:
            self.is_run = True
        else:
            self.is_run = False

        # далее непрерываемые процессы
        if JUMP in flags and not self.is_squat:
            self.is_jump = True

        if SQUAT in flags:
            self.is_squat = True

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
        '''
        Метод для передвижения персонажа в зависимости от флагов состояния а так же для обработки ударов
        :return:
        '''
        global screen
        if self.is_run:
            if self.left:
                if self.rect.x - self.speed > 0:
                    self.rect = self.rect.move(-self.speed, 0)
                else:
                    self.rect.x = 0
            else:
                if self.rect.x + self.image.get_width() + self.speed < user_screen_width:
                    self.rect = self.rect.move(self.speed, 0)
                else:
                    self.rect.x = user_screen_width - self.image.get_width()
        if self.is_jump:
            if self.jump_enable:
                self.jump_speed = -self.jump_power
                self.jump_enable = False

            if self.rect.y + self.rect.height + self.jump_speed < self.ground:
                self.rect = self.rect.move(0, self.jump_speed)
                self.jump_speed += 1
            else:
                self.rect.y = self.ground - self.rect.height

            if self.rect.y + self.rect.height == self.ground:
                self.jump_speed = 0
                self.jump_enable = True
                self.is_jump = False
                self.cur_frame_jump = 0
        if self.is_fight:
            if not self.is_enemy_hit and pygame.sprite.collide_mask(self, self.enemy)\
                    and (self.rect.x <= self.enemy.rect.x if self.right else self.rect.x >= self.enemy.rect.x)\
                    and (int(self.rect.y + self.rect.height / 2) in
                         range(int(self.enemy.rect.y), int(self.enemy.rect.y + self.enemy.rect.height))):
                self.is_enemy_hit = True
                self.enemy.hit(5)
                self.enemy.move_back(self.throw_back_power if self.right else -self.throw_back_power)
                pygame.mixer.init()
                sound_2 = pygame.mixer.Sound("slap.mp3")
                sound_2.play()
                self.health_dict[self.enemy] -= self.power
        else:
            self.is_enemy_hit = False

    def update(self):
        '''
        Обновление
        Метод запускает смену счетчика анимаций, а так же присваивание нужной картинки
        :return:
        '''
        self.image_swap()
        self.frame_swap()
