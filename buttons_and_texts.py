import pygame  # Импортируем pygame
# Импортируем нужное из других файлов
from arens import arens, arenas_count
from characters import characters, character1_count, character2_count

# Собираем информацию о разрешении экрана пользователя
user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

# Текст - заголовок игры на входном экране
game_entery_name = pygame.font.Font("Fonts/unispace bd.ttf",
                                    int(user_screen_height * 0.16))
text_surface = game_entery_name.render("MORTAL FIGHT", True, (255, 107, 107))

# Кнопка начала игры
play_button = pygame.Rect(0.78 * user_screen_width / 2, 0.21 * user_screen_height,
                          0.22 * user_screen_width, 0.12 * user_screen_height)
play_text_font = pygame.font.Font("Fonts/unispace bd.ttf",
                                  int(user_screen_height * 0.12))
play_text = play_text_font.render("PLAY", True, (255, 107, 107))
play_text_rect = play_text.get_rect(center=play_button.center)

# Кнопка выхода из игры
exit_button = pygame.Rect(0.78 * user_screen_width / 2, 0.35 * user_screen_height,
                          0.22 * user_screen_width, 0.12 * user_screen_height)
exit_text_font = pygame.font.Font("Fonts/unispace bd.ttf",
                                  int(user_screen_height * 0.12))
exit_text = exit_text_font.render("EXIT", True, (255, 107, 107))
exit_text_rect = exit_text.get_rect(center=exit_button.center)

# Кнопка возврата в меню игры
back_button = pygame.Rect(0.96 * user_screen_width / 2, 0.02 * user_screen_height,
                          0.04 * user_screen_width, 0.05 * user_screen_height)
back_image = pygame.transform.scale(pygame.image.load("krest.png").convert_alpha(),
                                    (0.03 * user_screen_width, 0.04 * user_screen_height))
back_image_rect = back_image.get_rect(center=back_button.center)

# Заголовок окна выбора арены
arena_text_font = pygame.font.Font("Fonts/unispace bd.ttf",
                                   int(user_screen_height * 0.12))
arena_text = arena_text_font.render("ARENA", True, (255, 107, 107))

# Окно выбора арены
aren_window = pygame.Rect(0.75 * user_screen_width / 4.5, 0.6 * user_screen_height,
                          0.25 * user_screen_width, 0.3 * user_screen_height)
arena = pygame.transform.scale(arens[arenas_count], aren_window.size)
arena_rect = arena.get_rect(center=aren_window.center)

# Стрелки выбора арены
left_strelka = pygame.transform.scale(pygame.image.load("left_strelka.png"),
                                      (0.05 * user_screen_width, 0.07 * user_screen_height))
left_strelka_rect = left_strelka.get_rect(topleft=(0.1 * user_screen_width, 0.69 * user_screen_height))
right_strelka = pygame.transform.scale(pygame.image.load("right_strelka.png"),
                                       (0.05 * user_screen_width, 0.07 * user_screen_height))
right_strelka_rect = right_strelka.get_rect(topleft=(0.43 * user_screen_width, 0.69 * user_screen_height))

# Иконка включенного звука
sound_on = pygame.transform.scale(pygame.image.load("soundon.png"),
                                  (0.07 * user_screen_width, 0.07 * user_screen_height))
sound_on_rect = sound_on.get_rect(topleft=(0.86 * user_screen_width, 0.09 * user_screen_height))

# Иконка выключенного звука
sound_off = pygame.transform.scale(pygame.image.load("soundoff.png"),
                                   (0.07 * user_screen_width, 0.07 * user_screen_height))
sound_off_rect = sound_off.get_rect(topleft=(0.86 * user_screen_width, 0.09 * user_screen_height))

# Окно выбора первого персонажа
character_choice_window = pygame.Rect(0.75 * user_screen_width / 1.3, 0.6 * user_screen_height,
                                      0.1 * user_screen_width, 0.3 * user_screen_height)
character_choice = pygame.transform.scale(characters[character1_count], character_choice_window.size)
character_choice_rect = character_choice.get_rect(center=character_choice_window.center)

# Стрелки для выбора первого персонажа
left_strelka_ch1 = pygame.transform.scale(pygame.image.load("left_strelka.png"),
                                          (0.02 * user_screen_width, 0.07 * user_screen_height))
left_strelka_ch1_rect = left_strelka_ch1.get_rect(topleft=(0.55 * user_screen_width, 0.69 * user_screen_height))
right_strelka_ch1 = pygame.transform.scale(pygame.image.load("right_strelka.png"),
                                           (0.02 * user_screen_width, 0.07 * user_screen_height))
right_strelka_ch1_rect = right_strelka_ch1.get_rect(topleft=(0.68 * user_screen_width, 0.69 * user_screen_height))

