t = input()
res = ""
count = 0
for i in t:
    
    x = 9-int(i)
    if count == 0 and x == 0 :
        res += str(i)
        count+=1
        print(res)
        continue
    if x < int(i):
        res += str(x)
    else:
        res += str(i)
    count+=1
print(int(res))