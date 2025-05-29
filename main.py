import pygame
import os

def main():

    #initialize pygame
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #close if ESC is pressed
                    run = False

        screen.fill("black")

        pygame.display.flip
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
