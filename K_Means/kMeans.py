import sys,math,random

# Input Data 
datafile = sys.argv[1]
f = open(datafile, "r")
data = []
l = f.readline()
while(l != ''):
    a = l.split()
    dataline = []
    for i in range(0, len(a), 1):
        dataline.append(float(a[i]))
    data.append(dataline)
    l = f.readline()
rows = len(data)
cols = len(data[0])
f.close()
# print(data)

cluster = int(sys.argv[2])
# print(cluster)
# c = []
m = [0]*cluster
for i in range(0,cluster,1):
    m[i] = data[random.randint(0, len(data)-1)]
    # c.append([])
# print(m)
# print(c)
# while()
prevObjective = []
currObjective = []
isConverged = False
while(isConverged != True):
    n = [0]*cluster
    c = []
    for ch in range(0,cluster,1):
        c.append([])
    for i in range(0, rows, 1):
        d = [0]*cluster
        for j in range(0, cols, 1):
            d[0] = d[0] + (data[i][j] - m[0][j])**2
            d[1] = d[1] + (data[i][j] - m[1][j])**2
        if(d[0]<d[1]):
            c[0].append(data[i])
            n[0] += 1
        else:
            c[1].append(data[i])
            n[1] += 1
    # print(len(c[0]),len(c[1]))
    # print(n[0],n[1])
    # print(c[0])
    # print(c[1])
    # h = 0
    prevObjective = m
    m = []
    for mean in range(0,cluster,1):
        m.append([0]*cols)
    for i in range(0,len(c[0]),1):
        for j in range(0, cols, 1):
            m[0][j] += c[0][i][j]
    for i in range(0,len(c[1]),1):
        for j in range(0, cols, 1):
            m[1][j] += c[1][i][j]
    for i in range(0,cluster,1):
        for j in range(0,cols,1):
            m[i][j] /= n[i]
    # print(m)
    currObjective = m
    print(len(c[0]),len(c[1]))
    # print(prevObjective)
    # print(currObjective)
    if(prevObjective == currObjective):
        isConverged = True
        break
    # print(len(c[0]),len(c[1]))


