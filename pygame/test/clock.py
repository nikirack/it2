import pygame
from datetime import datetime

pygame.init()

screen: pygame.Surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clock")

font = pygame.font.Font(None, 256)

clock = pygame.time.Clock()

center: tuple[int, int] = (screen.get_width() // 2, screen.get_height() // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    text = str(datetime.now().strftime("%H:%M:%S"))

    rendered_text: pygame.Surface = font.render(text, True, (0, 0, 0))

    screen.fill((255, 255, 255))

    text_rect: pygame.Rect = rendered_text.get_rect(center=center)
    screen.blit(rendered_text, text_rect)

    pygame.display.flip()

    clock.tick(10)

pygame.quit()