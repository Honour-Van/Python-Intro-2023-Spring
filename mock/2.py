a = int(input())
b = int(input())
if a >= 0 and b >= 0:
    print(f'{a} + {b} = {a + b}')
elif a < 0 and b < 0:
    print(f'({a}) - ({b}) = {a - b}')
else:
    print(f'({a}) * ({b}) = {a * b}')