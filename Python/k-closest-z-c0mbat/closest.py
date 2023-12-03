def closest(array: list, target: int, count: int) -> list:
    """Находит в упорядоченном массиве `array` `count` чисел, ближайших по значению к `target`.
    :param array: массив, в котором идёт поиск
    :param target: число, от которого отсчитываются ближайшие
    :param count: количество чисел, которые необходимо выдать
    """
    i = len(array) // 2  # индекс
    low = 0  # нижний индекс в рассматриваемом массиве
    top = len(array) - 1  # верхний индекс в рассматриваемом массиве
    res = []  # итоговый массив
    found = False  # нашелся ли элемент target в array
    if len(array) > 1:
        if array[i] == target:
            found = True
            res.append(array[i])
        else:
            if target < array[0]:  # если target меньше нулевого элемента массива
                found = True
                target = array[0]
                res.append(array[0])
            if target > array[len(array) - 1]:  # если target больше последнего элемента массива
                found = True
                target = array[len(array) - 1]
                res.append(array[len(array) - 1])
        while array[i] != target and not found:  # поиск элемента
            if target > array[i]:
                low = i + 1
            else:
                top = i - 1
            i = (low + top) // 2
            if array[i] == target:  # если нашелся элемент в массиве
                found = True
                res.append(array[i])
            else:  # если элемента в массиве нет, но нашлись два ближайших
                if array[i] < target < array[i + 1]:
                    res.append(array[i])
                    break

        a = 1
        b = 1
        while len(res) < count:  # заполняем результирующий массив
            if i - a >= 0 and i + b < len(array):
                if target - array[i - a] <= array[i + b] - target:
                    res.append(array[i - a])
                    a += 1
                else:
                    res.append(array[i + b])
                    b += 1
            else:
                if i - a < 0:
                    res.append(array[i + b])
                    b += 1
                elif i + b >= len(array):
                    res.append(array[i - a])
                    a += 1
        res.sort()
        return res
    else:
        return array
