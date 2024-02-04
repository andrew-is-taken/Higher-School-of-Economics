import random


def findEntitySpawn(map, Type) -> int:
    '''
    map: list, generated map
    type: int, 0 - ghost enemy(dynamic), 1-food(static)
    Function finds a position in generated map to spawn entity(ghost enemy or food for snake)
    Returns:
    tuple: available spawn coordinates, int: available direction of movement, int: available movement distance in desired direction
    '''
    spawn_coord = (random.randint(3, len(map[0]) - 4), random.randint(3, len(map) - 4))
    available_movement_dir = 0  # 0-horizontal 1-vertical
    available_movement_delta = (len(map[0]) + len(map)) // 5  # max movement distance from spawn coord
    if (Type == 0):  # spawning ghost enemy
        while map[spawn_coord[1]][spawn_coord[0]] == 'B' or map[spawn_coord[1]][spawn_coord[0]] == 'S':
            x = random.randint(3, len(map[0]) - 4)
            y = random.randint(3, len(map) - 4)
            spawn_coord = (x, y)

        x = spawn_coord[0]
        y = spawn_coord[1]
        available_movement_dir = random.randint(0, 1)

        if (available_movement_dir == 0):
            # checks if can move in desired direction, if can't checks another axis for movement,
            # if also can't move on new axis, searching for new spawn
            f = checkHorMovement(available_movement_delta, x, y, map)
            if (f[0]):
                spawn_coord = (f[2], f[3])
                available_movement_dir = 0
                available_movement_delta = f[1]
            else:
                f = checkVertMovement(available_movement_delta, y, x, map)
                if (f[0]):
                    spawn_coord = (f[2], f[3])
                    available_movement_dir = 1
                    available_movement_delta = f[1]
                else:
                    findEntitySpawn(map, 0)
        else:
            # checks if can move in desired direction, if can't checks another axis for movement,
            # if also can't move on new axis, searching for new spawn
            f = checkVertMovement(available_movement_delta, y, x, map)
            if (f[0]):
                spawn_coord = (f[2], f[3])
                available_movement_dir = 1
                available_movement_delta = f[1]
            else:
                f = checkHorMovement(available_movement_delta, x, y, map)
                if (f[0]):
                    spawn_coord = (f[2], f[3])
                    available_movement_dir = 0
                    available_movement_delta = f[1]
                else:
                    findEntitySpawn(map, 0)
    else:  # spawning food
        while map[spawn_coord[1]][spawn_coord[0]] == 'B' or map[spawn_coord[1]][spawn_coord[0]] == 'S' or (
                type(map[spawn_coord[1]][spawn_coord[0]]) is int):
            x = random.randint(3, len(map[0]) - 3)
            y = random.randint(3, len(map) - 3)
            spawn_coord = (x, y)
    '''available_movement_dir: int, 0-horizontal, 1-vertical'''
    return spawn_coord, available_movement_dir, available_movement_delta


def checkHorMovement(available_movement_delta, x, y, map):
    '''
    available_movement_delta: distance to move
    x: int, map horizontal size
    y: int, map vertical size
    map: generated map as list
    Function checks if ghost can move on horizontal axis
    '''
    max_right = 0
    max_left = 0
    canMoveHor = False
    for i in range(1, available_movement_delta + 1):
        if (map[y][x + i] == 'B' or map[y][x + i] == '#'):
            max_right = i - 1
            break
        else:
            max_right = i
    if (max_right < available_movement_delta):
        for i in range(1, available_movement_delta - max_right + 1):
            if (map[y][x - i] == 'B' or map[y][x - i] == '#'):
                max_left = i - 1
                break
            else:
                max_left = i
    if (max_right + max_left > 3):
        if (max_left > 0):
            x -= max_left
        available_movement_delta = max_left + max_right
        canMoveHor = True
    return canMoveHor, available_movement_delta, x, y


def checkVertMovement(available_movement_delta, y, x, map):
    '''
    available_movement_delta: distance to move
    x: int, map horizontal size
    y: int, map vertical size
    map: generated map as list
    Function checks if ghost can move on vertical axis
    '''
    max_down = 0
    max_up = 0
    canMoveVert = False
    for i in range(1, available_movement_delta + 1):
        if (map[y + i][x] == 'B' or map[y + i][x] == '#'):
            max_down = i - 1
            break
        else:
            max_down = i
    if (max_down < available_movement_delta):
        for i in range(1, available_movement_delta - max_down + 1):
            if (map[y - i][x] == 'B' or map[y - i][x] == '#'):
                max_up = i - 1
                break
            else:
                max_up = i
    if (max_down + max_up > 3):
        if (max_up > 0):
            y -= max_up
        available_movement_delta = max_up + max_down
        canMoveVert = True
    return canMoveVert, available_movement_delta, x, y
