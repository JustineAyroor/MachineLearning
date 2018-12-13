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
cluster = int(sys.argv[2])
m = [0]*cluster
for i in range(0,cluster,1):
    m[i] = data[random.randint(0, len(data)-1)]
prevObjective = []
currObjective = []
isConverged = False
while(isConverged != True):
    predval = []
    n = [0]*cluster
    c = []
    for ch in range(0,cluster,1):
        c.append([])
    
    for i in range(0, rows, 1):
        d = [0]*cluster
        for clus in range(0,cluster,1):
            for j in range(0, cols, 1):
                d[clus] = d[clus] + (data[i][j] - m[clus][j])**2
        minvalindex = d.index(min(d)) 
        c[minvalindex].append(data[i])
        n[minvalindex] += 1
        predval.append(minvalindex)
    prevObjective = m
    m = []
    for mean in range(0,cluster,1):
        m.append([0]*cols)
    for clusters in range(0,cluster,1):
        for i in range(0,len(c[clusters]),1):
            for j in range(0, cols, 1):
                m[clusters][j] += c[clusters][i][j]
    for i in range(0,cluster,1):
        for j in range(0,cols,1):
            m[i][j] /= n[i]
    currObjective = m
    pred = []
    for no in range(0,cluster,1):
        pred.append(len(c[no]))
    print(pred)
    if(prevObjective == currObjective):
        isConverged = True
        break

for i in range(0,rows,1):
    print(i, predval[i])