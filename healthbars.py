import pygame


class Healthbars():
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def health_on_all_arenas(self, arenas):
        for arena in arenas:
            pygame.draw.rect(arena, (255, 255, 255),  # цвет
                             (0.02 * self.screen_width - 2, 0.02 * self.screen_height - 2,  # начало
                              100 * 3 + 4, 44))  # размер
            pygame.draw.rect(arena, (0, 255, 0),
                             (0.02 * self.screen_width, 0.02 * self.screen_height, 100 * 3, 40))

            #  аналогично для второго игрока
            pygame.draw.rect(arena, (255, 255, 255),
                             (0.8 * self.screen_width - 2, 0.02 * self.screen_height - 2,
                              100 * 3 + 4, 44))
            pygame.draw.rect(arena, (0, 255, 0),
                             (0.8 * self.screen_width, 0.02 * self.screen_height, 100 * 3, 40))

    def draw(self, screen, current_health_1, current_health_2):  # Отрисовка хэлф баров
        pygame.draw.rect(screen, (255, 255, 255),
                         (0.02 * self.screen_width - 2, 0.02 * self.screen_height - 2,
                          100 * 3 + 4, 44))
        pygame.draw.rect(screen, (0, 255, 0),
                         (0.02 * self.screen_width, 0.02 * self.screen_height,
                          current_health_1 * 3, 40))

        pygame.draw.rect(screen, (255, 255, 255),
                         (0.8 * self.screen_width - 2, 0.02 * self.screen_height - 2,
                          100 * 3 + 4, 44))
        pygame.draw.rect(screen, (0, 255, 0),
                         (0.8 * self.screen_width, 0.02 * self.screen_height,
                          current_health_2 * 3, 40))
