import pygame

# Initialize pygame
pygame.init()

# Create window
screen: pygame.Surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello World")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(size=64)
text: pygame.Surface = font.render("Hello, World!", True, BLACK)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Center text
    text_rect: pygame.Rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)

    pygame.display.update()

# Quit
pygame.quit()