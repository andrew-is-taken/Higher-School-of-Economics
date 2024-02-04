import random


def genMap(size_x, size_y, k_barriers) -> list:
    """
    size_x: int, map horizontal size(min 15)
    size_y: int, map vertical size(min 15)
    k_barriers: int, amount of barriers in the map
    Generates map where:
    'Y' is empty field
    '#' is map border
    'B' is barrier
    """
    map = []
    line = []

    for i in range(size_x):  # filling top wall
        line.append('#')
    map.append(line)

    for i in range(size_y - 2):  # filling main part of the map and left and right walls
        x = []
        x.append('#')
        for j in range(size_x - 2):
            x.append('Y')
        x.append('#')
        map.append(x)
    map.append(line)  # filling bottom wall

    for i in range(k_barriers):  # creating barriers
        length = random.randint(3, 6)
        if (random.randint(0, 10) < 5):  # horizontal barrier
            start_coord = (random.randint(2, size_x - length - 2), random.randint(2, size_y - 3))
            for j in range(length):
                map[start_coord[1]][start_coord[0] + j] = 'B'
        else:  # vertical barrier
            start_coord = (random.randint(2, size_x - 3), random.randint(2, size_y - length - 2))
            for j in range(length):
                map[start_coord[1] + j][start_coord[0]] = 'B'

    '''For debug. To see generated map in terminal'''
    # for i in range(len(map)):
    #    print(map[i])

    return map
