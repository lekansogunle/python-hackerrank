def average(array):
    # your code goes here
    distinct_list = list(set(array))
    return (sum(distinct_list)/len(distinct_list))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
