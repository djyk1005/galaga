import pygame
import time
# initialization
pygame.init()
# color declaration
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# screen size
display_width = 800
display_height = 600
# frames per second
clock = pygame.time.Clock()
FPS = 30
# display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('galaga')
pygame.display.update()

# main loop


def gameLoop():

    gameExit = False
    gameOver = False
    # starting positions
    sx = display_width / 2
    sy = display_height / 4 * 3
    #change in positions
    dx = 0
    dy = 0

    while not gameExit:
        # TODO: game over

        for event in pygame.event.get():
            # event log (unnecessary)
            #print (event)
            # X out
            if event.type == pygame.QUIT:
                gameExit = True
            # movement
            # TODO:fix multiple pressed arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx += -10
                if event.key == pygame.K_RIGHT:
                    dx += 10
                if event.key == pygame.K_UP:
                    dy += -10
                if event.key == pygame.K_DOWN:
                    dy += 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dy = 0
        sx + dx
        sy + dy
        # render
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [sx, sy, 10, 10])
        pygame.display.update()
        clock.tick(FPS)
    pygame.display.update()

    pygame.quit()
    quit()


gameLoop()
