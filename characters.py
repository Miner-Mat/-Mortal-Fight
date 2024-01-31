import pygame  # Импортируем pygame

# Собираем информацию о разрешении экрана пользователя
user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

character1_count = 0  # Счётчик выбранного первого персонажа
character2_count = 1  # Счётчик выбранного второго персонажа

# Загружаем изображения персонажей, которые будут отображаться при их выборе
characters = [pygame.transform.scale(pygame.image.load("Characters_images/Ded_Maxim.png"),
                                     (user_screen_width, user_screen_height)),
              pygame.transform.scale(pygame.image.load("Characters_images/Vurdalak.png"),
                                     (user_screen_width, user_screen_height))]
