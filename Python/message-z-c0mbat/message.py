def message(string: str) -> int:
    """
    Находит количество `quantity` различных комбинаций букв, которые
    при кодировании заданным методом дают строку `string`
    """

    last_symbol = int(string[0])
    if last_symbol == 0:
        a = 1
    else:
        if last_symbol > 3:
            a = 1
        else:
            if int(string[1]) > 3:
                a = 1
            else:
                a = 2
    k_solo_a = 1
    last_symbol = int(string[1])

    for i in range(2, len(string)):
        if int(string[i]) > 3:
            if last_symbol != 0:
                if last_symbol < 3:
                    b = a - k_solo_a
                    a = k_solo_a * 2 + b
                    k_solo_a = b + k_solo_a
                else:
                    k_solo_a = a
            else:
                k_solo_a = a
        else:
            if last_symbol != 0:
                if last_symbol <= 3:
                    b = a - k_solo_a
                    a = k_solo_a * 2 + b
                    k_solo_a = b + k_solo_a
                else:
                    k_solo_a = a
            else:
                k_solo_a = a
        last_symbol = int(string[i])

    return a