# Окно выбора второго персонажа
character2_choice_window = pygame.Rect(0.77 * user_screen_width, 0.6 * user_screen_height,
                                       0.1 * user_screen_width, 0.3 * user_screen_height)
character2_choice = pygame.transform.scale(characters[character2_count], character2_choice_window.size)
character2_choice_rect = character2_choice.get_rect(center=character2_choice_window.center)

# Стрелки для выбора вторго персонажа
left_strelka_ch2 = pygame.transform.scale(pygame.image.load("left_strelka.png"),
                                          (0.02 * user_screen_width, 0.07 * user_screen_height))
left_strelka_ch2_rect = left_strelka_ch2.get_rect(topleft=(0.75 * user_screen_width, 0.69 * user_screen_height))
right_strelka_ch2 = pygame.transform.scale(pygame.image.load("right_strelka.png"),
                                           (0.02 * user_screen_width, 0.07 * user_screen_height))
right_strelka_ch2_rect = right_strelka_ch2.get_rect(topleft=(0.87 * user_screen_width, 0.69 * user_screen_height))

# Сообщения о выйгрыше игроков
ch1_win_text_font = pygame.font.Font("Fonts/unispace bd.ttf", int(user_screen_height * 0.12))
ch1_win_text = ch1_win_text_font.render("PLAYER 1 WIN", True, (255, 107, 107))
ch2_win_text_font = pygame.font.Font("Fonts/unispace bd.ttf", int(user_screen_height * 0.12))
ch2_win_text = ch1_win_text_font.render("PLAYER 2 WIN", True, (255, 107, 107))

# Кнопка начала новой игры
restart_button = pygame.Rect(0.96 * user_screen_width / 2, 0.62 * user_screen_height,
                             0.07 * user_screen_width, 0.14 * user_screen_height)
restart_image = pygame.transform.scale(pygame.image.load("restart.png").convert_alpha(),
                                       (0.07 * user_screen_width, 0.14 * user_screen_height))
restart_image_rect = restart_image.get_rect(center=restart_button.center)

# Надписи обозначающие игроков под хэлфбарами
ch1_font = pygame.font.Font("Fonts/unispace bd.ttf", int(user_screen_height * 0.04))
ch1_text = ch1_font.render("PLAYER 1", True, (255, 107, 107))
ch2_font = pygame.font.Font("Fonts/unispace bd.ttf", int(user_screen_height * 0.04))
ch2_text = ch1_font.render("PLAYER 2", True, (255, 107, 107))

# Первый персонаж выбор
ch1_choice_text_font = pygame.font.Font("Fonts/unispace bd.ttf", int(user_screen_height * 0.04))
ch1_choice_text = ch1_choice_text_font.render("P1", True, (255, 107, 107))

# Второй персонаж выбор
ch2_choice_text_font = pygame.font.Font("Fonts/unispace bd.ttf", int(user_screen_height * 0.04))
ch2_choice_text = ch2_choice_text_font.render("P2", True, (255, 107, 107))

# Кнопка открытия раскладки клавиатуры
control_image = pygame.transform.scale(pygame.image.load("control_button.png"),
                                       (0.07 * user_screen_width, 0.07 * user_screen_height))
control_rect = control_image.get_rect(topleft=(0.06 * user_screen_width, 0.09 * user_screen_height))

# Окно раскладки клавиатуры
control_layout = pygame.transform.scale(pygame.image.load("conrol_layout.png"),
                                        (user_screen_width, user_screen_height))
control_layout_rect = control_layout.get_rect(topleft=(0.01 * user_screen_width, 0.01 * user_screen_height))

# кнопка возврата из окна с показом управления
back_button_from_control = pygame.Rect(0.96 * user_screen_width / 2, 0.02 * user_screen_height,
                          0.25 * user_screen_width, 0.06 * user_screen_height)
back_image_from_control = pygame.transform.scale(pygame.image.load("krest.png").convert_alpha(),
                                    (0.05 * user_screen_width, 0.06 * user_screen_height))
back_image_rect_from_control = back_image_from_control.get_rect(center=back_button_from_control.center)

# Кнопка паузы
pause_image = pygame.transform.scale(pygame.image.load("pause.png").convert_alpha(),
                                     (0.03 * user_screen_width, 0.04 * user_screen_height))
pause_image_rect = pause_image.get_rect(topleft=(0.53 * user_screen_width, 0.03 * user_screen_height))

# Кнопка продолжения игры
play_image = pygame.transform.scale(pygame.image.load("play.png").convert_alpha(),
                                    (0.03 * user_screen_width, 0.04 * user_screen_height))
play_image_rect = play_image.get_rect(topleft=(0.53 * user_screen_width, 0.03 * user_screen_height))
