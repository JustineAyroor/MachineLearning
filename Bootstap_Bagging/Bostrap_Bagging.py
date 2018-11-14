# Justine Ayroor
# UCID: ja573
# Assignment 7
# Use  trainLabels and Labels File while execution 
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

# Input labels File
labelsFile = sys.argv[2]
f = open(labelsFile, "r")
labeldict = {}
l = f.readline()
while(l != ''):
    newlabels = l.split()
    labeldict[int(newlabels[1])] = int(newlabels[0])
    if(labeldict[int(newlabels[1])] == 0):
        labeldict[int(newlabels[1])] = -1
    l = f.readline()
f.close()

testData = []
TrainData = []
TrainDatalabels = []
missingLabels = []
for i in range(0, rows, 1):
    if(labeldict.get(i) == None):
        testData.append(data[i])    
        missingLabels.append(i)
    else:
        TrainData.append(data[i])
        TrainDatalabels.append(labeldict[i])

numofVotes = []
for i in range(0,len(testData),1):
    numofVotes.append([0,0])

for iterate in range(0, 100, 1):
    Bag = []
    BagLabel = []
    for i in range(0, 350, 1):
        randval = random.randint(0,len(TrainData)-1)
        Bag.append(TrainData[randval])
        BagLabel.append(TrainDatalabels[randval])

    giniVal = []
    splitIndex = []

    for k in range(0,cols,1):
        colVal = []
        giniStumps = []
        labels = []

        for i in range(0,len(Bag),1):
            colVal.append(Bag[i][k])
            labels.append(BagLabel[i])
            
        colVal, labels = zip(*sorted(zip(colVal,labels)))
        
        for stump in range(1,len(colVal),1):
            lsize = stump
            rsize = len(colVal) - stump
            lp=0
            rp=0
            for i in range(0,stump,1):
                if(labels[i] == -1):
                    lp+=1

            for i in range(stump,len(colVal),1):
                if(labels[i] == -1):
                    rp+=1

            gini = (lsize/len(colVal))*(lp/lsize)*(1 - lp/lsize) + (rsize/len(colVal))*(rp/rsize)*(1 - rp/rsize)
            giniStumps.append(gini)
            # print(lp,rp,rsize,lsize,gini, stump)
        splitIndex.append(giniStumps.index(min(giniStumps)))
        giniVal.append(min(giniStumps))
    comprow = splitIndex[giniVal.index(min(giniVal))]
    compcol = giniVal.index(min(giniVal))


    for i in range(0,len(testData),1):
        if(testData[i][compcol] < TrainData[comprow][compcol]):
            numofVotes[i][0] += 1
        else:
            numofVotes[i][1] += 1

for i in range(0, len(testData),1):
    if(numofVotes[i][0]<numofVotes[i][1]):
        print(missingLabels[i]," - 0")
        labeldict[missingLabels[i]] = 0
    else:
        print(missingLabels[i]," - 1")
        labeldict[missingLabels[i]] = 1

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
a = 0
b = 0
c = 0
d = 0
for i in missingLabels:
    if(truelabels[i] != labeldict[i]):
        error += 1
    if(truelabels[i] == 0 and labeldict[i] == 0):
        a += 1
    elif(truelabels[i] == 0 and labeldict[i] == 1):
        b += 1
    elif(truelabels[i] == 1 and labeldict[i] == 0):
        c += 1
    elif(truelabels[i] == 1 and labeldict[i] == 1):
        d += 1
print('Accuracy Check :', (100 - error/len(missingLabels)*100))
ber = 0.5*(b/(a+b)) + (c/(c+d))
print("BER: ",ber)