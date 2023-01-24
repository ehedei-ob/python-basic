from functools import reduce


def sumaImpares(list=[]):
    return reduce(lambda total, el: total + el, filter(lambda el: el % 2, list))


print(sumaImpares(range(1, 6)))
