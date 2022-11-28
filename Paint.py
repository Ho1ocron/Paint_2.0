import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My Game")
running = True
while running:
    screen.fill((255,255,255))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            