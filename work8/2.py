dictionary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert(num, base):
    if num < base:
        return dictionary[num]
    else:
        return convert(num // base, base) + dictionary[num % base]

base = int(input())
num = int(input())
print(convert(num, base))