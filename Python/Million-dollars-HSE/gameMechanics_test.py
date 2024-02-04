import unittest
from mapGenerator import genMap
from deployMap import Map, UpdateScoreText
from spawnSimpleEnemy import findEntitySpawn
import pygame


class functionalityTest(unittest.TestCase):
    def test_generation(self):
        map = genMap(30, 30, 10)
        self.assertIs(type(map), list)  # Check if function successfully generated map and returned it as a list
        for i in range(len(map)):
            print(map[i])

    def test_generation(self):
        map = genMap(20, 20, 10)
        self.assertIs(type(map), list)  # Check if function successfully generated map and returned it as a list
        for i in range(len(map)):
            print(map[i])

    def test_display(self):
        x = 30
        y = 30
        pygame.init()
        pygame.font.init()
        gameWindow = pygame.display.set_mode((30 * x + 300, 30 * y))
        Font = pygame.font.SysFont('Comic Sans MS', 30)
        map = genMap(x, y, 10)

        clock = pygame.time.Clock()
        staticText = Font.render('SCORE', False, (255, 255, 255))
        xCoord = 30 * 30 + 150
        gameWindow.blit(staticText, (xCoord - staticText.get_rect()[2] / 2, 20))
        play = True
        mapDisaplayed = Map(gameWindow, x, y, map)
        background = pygame.image.load('static/renderedMap.jpg')
        score = 0
        timer = 0
        while play:
            clock.tick(30)
            score += 1
            timer += 1
            if (timer > 30):
                play = False
            gameWindow.fill((0, 0, 0))
            gameWindow.blit(background, (0, 0))
            UpdateScoreText(score, gameWindow, Font, xCoord)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False

            pygame.display.update()

        pygame.quit()
        self.assertTrue(mapDisaplayed is True)  # True if successfully generated map and saved it as image

    def test_spawn_search(self):
        map = genMap(30, 30, 10)
        self.assertIs(type(findEntitySpawn(map, 0)),
                      tuple)  # Check if function successfully found spawn for ghost on map and returned it as a tuple
        self.assertIs(type(findEntitySpawn(map, 1)),
                      tuple)  # Check if function successfully found spawn for food on map and returned it as a tuple

    def test_spawn_search(self):
        map = genMap(15, 15, 5)
        self.assertIs(type(findEntitySpawn(map, 0)),
                      tuple)  # Check if function successfully found spawn for ghost on map and returned it as a tuple
        self.assertIs(type(findEntitySpawn(map, 1)),
                      tuple)  # Check if function successfully found spawn for food on map and returned it as a tuple


if __name__ == "__main__":
    unittest.main()
