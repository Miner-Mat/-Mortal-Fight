import pygame  # импортируем pygame
from healthbars import Healthbars  # Импортируем класс Healthbars

# Инициализация Pygame
pygame.init()

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

# Анимации персонажа в момент неподвижности вправо
anim_st = [pygame.image.load("Character_st/1st.png"),
           pygame.image.load("Character_st/2st.png"),
           pygame.image.load("Character_st/3st.png"),
           pygame.image.load("Character_st/4st.png"),
           pygame.image.load("Character_st/5st.png"),
           pygame.image.load("Character_st/6st.png"),
           pygame.image.load("Character_st/7st.png")]

# Анимации персонажа в момент неподвижности влево
minus_anim_st = [pygame.image.load("-Character_st/1st.png"), pygame.image.load("-Character_st/2st.png"),
                 pygame.image.load("-Character_st/3st.png"), pygame.image.load("-Character_st/4st.png"),
                 pygame.image.load("-Character_st/5st.png"), pygame.image.load("-Character_st/6st.png"),
                 pygame.image.load("-Character_st/7st.png")]

# Анимации персонажа во время атаки
anim_fight = [pygame.image.load("Character_fight/Attack_1.png"), pygame.image.load("Character_fight/Attack_2.png"),
              pygame.image.load("Character_fight/Attack_3.png"), pygame.image.load("Character_fight/Attack_4.png"),
              pygame.image.load("Character_fight/Attack_5.png")]

# Анимации персонажа во время бега
anim_run = [pygame.image.load("charact_run/run1.png"), pygame.image.load("charact_run/run2.png"),
            pygame.image.load("charact_run/run3.png"), pygame.image.load("charact_run/run4.png"),
            pygame.image.load("charact_run/run5.png"), pygame.image.load("charact_run/run6.png"),
            pygame.image.load("charact_run/run7.png"), pygame.image.load("charact_run/run8.png")]

# Арены для сражения
arens = [pygame.transform.scale(pygame.image.load("arenas/location.jpg"), (user_screen_width, user_screen_height)),
         pygame.transform.scale(pygame.image.load("arenas/location2.jpg"), (user_screen_width, user_screen_height)),
         pygame.transform.scale(pygame.image.load("arenas/location1.jpg"), (user_screen_width, user_screen_height)),
         pygame.transform.scale(pygame.image.load("arenas/location3.jpg"), (user_screen_width, user_screen_height)),
         pygame.transform.scale(pygame.image.load("arenas/location4.jpg"), (user_screen_width, user_screen_height))]

# константы для отслеживания текущего окна
MENU = 0
FIGHT = 1

width_of_character = anim_run[0].get_width()

# Определяющие положение персонажа переменные
x, y = 0.08 * user_screen_width, 0.66 * user_screen_height
early_x = 0
final_x = user_screen_width - width_of_character
speed = 0.008 * user_screen_height

# Определяющие положение второго персонажа переменные
x2, y2 = 0.8 * user_screen_width, 0.66 * user_screen_height
early_x2 = 0
final_x2 = user_screen_width - width_of_character
speed2 = 0.008 * user_screen_height

current_frame = 0  # текущий кадр стояния
current_frame_run = 0  # последний обновлённый кадр бега персонажа
current_frame_fight = 0
animation_delay = 100  # Задержка между кадрами


current_frame2 = 0
current_frame_run2 = 0

clock = pygame.time.Clock()

# Значения хэлф баров
current_health_1 = 100
current_health_2 = 100

# Флаги состояния положения персонажа
standing = True
left = False
right = True

standing2 = True
left2 = True
right2 = False

# Счетчик выбора арен
arenas_count = 2

# Текст - загаловок игры на входном экране
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


def frame_check():  # Проверка кадров
    '''
    Функция для смены кадров анимации
    :return:
    '''
    global current_frame, count, current_frame2, current_frame_fight
    if current_frame == 6:
        current_frame = 0
    if current_frame2 == 6:
        current_frame2 = 0
    if current_frame_fight == 4:
        current_frame_fight = 0
    current_frame += 1
    current_frame2 += 1
    current_frame_fight += 1


def key_check():  # Проверка нажатий
    '''
    Функция для проверки нажатий на клавиши для перемещения персонажей и их непосредственного перемещения
    :return:
    '''
    global x, current_frame_run, early_x, standing, right, left, speed, final_x
    global standing2, right2, left2, x2, current_frame_run2, speed2, early_x2, final_x2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if x - speed < early_x:
            x = early_x
            current_frame_run += 1
        else:
            x -= speed
            current_frame_run += 1
        if current_frame_run == 7:
            current_frame_run = 0
        standing = False
        right = False
        left = True

    elif keys[pygame.K_d]:
        # Если персонаж передвинется вправо после следующего хода, проверяем не выйдет ли он за пределы
        if x + speed + width_of_character > final_x:  # Нужно вычесть ширину персонажа из final_x
            x = final_x - width_of_character
        else:
            x += speed
        current_frame_run = (current_frame_run + 1) % 8  # Изменим логику обновления кадров бега
        standing = False
        right = True
        left = False

    if keys[pygame.K_LEFT]:
        if x2 - speed2 < early_x2:
            x2 = early_x2
            if current_frame_run2 == 0:
                current_frame_run2 = 7
            current_frame_run2 -= 1
        else:
            x2 -= speed2
            if current_frame_run2 == 0:
                current_frame_run2 = 7
            current_frame_run2 -= 1
        standing2 = False
        left2 = True
        right2 = False

    elif keys[pygame.K_RIGHT]:
        # Аналогично для второго персонажа
        if x2 + speed2 + width_of_character > final_x2:
            x2 = final_x2 - width_of_character
        else:
            x2 += speed2
        current_frame_run2 = (current_frame_run2 + 1) % 8
        standing2 = False
        left2 = False
        right2 = True


