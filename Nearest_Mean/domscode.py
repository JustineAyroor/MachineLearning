# The program takes in three arguements
# 1. dataset (the whole dataset)
# 2. trainlabels (this file contains some missing data on which predicition is done)
# 3. lables (this file should contain all labels with class values, as I am using this to compute Accuracy and BER)
import sys,math

# Reading the file with dataset
dataSetFileName = sys.argv[1]
f = open(dataSetFileName, "r")
dataSet = []
l = f.readline()
while (l != ""):
    rowData = []
    data = l.split()
    for i in range(0,len(data),1):
        rowData.append(float(data[i]))
    dataSet.append(rowData)
    l = f.readline()
f.close()

row = len(dataSet)
column = len(dataSet[0])

# Reading the train label file
trainLabelFile = sys.argv[2]
f = open(trainLabelFile,"r")
n =[]
n.append(0)
n.append(0)
trainLabels = {}
l = f.readline()
while(l!=""):
    a = l.split()
    trainLabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])]+=1
f.close()

# Calculating the mean for each class
m0 = []
m1 = []

for i in range(0, column, 1):
    m0.append(1)
    m1.append(1)


for i in range(0, row,1):
    for j in range(0, column, 1):
        if(trainLabels.get(i) != None and trainLabels[i] == 0):
            m0[j]+=dataSet[i][j]
        if(trainLabels.get(i) != None and trainLabels[i] == 1):
            m1[j]+=dataSet[i][j]


for i in range(0, column,1):
    m0[i]/=n[0]
    m1[i]/=n[1]

# Calculating Standard Deviation for each class
stdDeviation0 = []
stdDeviation1 = []

for i in range(0,column,1):
    stdDeviation0.append(0)
    stdDeviation1.append(0)

for i in range(0,row,1):
    for j in range(0, column,1):
        if(trainLabels.get(i)!= None and trainLabels[i]==0):
            stdDeviation0[j]+=(dataSet[i][j] - m0[j])**2
        
        if(trainLabels.get(i)!= None and trainLabels[i]==1):
            stdDeviation1[j]+=(dataSet[i][j] - m1[j])**2
        
for i in range(0, column,1):
    stdDeviation0[i]/=n[0]
    stdDeviation0[i] = math.sqrt(stdDeviation0[i])
    stdDeviation1[i]/=n[1]
    stdDeviation1[i] = math.sqrt(stdDeviation1[i])
    
# Prediction the missing labels:
missingLabels = []
print("Predicted Values: ")
for i in range(0, row,1):
    if(trainLabels.get(i) == None):
        d0 = 0
        d1 = 0    
        missingLabels.append(i)
        for j in range(0, column,1):
            d0 += ((dataSet[i][j] - m0[j])/stdDeviation0[j])**2
            d1 += ((dataSet[i][j] - m1[j])/stdDeviation1[j])**2
        
        if(d0 < d1):
            print(0,i)
            trainLabels[i] = 0
        else:
            print(1,i)
            trainLabels[i] = 1

# Calculating Accuracy and Balanced Error Rate
actualLabelFile = sys.argv[3]
f = open(actualLabelFile,"r")
actualLabels = {}

l = f.readline()
while(l!=""):
    a = l.split()
    actualLabels[int(a[1])] = int(a[0])
    l = f.readline()

error = 0
a = 0
b = 0
c = 0
d = 0
for i in missingLabels:
    if(trainLabels[i] != actualLabels[i]):
        error+=1
    if(actualLabels[i]==0 and trainLabels[i]==0):
        a+=1
    elif(actualLabels[i]==0 and trainLabels[i]==1):
        b+=1
    elif(actualLabels[i]==1 and trainLabels[i] ==0):
        c+=1
    elif(actualLabels[i]==1 and trainLabels[i]==1):
        d+=1 
error = (error/len(missingLabels))*100
balancedErrorRate = 0.5*((b/(a+b)) + (c/(c+d)))
print("Accuracy:",100-error,"%")
print ("Balanced Error Rate:",balancedErrorRate)