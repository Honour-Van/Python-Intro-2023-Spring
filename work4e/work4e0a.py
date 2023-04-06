n = int(input())
money_list = [100, 50, 20, 10, 5, 1]

for i in money_list:
    print(n // i)
    n %= i
