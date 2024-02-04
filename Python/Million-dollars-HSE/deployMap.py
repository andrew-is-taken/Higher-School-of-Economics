import pygame
from mapGenerator import genMap


def Map(gameWindow, x, y, map):
    '''
    gameWindow: pygame.display.set_mode((resolution x, resolution y)), pygame window
    x: int, map horizontal size(min 10)
    y: int, map vertical size(min 10)
    Function makes visualization of generated map in pygame window.
    '''
    border = pygame.image.load('static/border.png')
    background = pygame.image.load('static/background.jpg')
    background = pygame.transform.scale(background, (30 * x, 30 * y))
    gameWindow.blit(background, (0, 0))
    # draw generated map in window
    for i in range(0, 30 * x, 30):
        gameWindow.blit(border, (i, 0))
    for i in range(0, 30 * x, 30):
        gameWindow.blit(border, (i, 30 * (x - 1)))
    for i in range(30, 30 * y, 30):
        gameWindow.blit(border, (0, i))
    for i in range(30, 30 * y, 30):
        gameWindow.blit(border, (30 * (y - 1), i))
    for j in range(1, len(map)):
        for i in range(1, len(map[0])):
            if (map[j][i] == 'B'):
                gameWindow.blit(border, (i * 30, j * 30))
    # save result image to folder
    pygame.image.save(gameWindow, 'static/renderedMap.jpg')
    return True


def UpdateScoreText(scoreValue, gameWindow, Font, xCoord):
    '''
    scoreValue: current length of snake
    gameWindow: pygame window
    Font: font to render the text
    xCoord: value on horizontal axis where the text will be rendered
    surface: black image to render over previous text
    Function updates the score text with current length of snake
    '''
    textObj = Font.render(str(scoreValue), False, (255, 255, 255))
    gameWindow.blit(textObj, (xCoord - textObj.get_rect()[2] / 2, 60))
