import sys,math

# Read Data from file 
datafile = sys.argv[1]
f = open(datafile, 'r')
data = []
i = 0
l = f.readline()
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    #print(len(l2))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])

# Read labels from File

trainlabelfile = sys.argv[2]
f = open(trainlabelfile, 'r')
trainlabels = {}
l = f.readline()
while(l != ''):
    a = l.split()
    #print(a)
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()

#for i in range(0, rows, 1):
#    print(trainlabels)

# Determine the mean of each class

m0 = []
m1 = []

for i in range(0, cols, 1):
    m0.append(0)
    m1.append(0)

n0 = 0
n1 = 0

for i in range(0, rows, 1):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        n0 += 1
        for j in range(0, cols, 1):
            m0[j] += data[i][j]
    if(trainlabels.get(i) != None and trainlabels[i] == 1):
        n1 += 1
        for j in range(0, cols, 1):
            m1[j] += data[i][j]

for j in range(0, cols, 1):
    m0[j] /= n0
    m1[j] /= n1

# Classify Unlabelled points
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        d0 = 0
        d1 = 0
        for j in range(0, cols, 1):
            d0 = d0 + (m0[j] - data[i][j])**2
            d1 = d1 + (m1[j] - data[i][j])**2
        d0 = math.sqrt(d0)
        d1 = math.sqrt(d1)
        if(d0<d1):
            #print("0", i)
            trainlabels[i] = 0
        else:
            #print("1", i)
            trainlabels[i] = 1

#print('Datsa set:')
#for i in range(0, rows, 1):
#    #print('Each row:\n', i, data[i])
#    print('5th Cols: \n', data[i][4])
#print('Number of element with Class 0:', n0)
#print(len(m0))
#print('Mean of each input with Class 0:\n', m0)
#print('Number of element with Class 1:', n1)
#print(len(m1))
#print('Mean of each input with Class 1:\n', m1)
#print(len(m0))
#print(len(m1))
#print(trainlabels)

# Classify all data points and display
for j in range(0, rows, 1):
    test_data = data[j]
    x0 = 0
    x1 = 0
    for i in range(0,len(m0), 1):
        x0 += (int(m0[i]-test_data[i]))**2
    for i in range(0,len(m1), 1):
        x1 += (int(m1[i]-test_data[i]))**2
    
    EUdistx0 = math.sqrt(x0)
    EUdistx1 = math.sqrt(x1)
    
    print('Distance with m0:', EUdistx0)
    print('Distance with m1:', EUdistx1)
    
    if(EUdistx0 < EUdistx1):
        print('Class: 0', j)
    else:
        print('Class: 1', j)