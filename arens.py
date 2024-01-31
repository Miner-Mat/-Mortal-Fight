import pygame  # Импортируем pygame

# Собираем информацию о разрешении экрана пользователя
user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

arenas_count = 2  # Счётчик выбранной арены

# Загружаем изображения арен
arens = [pygame.transform.scale(pygame.image.load("arenas/location.jpg"), (user_screen_width, user_screen_height)),
         pygame.transform.scale(pygame.image.load("arenas/location2.jpg"), (user_screen_width, user_screen_height)),
         pygame.transform.scale(pygame.image.load("arenas/location1.jpg"), (user_screen_width, user_screen_height)),
         pygame.transform.scale(pygame.image.load("arenas/location3.jpg"), (user_screen_width, user_screen_height)),
         pygame.transform.scale(pygame.image.load("arenas/location4.jpg"), (user_screen_width, user_screen_height))]
