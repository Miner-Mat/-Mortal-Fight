import pygame

user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

characters = [pygame.transform.scale(pygame.image.load("Characters_images/Ded_Maxim.png"), (user_screen_width, user_screen_height)),
         pygame.transform.scale(pygame.image.load("Characters_images/Vurdalak.png"), (user_screen_width, user_screen_height))]