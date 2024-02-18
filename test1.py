import pygame

pygame.init()


def zoom_in():
    print("Scrolled up")

def zoom_out():
    print("Scrolled down")


pygame.display.set_caption("Zoom Zoom")
screen = pygame.display.set_mode((750, 750))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zoom_in()
            elif event.button == 5:
                zoom_out()
    pygame.display.flip()