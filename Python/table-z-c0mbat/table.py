def table(n: int, m: int, r: int, firstRow: list) -> list:
    '''Находит последнюю строку таблицы размера nxm
    :param
    n - количество строк
    m - количество столбов
    r - модуль, по которому выполняются вычисления
    firstRow - первая строка таблицы
    lastRow - последняя строка таблицы'''

    a = [[0] * m for i in range(3)]
    a[0] = firstRow
    profile = [0 for i in range(m)]
    diagonal_r = [0 for i in range(m)]
    diagonal_l = [0 for i in range(m)]
    a[1][0] = (a[0][1] + a[0][0]) % r
    profile[0] = (2 * a[1][0]) % r
    diagonal_r[0] = a[0][1]
    a[1][m - 1] = (a[0][m - 2] + a[0][m - 1]) % r
    profile[m - 1] = (2 * a[1][m - 1]) % r
    diagonal_l[m - 1] = a[0][m - 2]

    for j in range(1, m - 1):
        a[1][j] = (a[0][j - 1] + a[0][j] + a[0][j + 1]) % r
        profile[j] = (2 * a[1][j]) % r
        diagonal_r[j] = a[0][j + 1]
        diagonal_l[j] = a[0][j - 1]
    old_diag_r = [i for i in diagonal_r]
    old_diag_l = [i for i in diagonal_l]

    for i in range(2, n):
        a[2][0] = (old_diag_r[1] + a[1][1] + profile[0]) % r
        profile[0] = (2 * a[2][0]) % r
        diagonal_r[0] = (old_diag_r[1] + a[1][1]) % r
        a[2][m - 1] = (old_diag_l[m - 2] + a[1][m - 2] + profile[m - 1]) % r
        profile[m - 1] = (2 * a[2][m - 1]) % r
        diagonal_l[m - 1] = (old_diag_l[m - 2] + a[1][m - 2]) % r
        for j in range(1, m - 1):
            a[2][j] = (old_diag_r[j + 1] + a[1][j + 1] + old_diag_l[j - 1] + a[1][j - 1] + profile[j]) % r
            profile[j] = (2 * a[2][j]) % r
            diagonal_r[j], diagonal_l[j] = (old_diag_r[j + 1] + a[1][j + 1]) % r, (old_diag_l[j - 1] + a[1][j - 1]) % r
        old_diag_r = [i for i in diagonal_r]
        old_diag_l = [i for i in diagonal_l]
        a[1] = [i for i in a[2]]

    if n > 2:
        lastRow = a[2]
    elif n == 2:
        lastRow = a[1]
    else:
        lastRow = a[0]

    return lastRow
