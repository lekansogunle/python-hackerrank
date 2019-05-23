import numpy

n,m = map(int, input().split(" "));
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split(" "))))

mins = numpy.min(matrix, axis = 1)

print(mins.max())

