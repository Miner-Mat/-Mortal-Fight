import pygame  # импортируем pygame как игровой движок
import asyncio  # импортируем asyncio для создания асинхронности
import os  # импортируем os для работы с файлами
from moviepy.editor import VideoFileClip  # импортируем нужную функцию из moviepy для создания видеозаставки
from healthbars import Healthbars  # Импортируем класс Healthbars
from constants_for_hero import *  # Импортируем все константы персонажей
from hero import Hero  # импортируем класс Hero
from buttons_and_texts import *

# Инициализация Pygame
pygame.init()

# Собираем информацию о разрешении экрана пользователя
user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

screen = pygame.display.set_mode((user_screen_width, user_screen_height))  # Задаём разрешение основного окна
pygame.display.set_caption("Mortal Fight")  # Задаём название программе
icon = pygame.image.load("logo.jpg")  # Загружаем логотип
pygame.display.set_icon(icon)  # Выставляем логотип

video_clip = VideoFileClip("заставка.mp4")  # Загрузка видезаставки

# меняем размер в зависимости от экрана
# video_clip = video_clip.resize(height=user_screen_height, width=user_screen_width)
video_length = video_clip.duration  # продолжительность видео в секундах

pygame.mixer.init()  # инициализируем функцию добавления музыки

# константы для отслеживания текущего окна
MENU_WINDOW = 0
FIGHT_WINDOW = 1

ground = int(0.94 * user_screen_height)

# Определяющие положение персонажа переменные
x, y = 0.08 * user_screen_width, 0.66 * user_screen_height
speed = 0.015 * user_screen_height
power = 30
throw_back_power = 40
jump_power = 20

# Определяющие положение второго персонажа переменные
x2, y2 = 0.8 * user_screen_width, 0.66 * user_screen_height
speed2 = 0.015 * user_screen_height
power2 = 30
throw_back_power2 = 40
jump_power2 = 20

# Значения хэлф баров
health_1 = 100
health_2 = 100

ch_win_flag = False  # Флаг, означсающий что один из игроков победил
pause_flag = False  # Флаг, означающий что игра находится на паузе

health = Healthbars(user_screen_width, user_screen_height)  # Объявляем класс хэлфбаров


# Функция для воспроизведения видеозаставки
async def play_video(clip):
    start_time = pygame.time.get_ticks()
    clip_audio = clip.audio.set_fps(44100)
    clip.audio.write_audiofile("temp_audio.wav")
    pygame.mixer.music.load('temp_audio.wav')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        elapsed = (pygame.time.get_ticks() - start_time) / 1000.0
        if elapsed > video_length:
            break
        frame = clip.get_frame(elapsed)
        surf = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(surf, (0, 0))
        pygame.display.flip()
        pygame.time.wait(int(1000 / clip.fps))
        await asyncio.sleep(0)  # Позволяет другим задачам выполниться

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    if os.path.exists('temp_audio.wav'):
        os.remove('temp_audio.wav')


# Создание асинхронной функции для вызова воспроизведения заставки
async def main():
    video_clip = VideoFileClip("заставка.mp4")  # Загрузка видеоклипа
    await play_video(video_clip)  # Вызов функции воспроизведения заставки

# Создание и запуск цикла событий asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

pygame.mixer.music.load("menu_music.mp3")  # Загружаем музыку
pygame.mixer.music.set_volume(0.2)  # Выставляем громкость
pygame.mixer.music.play(-1)  # Запускаем бесконечный цикл проигрывания

sound = pygame.mixer.Sound("turn.mp3")
sound_2 = pygame.mixer.Sound("slap.mp3")


def key_check():  # Проверка нажатий
    '''
    Функция для проверки нажатий на клавиши и их обработки
    :return:
    '''
    keys = pygame.key.get_pressed()
    res1 = []  # списки с флагами, которые передадим в классы персонажей
    res2 = []
    if not ch_win_flag and not pause_flag:
        if keys[pygame.K_a]:
            res1.append(LEFT)
            res1.append(RUN)
        if keys[pygame.K_d]:
            res1.append(RIGHT)
            res1.append(RUN)
        if keys[pygame.K_w]:
            res1.append(JUMP)
        if keys[pygame.K_s]:
            res1.append(SQUAT)
        if keys[pygame.K_f]:
            res1.append(FIGHT)

        if keys[pygame.K_j]:
            res2.append(LEFT)
            res2.append(RUN)
        if keys[pygame.K_l]:
            res2.append(RIGHT)
            res2.append(RUN)
        if keys[pygame.K_i]:
            res2.append(JUMP)
        if keys[pygame.K_k]:
            res2.append(SQUAT)
        if keys[pygame.K_h]:
            res2.append(FIGHT)

        hero1.process_events(res1)
        hero2.process_events(res2)

        hero1.move()
        hero2.move()


