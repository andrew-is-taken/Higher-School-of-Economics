from typing import List, Tuple
import math

Point = Tuple[float, float]


def distance(a: Point, b: Point):
    '''Finds the distance between two points'''
    return math.hypot(a[0] - b[0], a[1] - b[1])


def search(P, n):
    min_val = float('inf')
    minA = (0, 0)
    minB = (0, 0)
    for i in range(n):
        for j in range(i + 1, n):
            if distance(P[i], P[j]) < min_val:
                min_val = distance(P[i], P[j])
                minA, minB = P[i], P[j]

    return min_val, minA, minB


def findClosest(points):
    n = len(points)

    if n <= 3:
        return search(points, n)[0]

    points_l = [points[x] for x in range(0, n // 2)]
    points_r = [points[x] for x in range(n // 2, n)]

    dl = findClosest(points_l)
    dr = findClosest(points_r)

    d = min(dl, dr)
    return d


def corridor(points, midPoint, minD):
    newPoints = []
    for i in range(0, len(points)):
        if points[i][0] >= midPoint[0] - minD and points[i][0] <= midPoint[0] + minD:
            newPoints.append(points[i])
        else:
            if points[i][0] > midPoint[0] + minD:
                break
    points = sorted(newPoints, key=lambda y: y[1])
    res = search(points, len(points))
    return res


def closest_pair_of_points(points: List[Point]) \
        -> Tuple[float, Point, Point]:
    '''Finds the closest pair of points in the list'''
    points = sorted(points, key=lambda x: x[0])
    mid = len(points) // 2
    midPoint = points[mid]
    if len(points) > 3:
        minD = findClosest(points)
        newD = corridor(points, midPoint, minD)
        return newD
    else:
        return search(points, len(points))
