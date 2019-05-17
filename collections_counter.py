# Enter your code here. Read input from STDIN. Print output to STDOUT

number_of_shoes = int(input());
shoe_sizes_in_shop = list(map(int, input().split(" ")));

number_of_customers = int(input());
customers_requests = []
for i in range(number_of_customers):
    customers_requests.append(list(map(int, input().split(" "))))

# print(number_of_shoes, shoe_sizes_in_shop, number_of_customers, customers_requests)

total = 0
# loop through customer_requests
    # if size(first element) is in shoe_sizes_in_shop add price(second element) total
    # remove size from shoe_sizes_in_shop

for request in customers_requests:
    if request[0] in shoe_sizes_in_shop:
        total += request[1]
        shoe_sizes_in_shop.remove(request[0])

print(total)

#https://www.hackerrank.com/challenges/collections-counter/problem
