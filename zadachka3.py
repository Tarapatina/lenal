a = int(input())
b = int(input())
s = 0
c = 0
for i in range (a,b+1):
    if i%3==0:
        s=s+i
        c=c+1
    i+=1
print(s/c)
