idnumber = input()  # 输入身份证号码
factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check = ["1","0","X","9","8","7","6","5","4","3","2"]
n = 0  # 求和
i = 0
h = 0
if len(idnumber) != 18:
    print("illegal")
elif not idnumber[:-1].isdigit():
    print("illegal")
else:
    while i < 17:
        n = n + int(idnumber[i])*factor[i]
        i = i + 1
    result = check[n % 11]
    if (idnumber[-1] == result) or (result == "X" and idnumber[-1] == "x"):
        if int(idnumber[-2]) % 2 == 0:
            print("female")
        else:
            print("male")
    else:
        print("illegal")
