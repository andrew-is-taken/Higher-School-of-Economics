def sums(array: list) -> int:
    """Находит количество различных сумм вида K1*A1 + K2*A2 + ... + KN*AN
    :param array: массив целых чисел, содержащий значений A1,A2...
    """
    array.sort()
    if array[0] == 0 and array[len(array) - 1] == 0:
        return 1
    else:
        sum = {0: 1}
        sum_dop = []
        for i in array:
            for j in sum.keys():
                sum_dop.append(i + j)
            for x in range(len(sum_dop)):
                sum[sum_dop[x]] = 1
            sum_dop = []
        return len(sum.keys())
