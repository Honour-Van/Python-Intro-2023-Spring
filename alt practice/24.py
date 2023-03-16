# credit: 王佳慧
s = input()
a,b,c = s.split()
if len(b) == 1 and b in '+-*/':
    if b == '/' and c =='0':
        print("Divided by zero!")
    else:
      if b == '+':
         d = int(a)+int(c)
         print(d)
      elif b == '-':
           d = int(a)-int(c)
           print(d)
      elif b == '*':
           d = int(a)*int(c)
           print(d)
      elif b == "/":
          d = int(a)/int(c)
          print("{:.2f}".format(d))
else:
   print("Invalid operator!")

# 我的一个使用eval的版本
# s= input()
# a, b, c = s.split()
# if len(b) != 1 or b not in '+-*/':
#     print("Invalid operator!")
# elif b == '/' and c =='0':
#     print("Divided by zero!")
# else:
#     ans = eval(s)
#     if b == "/":
#         print(f"{ans:.2f}")
#     else:
#         print(f"{ans:.0f}")

