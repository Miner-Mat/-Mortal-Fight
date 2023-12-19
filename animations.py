import pygame

user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

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