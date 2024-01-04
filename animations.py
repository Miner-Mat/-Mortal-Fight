import pygame

user_screen_info = pygame.display.Info()
user_screen_width = user_screen_info.current_w
user_screen_height = user_screen_info.current_h

# Анимации персонажа в момент неподвижности вправо
anim_stay = [pygame.image.load("Character_st/1st.png"),
           pygame.image.load("Character_st/2st.png"),
           pygame.image.load("Character_st/3st.png"),
           pygame.image.load("Character_st/4st.png"),
           pygame.image.load("Character_st/5st.png"),
           pygame.image.load("Character_st/6st.png"),
           pygame.image.load("Character_st/7st.png")]

# Анимации персонажа во время атаки
anim_fight = [pygame.image.load("Character_fight/Attack_1.png"), pygame.image.load("Character_fight/Attack_2.png"),
              pygame.image.load("Character_fight/Attack_3.png"), pygame.image.load("Character_fight/Attack_4.png"),
              pygame.image.load("Character_fight/Attack_5.png")]

# Анимации персонажа во время бега
anim_run = [pygame.image.load("charact_run/run1.png"), pygame.image.load("charact_run/run2.png"),
            pygame.image.load("charact_run/run3.png"), pygame.image.load("charact_run/run4.png"),
            pygame.image.load("charact_run/run5.png"), pygame.image.load("charact_run/run6.png"),
            pygame.image.load("charact_run/run7.png"), pygame.image.load("charact_run/run8.png")]

# Анимации персонажа во время прыжка
# anim_jump = [pygame.image.load("Character_jump/Jump_1.png"), pygame.image.load("Character_jump/Jump_2.png"),
#              pygame.image.load("Character_jump/Jump_3.png"), pygame.image.load("Character_jump/Jump_4.png"),
#              pygame.image.load("Character_jump/Jump_5.png"), pygame.image.load("Character_jump/Jump_6.png"),
#              pygame.image.load("Character_jump/Jump_7.png"), pygame.image.load("Character_jump/Jump_8.png"),
#              pygame.image.load("Character_jump/Jump_9.png")]

anim_jump = [pygame.image.load("Character_jump/Jump_3.png"), pygame.image.load("Character_jump/Jump_4.png"),
             pygame.image.load("Character_jump/Jump_5.png"), pygame.image.load("Character_jump/Jump_6.png"),
             pygame.image.load("Character_jump/Jump_7.png"), pygame.image.load("Character_jump/Jump_8.png")]
