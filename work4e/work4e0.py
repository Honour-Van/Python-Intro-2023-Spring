n = int(input())
money_list = [100, 50, 20, 10, 5, 1]

for i in money_list:
    m = n // i
    print(m)
    n = n % i
