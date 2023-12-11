import pygame

class Healthbars():
    def health_to_all(self, user_screen_width, user_screen_height, arens, current_health_1, current_health_2):
        for i in arens:
            pygame.draw.rect(i, (0, 255, 0), (0.02 * user_screen_width, 0.02 * user_screen_height, current_health_1 * 3, 40))
            pygame.draw.rect(i, (255, 255, 255), (0.02 * user_screen_width, 0.02 * user_screen_height, current_health_1 * 3, 40), width=2)
            pygame.draw.rect(i, (0, 255, 0), (0.8 * user_screen_width, 0.02 * user_screen_height, current_health_2 * 3, 40))
            pygame.draw.rect(i, (255, 255, 255), (0.8 * user_screen_width, 0.02 * user_screen_height, current_health_2 * 3, 40), width=2)

    def health_bar(self, user_screen_width, user_screen_height, arens, arenas_count, current_health_1, current_health_2):  # Отрисовка хэлф баров
        pygame.draw.rect(arens[arenas_count], (0, 255, 0), (0.02 * user_screen_width, 0.02 * user_screen_height, current_health_1 * 3, 40))
        pygame.draw.rect(arens[arenas_count], (255, 255, 255), (0.02 * user_screen_width, 0.02 * user_screen_height, current_health_1 * 3, 40), width=2)
        pygame.draw.rect(arens[arenas_count], (0, 255, 0), (0.8 * user_screen_width, 0.02 * user_screen_height, current_health_2 * 3, 40))
        pygame.draw.rect(arens[arenas_count], (255, 255, 255), (0.8 * user_screen_width, 0.02 * user_screen_height, current_health_2 * 3, 40), width=2)
