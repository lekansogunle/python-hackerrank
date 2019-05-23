import numpy

n,m = map(int, input().split(" "));
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split(" "))))

matrix = numpy.array(matrix);

print(numpy.transpose(matrix))
print(matrix.flatten())
