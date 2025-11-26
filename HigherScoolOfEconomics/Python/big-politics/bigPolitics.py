def bigPolitics(p: list) -> int:
    ''':param p: список населения всех провинций
       :return: количество паспортов, которые надо будет выдать'''
    p.sort()
    prev = 0
    while len(p) > 1:
        p.append(p[0] + p[1])
        prev = p[0] + p[1] + prev
        del (p[0], p[0])
        p.sort()
    return prev
