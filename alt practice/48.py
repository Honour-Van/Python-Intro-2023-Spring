number0 = {"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"10":8,"J":9,"Q":10,"K":11,"A":12,"2":13}
color = {"h":4,"s":3,"d":2,"c":1}
card = []
while True:
    a = input()
    if a == "":
        break
    a = a.split() #a是输入的一个列表
    card = []
    for item in a: #对于每一张牌来说
        color1 = item[0]
        number1 = item[1::]
        card.append((color1,color[color1],number1,number0[number1]))
    card.sort(key = lambda x:(-x[-1],-x[1]))
    print(" ".join(x[0]+x[2] for x in card))