def key_work():
    '''
    Функция для обработки нажатий на клавиши и запуска нужных анимаций
    :return:
    '''
    global current_health_2
    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if flag == FIGHT:
            if x < x2 + 170 and x + 170 > x2 and y < y2 + 300 and y + 300 > y2:
                current_health_2 -= 0.5

    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_f]:
        if left:
            screen.blit(pygame.transform.scale(minus_anim_st[current_frame], (0.09 * user_screen_width,
                                                                              0.28 * user_screen_height)), (x, y))
        if right:
            screen.blit(pygame.transform.scale(anim_st[current_frame], (0.09 * user_screen_width, 0.28 *
                                                                        user_screen_height)), (x, y))
    elif keys[pygame.K_a]:
        screen.blit(pygame.transform.flip(pygame.transform.scale(anim_run[current_frame],
                                                                 (0.14 * user_screen_width,
                                                                  0.28 * user_screen_height)), True, False), (x, y))
    elif keys[pygame.K_d]:
        screen.blit(pygame.transform.scale(anim_run[current_frame], (0.14 * user_screen_width,
                                                                     0.28 * user_screen_height)), (x, y))
    elif keys[pygame.K_f]:
        screen.blit(pygame.transform.scale(anim_fight[current_frame_fight], (0.14 * user_screen_width,
                                                                             0.28 * user_screen_height)), (x, y))

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if right2:
            screen.blit(
                pygame.transform.flip(pygame.transform.scale(minus_anim_st[current_frame2],
                                                             (0.09 * user_screen_width,
                                                              0.28 * user_screen_height)), True, False),
                (x2, y2))
        if left2:
            screen.blit(pygame.transform.flip(pygame.transform.scale(anim_st[current_frame2],
                                                                     (0.09 * user_screen_width,
                                                                      0.28 * user_screen_height)), True, False),
                        (x2, y2))
    elif keys[pygame.K_LEFT]:
        screen.blit(pygame.transform.flip(pygame.transform.scale(anim_run[current_frame2],
                                                                 (0.15 * user_screen_width,
                                                                  0.28 * user_screen_height)), True, False),
                    (x2, y2))
    elif keys[pygame.K_RIGHT]:
        screen.blit(pygame.transform.scale(anim_run[current_frame2], (0.15 * user_screen_width,
                                                                      0.28 * user_screen_height)), (x2, y2))


UPDATE_FRAMES = pygame.USEREVENT + 1  # создаём событие для обновления кадров и присваиваем ему номер
pygame.time.set_timer(UPDATE_FRAMES, 100)

flag = MENU
running = True  # флаг работы

while running:
    clock.tick(60)  # обновление экрана 60 раз в секунду
    health.health_to_all(user_screen_width, user_screen_height, arens, current_health_1, current_health_2)
    arena = pygame.transform.scale(arens[arenas_count], (600, 400))
    if flag == MENU:
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

    elif flag == FIGHT:
        health.health_bar(user_screen_width, user_screen_height, arens, arenas_count, current_health_1, current_health_2)
        key_check()  # вызываем проверку нажатий
        screen.blit(arens[arenas_count], (0, 0))  # отрисовываем фон
        pygame.draw.rect(screen, (170, 0, 0), back_button)
        screen.blit(back_image, back_image_rect)

        key_work()  # вызываем обработку нажатий

    pygame.display.update()  # обновляем окно

    # Скрипт выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                flag = FIGHT
            elif left_strelka_rect.collidepoint(event.pos):
                arenas_count -= 1
                if arenas_count < 0:
                    arenas_count = len(arens) - 1
            elif right_strelka_rect.collidepoint(event.pos):
                arenas_count += 1
                if arenas_count >= len(arens):
                    arenas_count = 0
            elif back_button.collidepoint(event.pos):
                flag = MENU
                # Сбрасываем значения всех переменных до по умолчанию
                x, y = 0.08 * user_screen_width, 0.66 * user_screen_height
                early_x = 0
                final_x = user_screen_width - width_of_character
                early_x2 = 0
                final_x2 = user_screen_width - width_of_character
                speed = 5
                x2, y2 = 0.8 * user_screen_width, 0.66 * user_screen_height
                speed2 = 5
                current_frame = 0
                current_frame_run = 0
                current_frame_fight = 0
                animation_delay = 100
                last_update = pygame.time.get_ticks()
                current_frame2 = 0
                current_frame_run2 = 0
                current_health_1 = 100
                current_health_2 = 100
                standing = True
                left = False
                right = True
                standing2 = True
                left2 = True
                right2 = False
                count = 6

            elif exit_button.collidepoint(event.pos):
                running = False

        if event.type == UPDATE_FRAMES:
            frame_check()  # вызываем проверку кадров

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()