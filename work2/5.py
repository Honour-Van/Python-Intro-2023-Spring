x=int(input())
GPA=4-3*(100-x)**2/1600
if GPA>=1.00:
    print(f"{GPA:.2f}")
else:
    print("0.00")