import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Square")

clock = pygame.time.Clock()

x = 0
y = 250
speed = 500 #pixels per second 

FPS = 6000

running = True
while running:
    dt = clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += speed*dt

    if x > 800:
        x = -50

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 150, 255), (x, y, 50, 50))

    pygame.display.flip()

pygame.quit()