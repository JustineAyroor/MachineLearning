# Justine Ayroor
# UCID: ja573
# Assignment 6
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
    # dataline.append(1)
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

giniVal = []
splitIndex = []
# print(len(giniVal))
# print(len(colVal))

for k in range(0,cols,1):
    colVal = []
    giniStumps = []
    labels = []

    for i in range(0,rows,1):
        if(labeldict.get(i) != None):
            colVal.append(data[i][k])
            labels.append(labeldict[i])
        
    colVal, labels = zip(*sorted(zip(colVal,labels)))
    
    for stump in range(1,len(colVal),1):
        lsize = stump
        rsize = rows - stump
        lp=0
        rp=0
        for i in range(0,stump,1):
            if(labels[i] == -1):
                lp+=1

        for i in range(stump,len(colVal),1):
            if(labels[i] == -1):
                rp+=1

        gini = (lsize/rows)*(lp/lsize)*(1 - lp/lsize) + (rsize/rows)*(rp/rsize)*(1 - rp/rsize)
        giniStumps.append(gini)
        # print(lp,rp,rsize,lsize,gini, stump)
    splitIndex.append(giniStumps.index(min(giniStumps)))
    giniVal.append(min(giniStumps))

print("Split-Index:",splitIndex[giniVal.index(min(giniVal))])
print("Collumn With Min GiniValue: ",giniVal.index(min(giniVal)))
print("Gini Value: ",min(giniVal))
