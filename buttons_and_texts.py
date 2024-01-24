import pygame
from arens import arens, arenas_count


user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

# Текст - заголовок игры на входном экране
game_entery_name = pygame.font.Font("Fonts/unispace bd.ttf",
                                    int(user_screen_width * 0.08 * user_screen_width * 0.08 / 100))
text_surface = game_entery_name.render("MORTAL FIGHT", True, (255, 107, 107))

# Кнопка начала игры
play_button = pygame.Rect(0.78 * user_screen_width / 2, 0.21 * user_screen_height,
                          0.22 * user_screen_width, 0.12 * user_screen_height)
play_text_font = pygame.font.Font("Fonts/unispace bd.ttf",
                                  int(user_screen_width * 0.07 * user_screen_width * 0.07 / 100))
play_text = play_text_font.render("PLAY", True, (255, 107, 107))
play_text_rect = play_text.get_rect(center=play_button.center)

# Кнопка выхода из игры
exit_button = pygame.Rect(0.78 * user_screen_width / 2, 0.35 * user_screen_height,
                          0.22 * user_screen_width, 0.12 * user_screen_height)
exit_text_font = pygame.font.Font("Fonts/unispace bd.ttf",
                                  int(user_screen_width * 0.07 * user_screen_width * 0.07 / 100))
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
                                   int(user_screen_width * 0.07 * user_screen_width * 0.07 / 100))
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