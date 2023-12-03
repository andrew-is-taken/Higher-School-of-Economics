def decode(string):
    res = ''
    s = list(string)
    kol = ''
    while len(s) > 0:
        if s[0].isdigit():
            kol += s[0]
            del (s[0])
        else:
            if kol.isdigit():
                res += s[0] * int(kol)
                kol = ''
                del (s[0])
            else:
                res += s[0]
                del (s[0])
    return res


def encode(string):
    k = 1
    res = ''
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            k += 1
        else:
            if k == 1:
                res += string[i - 1]
            else:
                res += str(k) + string[i - 1]
            k = 1
        if i == len(string) - 1:
            if k == 1:
                res += string[i]
            else:
                res += str(k) + string[i]
    return res
