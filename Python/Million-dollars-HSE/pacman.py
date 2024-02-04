from variables import *
from spawnSimpleEnemy import findEntitySpawn
from class_zmey import *
import random


class PacMan:
    '''
       __init__: class generator
       pos_x: x position
       pos_y: y position
       speed: object speed
       sprite_sequence: array for storing sprites
       game_map: big map of the game
       timer: game timer
       sprite_width: sprite dimensions
       '''

    def __init__(self, game_map, cell_width, screen, zmeyka):
        self.screen = screen
        self.zmeykaObj = zmeyka
        self.cell_width = cell_width
        self.screen_pos_x = None
        self.screen_pos_y = None
        self.pos_x = 10
        self.pos_y = 10
        self.sprite_sequence_L = []
        self.sprite_sequence_R = []
        self.isit = False
        self.max_speed = 2
        self.speed = self.max_speed
        self.direction = 'R'  # R, D, L, U
        self.game_map = game_map
        self.case = None
        self.timer = 0
        self.sprite_timer = 0
        self.sprite_width = 34
        self.spawn()

    def spawn(self):
        '''
            pos_x: x position
            pos_y: y position
            Function: array for storing sprites
               '''
        res = findEntitySpawn(self.game_map, 1)
        self.pos_x, self.pos_y = res[0][0], res[0][1]
        for i in range(1, 10):
            self.sprite_sequence_L.append('static/packmanSequence/movementLeft/000' + str(i) + '.png')
        for i in range(11, 16):
            self.sprite_sequence_L.append('static/packmanSequence/movementLeft/00' + str(i) + '.png')
        for i in range(1, 10):
            self.sprite_sequence_R.append('static/packmanSequence/movementRight/000' + str(i) + '.png')
        for i in range(11, 16):
            self.sprite_sequence_R.append('static/packmanSequence/movementRight/00' + str(i) + '.png')
        self.render()

    def render(self):
        '''
        sprite_name: name of log png
        current_sprite: the sprite we selected
        direction: direction of travel
        Function loads the pacman picture
        '''
        if not self.isit:
            self.sprite_timer += 1
            if self.direction == 'L':
                current_sprite = pg.image.load(self.sprite_sequence_L[self.sprite_timer])
                current_sprite = pg.transform.scale(current_sprite, (
                current_sprite.get_rect()[2] // 4, current_sprite.get_rect()[3] // 4))
            elif self.direction == 'R':
                current_sprite = pg.image.load(self.sprite_sequence_R[self.sprite_timer])
                current_sprite = pg.transform.scale(current_sprite, (
                current_sprite.get_rect()[2] // 4, current_sprite.get_rect()[3] // 4))
            elif self.direction == 'U':
                current_sprite = pg.image.load('static/packmanSequence/moveUp.png')
                current_sprite = pg.transform.scale(current_sprite, (
                current_sprite.get_rect()[2] // 4, current_sprite.get_rect()[3] // 4))
            elif self.direction == 'D':
                current_sprite = pg.image.load('static/packmanSequence/moveDown.png')
                current_sprite = pg.transform.scale(current_sprite, (
                current_sprite.get_rect()[2] // 4, current_sprite.get_rect()[3] // 4))
            if self.sprite_timer >= 13:
                self.isit = True
        else:
            self.sprite_timer -= 1
            if self.direction == 'L':
                current_sprite = pg.image.load(self.sprite_sequence_L[self.sprite_timer])
                current_sprite = pg.transform.scale(current_sprite, (
                current_sprite.get_rect()[2] // 4, current_sprite.get_rect()[3] // 4))
            elif self.direction == 'R':
                current_sprite = pg.image.load(self.sprite_sequence_R[self.sprite_timer])
                current_sprite = pg.transform.scale(current_sprite, (
                current_sprite.get_rect()[2] // 4, current_sprite.get_rect()[3] // 4))
            elif self.direction == 'U':
                current_sprite = pg.image.load('static/packmanSequence/moveUp.png')
                current_sprite = pg.transform.scale(current_sprite, (
                current_sprite.get_rect()[2] // 4, current_sprite.get_rect()[3] // 4))
            elif self.direction == 'D':
                current_sprite = pg.image.load('static/packmanSequence/moveDown.png')
                current_sprite = pg.transform.scale(current_sprite, (
                current_sprite.get_rect()[2] // 4, current_sprite.get_rect()[3] // 4))
            if self.sprite_timer <= 2:
                self.isit = False
        self.screen.blit(current_sprite, (30 * self.pos_x, 30 * self.pos_y))

    def update(self, game_map):
        '''
            timer: game timer
            game_map: big map of the game
            Function updating the picture in the game
                '''
        self.timer += 0.25
        if self.timer > 3:
            self.timer = 0
            self.movement_logic()
        self.game_map = game_map
        self.render()

    def movement_logic(self):
        '''
            pos_x: x position
            pos_y: y position
            game_map: big map of the game
            Function move logic
            Direction: direction of movement
            '''
        if (self.game_map[self.pos_y][self.pos_x] == 'S' or self.game_map[self.pos_y][self.pos_x + 1] == 'S'
                or self.game_map[self.pos_y][self.pos_x - 1] == 'S' or self.game_map[self.pos_y + 1][self.pos_x] == 'S'
                or self.game_map[self.pos_y - 1][self.pos_x] == 'S'):
            self.zmeykaObj.finished = True
            return
        if (self.direction == 'R'):
            if (self.game_map[self.pos_y][self.pos_x + 1] == 'S'):
                self.zmeykaObj.finished = True
                return
            elif (self.game_map[self.pos_y][self.pos_x + 1] == '#' or self.game_map[self.pos_y][self.pos_x + 1] == 'B'):
                newdir = random.randint(0, 2)
                if (newdir == 0):
                    self.direction = 'L'
                elif (newdir == 1):
                    self.direction = 'U'
                elif (newdir == 2):
                    self.direction = 'D'
                self.movement_logic()
                return
            else:
                newdir = random.randint(0, 5)
                if (newdir < 3):
                    self.direction = 'R'
                    if (self.game_map[self.pos_y][self.pos_x + 1] == '#' or self.game_map[self.pos_y][
                        self.pos_x + 1] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 3):
                    self.direction = 'U'
                    if (self.game_map[self.pos_y - 1][self.pos_x] == '#' or self.game_map[self.pos_y - 1][
                        self.pos_x] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 4):
                    self.direction = 'L'
                    if (self.game_map[self.pos_y][self.pos_x - 1] == '#' or self.game_map[self.pos_y][
                        self.pos_x - 1] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 5):
                    self.direction = 'D'
                    if (self.game_map[self.pos_y + 1][self.pos_x] == '#' or self.game_map[self.pos_y + 1][
                        self.pos_x] == 'B'):
                        self.movement_logic()
                        return
        elif (self.direction == 'L'):
            if (self.game_map[self.pos_y][self.pos_x - 1] == 'S'):
                self.zmeykaObj.finished = True
                return
            elif (self.game_map[self.pos_y][self.pos_x - 1] == '#' or self.game_map[self.pos_y][self.pos_x - 1] == 'B'):
                newdir = random.randint(0, 2)
                if (newdir == 0):
                    self.direction = 'R'
                elif (newdir == 1):
                    self.direction = 'U'
                elif (newdir == 2):
                    self.direction = 'D'
                self.movement_logic()
                return
            else:
                newdir = random.randint(0, 5)
                if (newdir < 3):
                    self.direction = 'L'
                    if (self.game_map[self.pos_y][self.pos_x - 1] == '#' or self.game_map[self.pos_y][
                        self.pos_x - 1] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 3):
                    self.direction = 'R'
                    if (self.game_map[self.pos_y][self.pos_x + 1] == '#' or self.game_map[self.pos_y][
                        self.pos_x + 1] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 4):
                    self.direction = 'U'
                    if (self.game_map[self.pos_y - 1][self.pos_x] == '#' or self.game_map[self.pos_y - 1][
                        self.pos_x] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 5):
                    self.direction = 'D'
                    if (self.game_map[self.pos_y + 1][self.pos_x] == '#' or self.game_map[self.pos_y + 1][
                        self.pos_x] == 'B'):
                        self.movement_logic()
                        return
        elif (self.direction == 'U'):
            if (self.game_map[self.pos_y - 1][self.pos_x] == 'S'):
                self.zmeykaObj.finished = True
                return
            elif (self.game_map[self.pos_y - 1][self.pos_x] == '#' or self.game_map[self.pos_y - 1][self.pos_x] == 'B'):
                newdir = random.randint(0, 2)
                if (newdir == 0):
                    self.direction = 'R'
                elif (newdir == 1):
                    self.direction = 'L'
                elif (newdir == 2):
                    self.direction = 'D'
                self.movement_logic()
                return
            else:
                newdir = random.randint(0, 5)
                if (newdir < 3):
                    self.direction = 'U'
                    if (self.game_map[self.pos_y - 1][self.pos_x] == '#' or self.game_map[self.pos_y - 1][
                        self.pos_x] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 3):
                    self.direction = 'R'
                    if (self.game_map[self.pos_y][self.pos_x + 1] == '#' or self.game_map[self.pos_y][
                        self.pos_x + 1] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 4):
                    self.direction = 'L'
                    if (self.game_map[self.pos_y][self.pos_x - 1] == '#' or self.game_map[self.pos_y][
                        self.pos_x - 1] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 5):
                    self.direction = 'D'
                    if (self.game_map[self.pos_y + 1][self.pos_x] == '#' or self.game_map[self.pos_y + 1][
                        self.pos_x] == 'B'):
                        self.movement_logic()
                        return
        elif (self.direction == 'D'):
            if (self.game_map[self.pos_y + 1][self.pos_x] == 'S'):
                self.zmeykaObj.finished = True
                return
            elif (self.game_map[self.pos_y + 1][self.pos_x] == '#' or self.game_map[self.pos_y + 1][self.pos_x] == 'B'):
                newdir = random.randint(0, 2)
                if (newdir == 0):
                    self.direction = 'R'
                elif (newdir == 1):
                    self.direction = 'L'
                elif (newdir == 2):
                    self.direction = 'U'
                self.movement_logic()
                return
            else:
                newdir = random.randint(0, 5)
                if (newdir < 3):
                    self.direction = 'D'
                    if (self.game_map[self.pos_y + 1][self.pos_x] == '#' or self.game_map[self.pos_y + 1][
                        self.pos_x] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 3):
                    self.direction = 'R'
                    if (self.game_map[self.pos_y][self.pos_x + 1] == '#' or self.game_map[self.pos_y][
                        self.pos_x + 1] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 4):
                    self.direction = 'L'
                    if (self.game_map[self.pos_y][self.pos_x - 1] == '#' or self.game_map[self.pos_y][
                        self.pos_x - 1] == 'B'):
                        self.movement_logic()
                        return
                elif (newdir == 5):
                    self.direction = 'U'
                    if (self.game_map[self.pos_y - 1][self.pos_x] == '#' or self.game_map[self.pos_y - 1][
                        self.pos_x] == 'B'):
                        self.movement_logic()
                        return
        self.move()

    def move(self):
        '''
        pos_x: x position
        pos_y: y position
        direction: direction of travel
        '''
        if self.direction == 'U':
            self.pos_y -= 1
        elif (self.direction == 'D'):
            self.pos_y += 1
        elif (self.direction == 'R'):
            self.pos_x += 1
        elif (self.direction == 'L'):
            self.pos_x -= 1
