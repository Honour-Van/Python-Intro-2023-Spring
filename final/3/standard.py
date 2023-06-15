def standard_func():
    a = input().split()
    ans = 0
    for i in a:
        if i[0] == 'A':
            ans += 0.5
        elif i[0] == 'B':
            ans += 1
    print(f'{ans:.1f}')

if __name__ == '__main__':
    standard_func()