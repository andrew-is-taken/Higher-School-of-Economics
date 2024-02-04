import unittest


class functionalityTest(unittest.TestCase):
    def test_spawn(self):
        sprite_sequence_L = []
        sprite_sequence_R = []
        for i in range(1, 10):
            sprite_sequence_L.append('static/packmanSequence/movementLeft/000' + str(i) + '.png')
        for i in range(11, 16):
            sprite_sequence_L.append('static/packmanSequence/movementLeft/00' + str(i) + '.png')
        for i in range(1, 10):
            sprite_sequence_R.append('static/packmanSequence/movementRight/000' + str(i) + '.png')
        for i in range(11, 16):
            sprite_sequence_R.append('static/packmanSequence/movementRight/00' + str(i) + '.png')
        print(sprite_sequence_L, sprite_sequence_R)
        self.assertEqual(len(sprite_sequence_L), 14)
        self.assertEqual(len(sprite_sequence_R), 14)


if __name__ == "__main__":
    unittest.main()
