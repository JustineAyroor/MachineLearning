# Program will take 3 arguments 
import sys,math

# Input Data Set
BC_file = sys.argv[1]
f = open(BC_file, "r")
data = []
l = f.readline()
while(l != ''):
    a = l.split()
    l2 = []
    for i in range(0, len(a), 1):
        l2.append(float(a[i]))
    data.append(l2)
    l = f.readline()
rows = len(data)
cols = len(data[0])

print('Number of Rows in Dataset',rows)
print('Number of Collumns in Dataset',cols)
f.close()

# Input trainlabels
labelfile = sys.argv[2]
f = open(labelfile, "r")
labels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()
while(l != ''):
    a = l.split()
    # Find Class of each data using the labels
    labels[int(a[1])] = int(a[0])
    # Segregating the classes to find out the number of elements in each class
    n[int(a[0])] +=1
    l = f.readline()
# Print Number of elements in each class
print('Number of elements in Class 0:',n[0])
print('Number of elements in Class 1:',n[1])
f.close()

# Initializing the mean of all vectors to 1
m0 = []
for j in range(0, cols, 1):
    m0.append(1)

m1 = []
for j in range(0, cols, 1):
    m1.append(1)

# Computing mean of each class
for i in range(0, rows, 1):
    if(labels.get(i) != None and labels[i] == 0):
        for j in range(0, cols, 1):
            m0[j] += data[i][j]
    if(labels.get(i) != None and labels[i] == 1):
        for j in range(0, cols, 1):
            m1[j] += data[i][j]

for j in range(0, cols, 1):
    m0[j] /= n[0]
    m1[j] /= n[1]

# Find S.d of Each variable
sd0 = []
for j in range(0, cols, 1):
    sd0.append(0)

sd1 = []
for j in range(0, cols, 1):
    sd1.append(0)

for i in range(0, rows, 1):
    if(labels.get(i) != None and labels[i] == 0):
        for j in range(0, cols, 1):
            sd0[j] += (data[i][j] - m0[j])**2
    if(labels.get(i) != None and labels[i] == 1):
        for j in range(0, cols, 1):
            sd1[j] += (data[i][j] - m1[j])**2

for j in range(0, cols, 1):
    sd0[j] /= n[0]
    sd1[j] /= n[1]
    sd0[j] = math.sqrt(sd0[j])
    sd1[j] = math.sqrt(sd1[j])

# Prediction
labels_missing = []
for i in range(0, rows, 1):
    if(labels.get(i) == None):
        d0 = 0
        d1 = 0
        labels_missing.append(i)
        for j in range(0, cols, 1):
            d0 = d0 + ((m0[j] - data[i][j])/sd0[j])**2
            d1 = d1 + ((m1[j] - data[i][j])/sd1[j])**2
        if(d0<d1):
            #print("0", i)
            labels[i] = 0
        else:
            #print("1", i)
            labels[i] = 1

# Accuracy Check & Balanced Error Rate
trainlabelfile = sys.argv[3]
f = open(trainlabelfile, "r")
truelabels = {}
l = f.readline()
while(l != ''):
    a = l.split()
    truelabels[int(a[1])] = int(a[0])
    l = f.readline()
f.close()

error = 0
errorIndex = []
a = 0
b = 0
c = 0
d = 0
for i in labels_missing:
    if(truelabels[i] != labels[i]):
        error += 1
        errorIndex.append(i)
    if(truelabels[i] == 0 and labels[i] == 0):
        a += 1
    elif(truelabels[i] == 0 and labels[i] == 1):
        b += 1
    elif(truelabels[i] == 1 and labels[i] == 0):
        c += 1
    elif(truelabels[i] == 1 and labels[i] == 1):
        d += 1
print(error)
print(errorIndex)
print('Accuracy Check :', (100 - error/len(labels_missing)*100))
ber = 0.5*(b/(a+b)) + (c/(c+d))
print("BER: ",ber)

# Average Test Error
mean = 0
sderr = 0
errdata = []
for i in errorIndex:
    errdata.append(labels[i])
print(errdata)
for i in range(0, len(errdata), 1):
    mean += errdata[i]
mean /= len(errdata)
for j in range(0, len(errdata), 1):
     sderr += (errdata[j] - mean)**2
sderr /= len(errdata)
sderr = math.sqrt(sderr)
print('Naive Bayes Error:')
print('Mean: ', mean, 'S.D: ', sderr)