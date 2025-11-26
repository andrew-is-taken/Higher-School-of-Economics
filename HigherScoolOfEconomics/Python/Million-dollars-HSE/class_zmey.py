# from _typeshed import Self

from pygame.sprite import RenderClear
from variables import *
import random
from spawnSimpleEnemy import findEntitySpawn
from deployMap import UpdateScoreText
from pacman import *


def test():
    Zmeyka.spawn()


class Zmeyka:
    '''
    __init__: class generator
    pos_x: x position
    pos_y: y position
    segmentsPositions: segment position
    speed: object speed
    timer: game timer
    timerFood: food spawn timer
    foodInMap: where is the food on the map
    length: snake length
    sprite_width: sprite dimensions
    Function creates variables for the snake class
    '''

    def __init__(self, game_map, cell_width):
        self.screen = pg.Surface((37, 37), pg.SRCALPHA)
        self.cell_width = cell_width
        self.pos_x = None
        self.pos_y = None
        self.segmentsPositions = []
        self.length = None
        self.finished = False
        self.direction = None
        self.justAteSomething = False
        self.max_speed = 2
        self.speed = self.max_speed
        self.game_map = game_map
        self.timer = 0
        self.timerFood = 0
        self.foodInMap = []
        self.food = pg.image.load('static/star.png')
        self.Font = pg.font.SysFont('Comic Sans MS', 30)
        self.sprite_width = 34
        self.pac = PacMan(self.game_map, 30, self.screen, self)
        self.spawn()

    def eatStar(self, id):
        '''
        eatStar: class generator
        segmentsPositions: segment position
        length: snake length
        foodInMap: where is the food on the map
        game_map: big map of the game
        Function for eating stars
        '''
        self.segmentsPositions.append(self.segmentsPositions[len(self.segmentsPositions) - 1].copy())
        self.length += 1
        self.justAteSomething = True
        self.foodInMap.pop(id)
        for i in range(len(self.foodInMap)):
            self.game_map[self.foodInMap[i][1]][self.foodInMap[i][0]] = i

    def spawn(self):
        '''
        pos_x: x position
        pos_y: y position
        direction: direction of travel
        segmentsPositions: segment position
        case: random spawn number
        Function randomly spawn a snake
        '''
        case = random.randint(0, 3)
        self.pac.case = case

        if (case == 0):
            self.direction = 'R'
            self.pos_x = len(self.game_map[0]) // 2
            self.pos_y = 1
            self.length = 5
            self.segmentsPositions = [[self.pos_x - 4, self.pos_y], [self.pos_x - 3, self.pos_y],
                                      [self.pos_x - 2, self.pos_y], [self.pos_x - 1, self.pos_y],
                                      [self.pos_x, self.pos_y]]
        elif (case == 1):
            self.direction = 'L'
            self.pos_x = len(self.game_map[0]) // 2
            self.pos_y = len(self.game_map) - 2
            self.length = 5
            self.segmentsPositions = [[self.pos_x + 4, self.pos_y], [self.pos_x + 3, self.pos_y],
                                      [self.pos_x + 2, self.pos_y], [self.pos_x + 1, self.pos_y],
                                      [self.pos_x, self.pos_y]]
        elif (case == 2):
            self.direction = 'U'
            self.pos_x = 1
            self.pos_y = len(self.game_map) // 2
            self.length = 5
            self.segmentsPositions = [[self.pos_x, self.pos_y + 4], [self.pos_x, self.pos_y + 3],
                                      [self.pos_x, self.pos_y + 2], [self.pos_x, self.pos_y + 1],
                                      [self.pos_x, self.pos_y]]
        elif (case == 3):
            self.direction = 'D'
            self.pos_x = len(self.game_map[0]) - 2
            self.pos_y = len(self.game_map) // 2
            self.length = 5
            self.segmentsPositions = [[self.pos_x, self.pos_y - 4], [self.pos_x, self.pos_y - 3],
                                      [self.pos_x, self.pos_y - 2], [self.pos_x, self.pos_y - 1],
                                      [self.pos_x, self.pos_y]]
        self.render()

    def render(self):
        '''
        sprite_name: name of log png
        current_sprite: the sprite we selected
        direction: direction of travel
        length: snake length
        foodInMap: where is the food on the map
        segmentsPositions: segment position
        Function loads the snake picture
        '''
        sprite_name = 'static/zmeySprite.png'
        current_sprite = pg.image.load(sprite_name)
        for i in range(len(self.segmentsPositions)):
            self.screen.blit(current_sprite, (30 * self.segmentsPositions[i][0], 30 * self.segmentsPositions[i][1]))
        for i in range(len(self.foodInMap)):
            self.screen.blit(self.food, (self.foodInMap[i][0] * 30, self.foodInMap[i][1] * 30))
        UpdateScoreText(self.length, self.screen, self.Font, 1050)

    def update(self, game_map, user_input):
        '''
        timer: game timer
        game_map: big map of the game
        finished: is game finished
        timerFood: food spawn timer
        foodInMap: where is the food on the map
        Function updating the picture in the game
        '''
        if (not self.finished):
            self.timer += 0.25
            if self.timer > 3:
                self.timer = 0
                self.game_map = game_map
                self.move()
                if (self.finished):
                    return
            self.timerFood += 1
            if self.timerFood > 60:
                self.timerFood = 0
                spawn_coord = findEntitySpawn(self.game_map, 1)[0]
                self.foodInMap.append(spawn_coord)
                self.game_map[spawn_coord[1]][spawn_coord[0]] = len(self.foodInMap) - 1
            self.process_user_input(user_input)
            self.render()

    def process_user_input(self, user_input):
        '''
        direction: direction of travel
        Function of user input
        '''
        if user_input[hot_keys['Left']]:
            if (self.direction != 'R'):
                self.direction = 'L'
        if user_input[hot_keys['Up']]:
            if (self.direction != 'D'):
                self.direction = 'U'
        if user_input[hot_keys['Down']]:
            if (self.direction != 'U'):
                self.direction = 'D'
        if user_input[hot_keys['Right']]:
            if (self.direction != 'L'):
                self.direction = 'R'

    def movement_logic(self):
        '''
        pos_x: x position
        pos_y: y position
        game_map: big map of the game
        finished: is game finished
        Function move logic
        '''
        if (self.game_map[self.pos_y][self.pos_x] == '#' or self.game_map[self.pos_y][self.pos_x] == 'B' or
                self.game_map[self.pos_y][self.pos_x] == 'S'):
            self.finished = True
            return
        elif (type(self.game_map[self.pos_y][self.pos_x]) is int):
            self.eatStar(self.game_map[self.pos_y][self.pos_x])

    def move(self):
        '''
        pos_x: x position
        pos_y: y position
        game_map: big map of the game
        direction: direction of travel
        segmentsPositions: segment position
        justAteSomething: where is
        Function all movements of the snake on the map
        '''
        if self.direction == 'U':
            self.pos_y -= 1
            if (self.justAteSomething):
                self.segmentsPositions[len(self.segmentsPositions) - 1][1] -= 1
                self.justAteSomething = False
                self.game_map[self.segmentsPositions[len(self.segmentsPositions) - 1][1]][
                    self.segmentsPositions[len(self.segmentsPositions) - 1][0]] = 'Y'
            else:
                self.game_map[self.segmentsPositions[0][1]][self.segmentsPositions[0][0]] = 'Y'
                for i in range(1, self.length):
                    self.segmentsPositions[i - 1] = self.segmentsPositions[i].copy()
                self.segmentsPositions[len(self.segmentsPositions) - 1][1] -= 1
                self.game_map[self.segmentsPositions[len(self.segmentsPositions) - 2][1]][
                    self.segmentsPositions[len(self.segmentsPositions) - 2][0]] = 'S'
        elif self.direction == 'D':
            self.pos_y += 1
            if (self.justAteSomething):
                self.segmentsPositions[len(self.segmentsPositions) - 1][1] += 1
                self.justAteSomething = False
                self.game_map[self.segmentsPositions[len(self.segmentsPositions) - 2][1]][
                    self.segmentsPositions[len(self.segmentsPositions) - 2][0]] = 'Y'
            else:
                self.game_map[self.segmentsPositions[0][1]][self.segmentsPositions[0][0]] = 'Y'
                for i in range(1, self.length):
                    self.segmentsPositions[i - 1] = self.segmentsPositions[i].copy()
                self.segmentsPositions[len(self.segmentsPositions) - 1][1] += 1
                self.game_map[self.segmentsPositions[len(self.segmentsPositions) - 2][1]][
                    self.segmentsPositions[len(self.segmentsPositions) - 2][0]] = 'S'
        elif self.direction == 'R':
            self.pos_x += 1
            if (self.justAteSomething):
                self.segmentsPositions[len(self.segmentsPositions) - 1][0] += 1
                self.justAteSomething = False
                self.game_map[self.segmentsPositions[len(self.segmentsPositions) - 2][1]][
                    self.segmentsPositions[len(self.segmentsPositions) - 2][0]] = 'Y'
            else:
                self.game_map[self.segmentsPositions[0][1]][self.segmentsPositions[0][0]] = 'Y'
                for i in range(1, self.length):
                    self.segmentsPositions[i - 1] = self.segmentsPositions[i].copy()
                self.segmentsPositions[len(self.segmentsPositions) - 1][0] += 1
                self.game_map[self.segmentsPositions[len(self.segmentsPositions) - 2][1]][
                    self.segmentsPositions[len(self.segmentsPositions) - 2][0]] = 'S'
        elif self.direction == 'L':
            self.pos_x -= 1
            if (self.justAteSomething):
                self.segmentsPositions[len(self.segmentsPositions) - 1][0] -= 1
                self.justAteSomething = False
                self.game_map[self.segmentsPositions[len(self.segmentsPositions) - 2][1]][
                    self.segmentsPositions[len(self.segmentsPositions) - 2][0]] = 'Y'
            else:
                self.game_map[self.segmentsPositions[0][1]][self.segmentsPositions[0][0]] = 'Y'
                for i in range(1, self.length):
                    self.segmentsPositions[i - 1] = self.segmentsPositions[i].copy()
                self.segmentsPositions[len(self.segmentsPositions) - 1][0] -= 1
                self.game_map[self.segmentsPositions[len(self.segmentsPositions) - 2][1]][
                    self.segmentsPositions[len(self.segmentsPositions) - 2][0]] = 'S'
        self.pos_x = self.segmentsPositions[len(self.segmentsPositions) - 1][0]
        self.pos_y = self.segmentsPositions[len(self.segmentsPositions) - 1][1]
        self.movement_logic()

    def snakeBrake(self, dir):
        '''
        img: black finish game
        Function brake the game and snake
        '''
        img = pg.image.load('static/blackSurface.png')
        self.screen.blit(img, (30 * self.pos_x, 30 * self.pos_y))
