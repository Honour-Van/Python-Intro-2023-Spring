
n = int(input())
def getBMI(height,weight):
    bmi=weight/((height/100)**2)
    if bmi<18.5:
        result="Underweight"
    elif 18.5<=bmi<24:
        result="Normal"
    elif 24<=bmi<28:
        result="Overweight"
    else:
        result="Obesity"
    return result
for i in range(n):
    height,weight = map(float, input().split())
    result = getBMI(height,weight)
    print(result)