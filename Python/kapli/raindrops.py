def convert(number):
    out = ''
    sep = False
    if number % 3 == 0:
        out += 'Pling'
        sep = True
    if number % 5 == 0:
        out += 'Plang'
        sep = True
    if number % 7 == 0:
        out += 'Plong'
        sep = True
    if not sep:
        out += str(number)
    return out
