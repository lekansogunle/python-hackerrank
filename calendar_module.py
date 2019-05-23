# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

date_value = list(map(int, input().split()))
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(days[calendar.weekday(date_value[2], date_value[0], date_value[1])])
