from typing import List


def min_digits_sum(arr: List[int]) -> int:
    res = ['', '']
    arr = sorted(arr)
    lastWasFirst = False
    kNull = arr.count(0)
    for i in range(kNull, len(arr)):
        temp = str(arr[i])
        if lastWasFirst:
            res[1] += temp
            lastWasFirst = False
        else:
            res[0] += temp
            lastWasFirst = True
    if res[0] == '':
        res[0] = '0'
    if res[1] == '':
        res[1] = '0'
    return int(res[0]) + int(res[1])