animation_delay = 100
UPDATE_FRAMES = pygame.USEREVENT + 1  # создаём событие для обновления кадров и присваиваем ему номер
pygame.time.set_timer(UPDATE_FRAMES, animation_delay)

health.health_on_all_arenas(arens)  # рисует хелф бары на всех аренах для отображения в меню

flag = MENU_WINDOW

running = True  # флаг работы
sound_flag = True  # флаг нынешнего состояния звука

control_button_presed = False

clock = pygame.time.Clock()

while running:
    clock.tick(60)  # обновление экрана 60 раз в секунду

    if flag == MENU_WINDOW:
        arena = pygame.transform.scale(arens[arenas_count], (0.25 * user_screen_width, 0.3 * user_screen_height))
        character_choice = pygame.transform.scale(characters[character1_count],
                                                  (0.09 * user_screen_width, 0.3 * user_screen_height))
        character2_choice = pygame.transform.scale(characters[character2_count],
                                                   (0.09 * user_screen_width, 0.3 * user_screen_height))
        screen.fill((192, 6, 13))
        screen.blit(text_surface, ((user_screen_width - text_surface.get_width()) / 2, 0.04 * user_screen_height))
        pygame.draw.rect(screen, (170, 0, 0), play_button)
        screen.blit(play_text, play_text_rect)
        pygame.draw.rect(screen, (170, 0, 0), exit_button)
        screen.blit(exit_text, exit_text_rect)
        pygame.draw.rect(screen, (170, 0, 0), aren_window)
        screen.blit(arena, arena_rect)
        screen.blit(arena_text, (0.2 * user_screen_width, 0.46 * user_screen_height))
        screen.blit(left_strelka, left_strelka_rect)
        screen.blit(right_strelka, right_strelka_rect)
        screen.blit(character_choice, character_choice_rect)
        screen.blit(left_strelka_ch1, left_strelka_ch1_rect)
        screen.blit(right_strelka_ch1, right_strelka_ch1_rect)
        screen.blit(character2_choice, character2_choice_rect)
        screen.blit(left_strelka_ch2, left_strelka_ch2_rect)
        screen.blit(right_strelka_ch2, right_strelka_ch2_rect)
        screen.blit(ch1_choice_text, (0.6 * user_screen_width, 0.54 * user_screen_height))
        screen.blit(ch2_choice_text, (0.8 * user_screen_width, 0.54 * user_screen_height))
        screen.blit(control_image, control_rect)
        if sound_flag:
            screen.blit(sound_on, sound_on_rect)
        else:
            screen.blit(sound_off, sound_off_rect)

        if control_button_presed:
            screen.blit(control_layout, control_layout_rect)

    elif flag == FIGHT_WINDOW:
        screen.blit(arens[arenas_count], (0, 0))  # отрисовываем фон
        health.draw(screen, health_dict[hero1], health_dict[hero2])
        pygame.draw.rect(screen, (170, 0, 0), back_button)
        screen.blit(back_image, back_image_rect)
        screen.blit(ch1_text, (0.02 * user_screen_width, 0.05 * user_screen_height))
        screen.blit(ch2_text, (0.8 * user_screen_width, 0.05 * user_screen_height))
        if not pause_flag:
            screen.blit(pause_image, pause_image_rect)
        else:
            screen.blit(play_image, play_image_rect)
        key_check()  # вызываем проверку нажатий

        heroes.draw(screen)

        if health_dict[hero1] <= 0:
            screen.blit(ch2_win_text, (0.25 * user_screen_width, 0.46 * user_screen_height))
            ch_win_flag = True
            pygame.draw.rect(screen, (170, 0, 0), restart_button)
            screen.blit(restart_image, restart_image_rect)

            # запускаем анимацию смерти
            hero1.process_events([DEAD])
        elif health_dict[hero2] <= 0:
            screen.blit(ch1_win_text, (0.25 * user_screen_width, 0.46 * user_screen_height))
            ch_win_flag = True
            pygame.draw.rect(screen, (170, 0, 0), restart_button)
            screen.blit(restart_image, restart_image_rect)

            # запускаем анимацию смерти
            hero2.process_events([DEAD])

    pygame.display.update()  # обновляем окно

    # Скрипт выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                sound.play()
                flag = FIGHT_WINDOW
                pygame.mixer.music.load("music.mp3")  # Загружаем музыку
                if sound_flag:
                    pygame.mixer.music.set_volume(0.2)
                else:
                    pygame.mixer.music.set_volume(0)
                pygame.mixer.music.play(-1)  # Запускаем бесконечный цикл проигрывания

                # создаем персонажей
                heroes = pygame.sprite.Group()

                hero1 = Hero(x, ground, speed, power, throw_back_power, jump_power, 1000, heroes, direction=RIGHT,
                             character=ALL_CHARACTERS[character1_count])
                hero2 = Hero(x2, ground, speed2, power2, throw_back_power2, jump_power2, 1000, heroes, direction=LEFT,
                             character=ALL_CHARACTERS[character2_count])

                health_dict = {hero1: health_1, hero2: health_2}

                hero1.set_enemy(hero2, health_dict)
                hero2.set_enemy(hero1, health_dict)

            elif left_strelka_rect.collidepoint(event.pos):
                sound.play()
                arenas_count -= 1
                if arenas_count < 0:
                    arenas_count = len(arens) - 1
            elif right_strelka_rect.collidepoint(event.pos):
                sound.play()
                arenas_count += 1
                if arenas_count >= len(arens):
                    arenas_count = 0
            elif left_strelka_ch1_rect.collidepoint(event.pos):
                sound.play()
                character1_count -= 1
                if character1_count < 0:
                    character1_count = len(characters) - 1
            elif right_strelka_ch1_rect.collidepoint(event.pos):
                sound.play()
                character1_count += 1
                if character1_count >= len(characters):
                    character1_count = 0
            elif left_strelka_ch2_rect.collidepoint(event.pos):
                sound.play()
                character2_count -= 1
                if character2_count < 0:
                    character2_count = len(characters) - 1
            elif right_strelka_ch2_rect.collidepoint(event.pos):
                sound.play()
                character2_count += 1
                if character2_count >= len(characters):
                    character2_count = 0
            elif sound_on_rect.collidepoint(event.pos) or sound_off_rect.collidepoint(event.pos):
                sound.play()
                sound_flag = not sound_flag  # Переключаем звук на противоположное состояние
                if sound_flag:
                    pygame.mixer.music.set_volume(0.2)
                else:
                    pygame.mixer.music.set_volume(0)
            elif restart_button.collidepoint(event.pos):
                sound.play()
                ch_win_flag = False
                x, y = 0.08 * user_screen_width, 0.66 * user_screen_height
                speed = 0.015 * user_screen_height
                power = 30
                jump_power = 20
                x2, y2 = 0.8 * user_screen_width, 0.66 * user_screen_height
                speed2 = 0.015 * user_screen_height
                power2 = 30
                jump_power2 = 20

                # создаем персонажей
                heroes = pygame.sprite.Group()

                hero1 = Hero(x, ground, speed, power, throw_back_power, jump_power, 1000, heroes, direction=RIGHT,
                             character=ALL_CHARACTERS[character1_count])
                hero2 = Hero(x2, ground, speed2, power2, throw_back_power2, jump_power2, 1000, heroes, direction=LEFT,
                             character=ALL_CHARACTERS[character2_count])

                health_dict = {hero1: health_1, hero2: health_2}

                hero1.set_enemy(hero2, health_dict)
                hero2.set_enemy(hero1, health_dict)
            elif control_rect.collidepoint(event.pos):
                control_button_presed = True
                sound.play()
            elif pause_image_rect.collidepoint(event.pos) or play_image_rect.collidepoint(event.pos):
                sound.play()
                pause_flag = not pause_flag
            elif back_button.collidepoint(event.pos):
                pause_flag = False
                sound.play()
                pygame.mixer.music.load("menu_music.mp3")  # Загружаем музыку
                if sound_flag:
                    pygame.mixer.music.set_volume(0.2)
                else:
                    pygame.mixer.music.set_volume(0)
                pygame.mixer.music.play(-1)  # Запускаем бесконечный цикл проигрывания
                flag = MENU_WINDOW
                ch_win_flag = False

                x, y = 0.08 * user_screen_width, 0.66 * user_screen_height
                speed = 0.015 * user_screen_height
                power = 30
                jump_power = 20

                x2, y2 = 0.8 * user_screen_width, 0.66 * user_screen_height
                speed2 = 0.015 * user_screen_height
                power2 = 30
                jump_power2 = 20

                # создаем персонажей
                heroes = pygame.sprite.Group()

                hero1 = Hero(x, ground, speed, power, throw_back_power, jump_power, 1000, heroes, direction=RIGHT,
                             character=ALL_CHARACTERS[character1_count])
                hero2 = Hero(x2, ground, speed2, power2, throw_back_power2, jump_power2, 1000, heroes, direction=LEFT,
                             character=ALL_CHARACTERS[character2_count])

                health_dict = {hero1: health_1, hero2: health_2}

                hero1.set_enemy(hero2, health_dict)
                hero2.set_enemy(hero1, health_dict)

            elif exit_button.collidepoint(event.pos):
                running = False

        if event.type == UPDATE_FRAMES and flag == FIGHT_WINDOW:
            heroes.update()

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
