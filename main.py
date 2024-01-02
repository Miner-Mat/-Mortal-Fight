import pygame  # импортируем pygame
from healthbars import Healthbars  # Импортируем класс Healthbars
from constants_for_hero import *

# Инициализация Pygame
pygame.init()


from hero import Hero
from arens import arens


user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

screen = pygame.display.set_mode((user_screen_width, user_screen_height))  # Задаём разрешение основного окна
pygame.display.set_caption("Mortal Fight")  # Задаём название программе
icon = pygame.image.load("logo.jpg")  # Загружаем логотип
pygame.display.set_icon(icon)  # Выставляем логотип

pygame.mixer.init()  # инициализируем функцию добавления музыки
pygame.mixer.music.load("music.mp3")  # Загружаем музыку
pygame.mixer.music.set_volume(0.2)  # Выставляем громкость
pygame.mixer.music.play(-1)  # Запускаем бесконечный цикл проигрывания

# константы для отслеживания текущего окна
MENU_WINDOW = 0
FIGHT_WINDOW = 1

ground = int(0.94 * user_screen_height)

# Определяющие положение персонажа переменные
x, y = 0.08 * user_screen_width, 0.66 * user_screen_height
speed = 0.015 * user_screen_height
power = 5
jump_power = 20

# Определяющие положение второго персонажа переменные
x2, y2 = 0.8 * user_screen_width, 0.66 * user_screen_height
speed2 = 0.015 * user_screen_height
power2 = 5
jump_power2 = 20

clock = pygame.time.Clock()

# Значения хэлф баров
current_health_1 = 100
current_health_2 = 100

# Счетчик выбора арен
arenas_count = 2

# Текст - заголовок игры на входном экране
game_entery_name = pygame.font.Font("Fonts/unispace bd.ttf", int((0.33 * user_screen_width) // (0.36 * user_screen_width // 100)))
text_surface = game_entery_name.render("MORTAL FIGHT", True, (255, 107, 107))

# Кнопка начала игры
play_button = pygame.Rect(0.43 * user_screen_width, 0.2 * user_screen_height, 300, 100)
play_text_font = pygame.font.Font("Fonts/unispace bd.ttf", int((0.08 * user_screen_width) // (0.12 * user_screen_width // 100)))
play_text = play_text_font.render("PLAY", True, (255, 107, 107))
play_text_rect = play_text.get_rect(center=play_button.center)

# Кнопка выхода из игры
exit_button = pygame.Rect(0.43 * user_screen_width, 0.32 * user_screen_height, 300, 100)
exit_text_font = pygame.font.Font("Fonts/unispace bd.ttf", int((0.08 * user_screen_width) // (0.12 * user_screen_width // 100)))
exit_text = exit_text_font.render("EXIT", True, (255, 107, 107))
exit_text_rect = exit_text.get_rect(center=exit_button.center)

# Кнопка возврата в меню игры
back_button = pygame.Rect(0.64 * user_screen_width, 0.02 * user_screen_height, 50, 50)
back_image = pygame.transform.scale(pygame.image.load("krest.png").convert_alpha(), (0.02 * user_screen_width, 0.03 * user_screen_height))
back_image_rect = back_image.get_rect(center=back_button.center)

# Заголовок окна выбора арены
arena_text_font = pygame.font.Font("Fonts/unispace bd.ttf", int((0.08 * user_screen_width) // (0.12 * user_screen_width // 100)))
arena_text = arena_text_font.render("ARENA", True, (255, 107, 107))

# Окно выбора арены
aren_window = pygame.Rect(0.11 * user_screen_width, 0.53 * user_screen_height, 600, 400)
arena = pygame.transform.scale(arens[arenas_count], (600, 400))
arena_rect = arena.get_rect(center=aren_window.center)

# Стрелки выбора арены
left_strelka = pygame.transform.scale(pygame.image.load("left_strelka.png"), (0.05 * user_screen_width, 0.05 * user_screen_height))
left_strelka_rect = left_strelka.get_rect(topleft=(0.05 * user_screen_width, 0.68 * user_screen_height))
right_strelka = pygame.transform.scale(pygame.image.load("right_strelka.png"), (0.05 * user_screen_width, 0.05 * user_screen_height))
right_strelka_rect = right_strelka.get_rect(topleft=(0.44 * user_screen_width, 0.67 * user_screen_height))

health = Healthbars()  # Объявляем класс хэлфбаров

heroes = pygame.sprite.Group()

hero1 = Hero(x, y, ground, speed, power, jump_power, 1000, heroes, direction=RIGHT)
hero2 = Hero(x2, y2, ground, speed2, power2, jump_power2, 1000, heroes, direction=LEFT)


def key_check():  # Проверка нажатий
    '''
    Функция для проверки нажатий на клавиши и их обработки
    :return:
    '''
    keys = pygame.key.get_pressed()
    res1 = []  # списки с флагами, которые передадим в классы персонажей
    res2 = []
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
        res2.append(FIGHT_WINDOW)

    hero1.process_events(res1)
    hero2.process_events(res2)

    hero1.move()
    hero2.move()


animation_delay = 100
UPDATE_FRAMES = pygame.USEREVENT + 1  # создаём событие для обновления кадров и присваиваем ему номер
pygame.time.set_timer(UPDATE_FRAMES, animation_delay)

flag = MENU_WINDOW
running = True  # флаг работы

while running:
    clock.tick(60)  # обновление экрана 60 раз в секунду
    health.health_to_all(user_screen_width, user_screen_height, arens, current_health_1, current_health_2)
    arena = pygame.transform.scale(arens[arenas_count], (600, 400))
    if flag == MENU_WINDOW:
        screen.fill((192, 6, 13))
        screen.blit(text_surface, (0.31 * user_screen_width, 0.04 * user_screen_height))
        pygame.draw.rect(screen, (170, 0, 0), play_button)
        screen.blit(play_text, play_text_rect)
        pygame.draw.rect(screen, (170, 0, 0), exit_button)
        screen.blit(exit_text, exit_text_rect)
        pygame.draw.rect(screen, (170, 0, 0), aren_window)
        screen.blit(arena, arena_rect)
        screen.blit(arena_text, (0.2 * user_screen_width, 0.43 * user_screen_height))
        screen.blit(left_strelka, (0.05 * user_screen_width, 0.68 * user_screen_height))
        screen.blit(right_strelka, (0.43 * user_screen_width, 0.67 * user_screen_height))

    elif flag == FIGHT_WINDOW:
        health.health_bar(user_screen_width, user_screen_height, arens, arenas_count, current_health_1, current_health_2)
        screen.blit(arens[arenas_count], (0, 0))  # отрисовываем фон
        pygame.draw.rect(screen, (170, 0, 0), back_button)
        screen.blit(back_image, back_image_rect)

        key_check()  # вызываем проверку нажатий

        heroes.draw(screen)

    pygame.display.update()  # обновляем окно

    # Скрипт выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                flag = FIGHT_WINDOW
            elif left_strelka_rect.collidepoint(event.pos):
                arenas_count -= 1
                if arenas_count < 0:
                    arenas_count = len(arens) - 1
            elif right_strelka_rect.collidepoint(event.pos):
                arenas_count += 1
                if arenas_count >= len(arens):
                    arenas_count = 0

            elif back_button.collidepoint(event.pos):
                flag = MENU_WINDOW

            elif exit_button.collidepoint(event.pos):
                running = False

        if event.type == UPDATE_FRAMES:
            heroes.update()

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
