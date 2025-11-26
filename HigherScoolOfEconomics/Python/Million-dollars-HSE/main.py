from class_zmey import *
import deployMap as renderedMap
from mapGenerator import genMap
from pacman import *

# x-size on horizontal axis(min 15)
# y-size on vertical axis(min 15)
x = 30
y = 30


class NeedToRetry():
    def __init__(self):
        self.retry = False


def main(x, y):
    '''
    x: amount of cells on width
    y: amount of cells on height
    Main function, opening pygame window, displaying generated map and updating events in game
    '''
    pg.init()
    pg.font.init()
    gameWindow = pg.display.set_mode((x * 30 + 300, y * 30))
    Font = pg.font.SysFont('Comic Sans MS', 30)
    clock = pg.time.Clock()
    map = genMap(x, y, 10)
    zmeyka = Zmeyka(map, 30)
    pacman = PacMan(map, 30, gameWindow, zmeyka)
    zmeyka.finished = False
    zmeyka.screen = gameWindow
    shownEndDisplay = False
    needToUpdate = True
    NeedToRetryObj = NeedToRetry()

    staticText = Font.render('SCORE', False, (255, 255, 255))
    xCoord = 30 * x + 150
    gameWindow.blit(staticText, (xCoord - staticText.get_rect()[2] / 2, 20))
    play = True
    renderedMap.Map(gameWindow, x, y, map)
    background = pg.image.load('static/renderedMap.jpg')
    while play:  # update every frame
        clock.tick(30)
        if (NeedToRetryObj.retry):
            map = genMap(x, y, 10)
            zmeyka = Zmeyka(map, 30)
            pacman = PacMan(map, 30, gameWindow, zmeyka)
            zmeyka.finished = False
            zmeyka.screen = gameWindow
            shownEndDisplay = False
            needToUpdate = True

            staticText = Font.render('SCORE', False, (255, 255, 255))
            xCoord = 30 * x + 150
            gameWindow.blit(staticText, (xCoord - staticText.get_rect()[2] / 2, 20))
            play = True
            renderedMap.Map(gameWindow, x, y, map)
            background = pg.image.load('static/renderedMap.jpg')
            NeedToRetryObj.retry = False
        if (not zmeyka.finished):  # if game didn't end
            DrawEvents(gameWindow, background, zmeyka, pacman)
        elif (not shownEndDisplay):  # if game ended but not showing display with score and retry
            lostGame(gameWindow)
            shownEndDisplay = True
        if (shownEndDisplay and needToUpdate):  # if game ended and showing display with score and retry
            bestScore = int(open('static/bestScore.txt', 'r').read())
            ScoreText = Font.render('SCORE: ' + str(zmeyka.length), False, (255, 255, 255))
            gameWindow.blit(ScoreText, (gameWindow.get_size()[0] // 2 - ScoreText.get_rect()[2] // 2,
                                        gameWindow.get_size()[1] // 2 - ScoreText.get_rect()[3] // 2 - 100))
            BestScoreText = Font.render('BEST SCORE WAS: ' + str(bestScore), False, (255, 255, 255))
            gameWindow.blit(BestScoreText, (gameWindow.get_size()[0] // 2 - BestScoreText.get_rect()[2] // 2,
                                            gameWindow.get_size()[1] // 2 - BestScoreText.get_rect()[3] // 2 + 100))
            if (bestScore < zmeyka.length):
                open('static/bestSCore.txt', 'w').close()
                file = open('static/bestSCore.txt', 'w')
                file.write(str(zmeyka.length))
                file.close()
            needToUpdate = False
            img = pg.image.load('static/buttonSprite.png')
            gameWindow.blit(img, (gameWindow.get_size()[0] // 2 - img.get_rect()[2] // 2,
                                  gameWindow.get_size()[1] // 2 - img.get_rect()[3] // 2))
            EndText = Font.render('RETRY', False, (0, 0, 0))
            gameWindow.blit(EndText, (gameWindow.get_size()[0] // 2 - EndText.get_rect()[2] // 2,
                                      gameWindow.get_size()[1] // 2 - EndText.get_rect()[3] // 2))
            rect = pg.Rect(gameWindow.get_size()[0] // 2 - img.get_rect()[2] // 2,
                           gameWindow.get_size()[1] // 2 - img.get_rect()[3] // 2, img.get_rect()[2], img.get_rect()[3])
        for event in pg.event.get():  # checking game events
            if (shownEndDisplay):
                clickRetry(event, rect, NeedToRetryObj)
            if event.type == pg.QUIT:
                play = False
        pg.display.update()


def DrawEvents(gameWindow, background, zmeyka, pacman):
    '''
    gameWindow: pygame window
    background: rendered map as image
    zmeyka: class 
    '''
    # updating screen and rendering
    gameWindow.fill((0, 0, 0))
    gameWindow.blit(background, (0, 0))
    user_input = pg.key.get_pressed()
    # updating snake, pacman and rendering
    zmeyka.update(zmeyka.game_map, user_input)
    pacman.update(pacman.game_map)


def lostGame(gameWindow):
    '''
    gameWindow: pygame window
    Called when snake hits walls, displaying end game screen
    '''
    img = pg.image.load('static/loseBackground.png')
    img = pg.transform.scale(img, (30 * x, 30 * y))
    gameWindow.blit(img, (0, 0))


def clickRetry(event, button, obj):
    '''
    button: rect
    Click on retry button to start game from the beginning
    '''
    mouse_x, mouse_y = pg.mouse.get_pos()
    if event.type == pg.MOUSEBUTTONDOWN:
        if pg.mouse.get_pressed()[0]:
            if button.collidepoint(mouse_x, mouse_y):
                obj.retry = True


if __name__ == '__main__':
    main(x, y)
