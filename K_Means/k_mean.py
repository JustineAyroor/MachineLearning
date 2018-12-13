import math,sys,random
list = [1,2,3,4,5]
k = 3
m = [0,0,0]
c = []
for i in range(0,k,1):
    m[i] = list[random.randint(0, len(list)-1)]
    c.append([])
print(m)

d = [0]*3
# print(d)
for i in range(0,len(list),1):
    for j in range(0, k, 1):
        d[j] = (list[i] - m[j])**2
    if(d[0]<d[1] and d[0]< d[2]):
        c[0].append(list[i])
    elif(d[1]<d[0] and d[1]< d[2]):
        c[1].append(list[i])
    else:
        c[2].append(list[i])
print(c)
mc = [0,0,0]
# h = 0
for h in range(0,k,1):
    for e in range(0,len(c[h]),1):
        mc[h] += c[h][e]
    mc[h] = mc[h]/len(c[h])
# h +=1
print(mc)