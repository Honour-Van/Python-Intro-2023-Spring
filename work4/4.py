id_num=input()
n=list(map(int,id_num))
s=0
for i in range(0,15,2):
    t=n[i]*2
    s+=(t//10)+(t%10)
for j in range(1,15,2):
    s+=n[j]
if (10-s%10)%10==n[-1]:
    print("yes")
else:
    print("no")