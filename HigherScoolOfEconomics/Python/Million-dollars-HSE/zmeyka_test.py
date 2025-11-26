import unittest
from class_zmey import Zmeyka
import random
import pygame


class functionalityTest(unittest.TestCase):
    def test_spawn(self):
        case = 0  # желаемый кейс

        if case == 0:
            self.direction = 'R'
            self.pos_x = 15
            self.pos_y = 1
            self.length = 5
            self.segmentsPositions = [[self.pos_x - 4, self.pos_y], [self.pos_x - 3, self.pos_y],
                                      [self.pos_x - 2, self.pos_y], [self.pos_x - 1, self.pos_y],
                                      [self.pos_x, self.pos_y]]
        elif case == 1:
            self.direction = 'L'
            self.pos_x = 15
            self.pos_y = 28
            self.length = 5
            self.segmentsPositions = [[self.pos_x + 4, self.pos_y], [self.pos_x + 3, self.pos_y],
                                      [self.pos_x + 2, self.pos_y], [self.pos_x + 1, self.pos_y],
                                      [self.pos_x, self.pos_y]]
        elif case == 2:
            self.direction = 'U'
            self.pos_x = 1
            self.pos_y = 15
            self.length = 5
            self.segmentsPositions = [[self.pos_x, self.pos_y + 4], [self.pos_x, self.pos_y + 3],
                                      [self.pos_x, self.pos_y + 2], [self.pos_x, self.pos_y + 1],
                                      [self.pos_x, self.pos_y]]
        elif case == 3:
            self.direction = 'D'
            self.pos_x = 28
            self.pos_y = 15
            self.length = 5
            self.segmentsPositions = [[self.pos_x, self.pos_y - 4], [self.pos_x, self.pos_y - 3],
                                      [self.pos_x, self.pos_y - 2], [self.pos_x, self.pos_y - 1],
                                      [self.pos_x, self.pos_y]]
        print(self.segmentsPositions)


if __name__ == "__main__":
    unittest.main()
