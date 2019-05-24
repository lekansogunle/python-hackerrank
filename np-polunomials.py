import numpy

polyn = list(map(float, input().split(' ')))
value = float(input())

print(numpy.polyval(polyn, value))
