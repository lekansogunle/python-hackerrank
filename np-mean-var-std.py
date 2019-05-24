import numpy

n,m = map(int, input().split(" "));
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split(" "))))

mat = numpy.array(matrix)

print(numpy.mean(mat, axis = 1) )
print(numpy.var(mat, axis = 0) )
print(round(numpy.std(mat, axis = None), 11) )
