import pygame


WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")

FPS = 60

run = True
clock = pygame.time.Clock()

def board():
    color = (255, 255, 255)
    width = WIN.get_width()
    for i in range(1, 10):
        pos = width / 10 * i
        # linia pozioma
        pygame.draw.line(WIN, color, (0, pos), (width, pos), 1)
        # linia pionowa
        pygame.draw.line(WIN, color, (pos, 0), (pos, width), 1)

while run:
    clock.tick(FPS)

#    draw(WIN, images, player_car)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        else:
            board()
            pygame.draw.rect(WIN, (222, 1, 22), pygame.Rect(0, 0, 50, 50))
