from math import sqrt


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


args = {'c': 12, 'b': 8, 'a': 7}

print(triangle_area(**args))
