import pygame
from Line import Line

pygame.init()

screen = pygame.display.set_mode((1550, 800))
pygame.display.set_caption("My Game")
running = True

while running:
    screen.fill((0,0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #: Выход из окна
            running = False
            pygame.quit()
            exit()
        Line() #: Создание квадратов за мышкой
