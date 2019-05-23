import numpy

def arrays(arr):
    arr.reverse()
    # complete this function
    return numpy.array(arr, float)

arr = input().strip().split(' ')
