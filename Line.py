import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill(BLACK)
pygame.display.update()
a = True



def Line():
    while 1:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.draw.rect(screen, (255, 255, 255), ((pos[0]-25, pos[1]-25), (50, 50)))
        pygame.display.update()
        pygame.time.delay(20)

        