n=int(input())
l = []
x=0
for i in range(n):
    temp = input()
    if temp == "++X" or temp == "X++":
        x+=1
    else:
        x-=1

print(x)
