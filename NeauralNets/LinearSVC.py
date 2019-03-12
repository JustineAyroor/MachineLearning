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
    dataline.append(1)
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
    l = f.readline()
f.close()
testdata = []
missingLabels = []
for i in range(0, rows, 1):
    if(labeldict.get(i) == None):  
        missingLabels.append(i)
        testdata.append(data[i])

traindata = []
trainlabels = []
for i in labeldict:
    trainlabels.append(labeldict[i])
    traindata.append(data[i])

from sklearn.svm import LinearSVC
classifier  = LinearSVC(max_iter=10000,C = 1)
classifier.fit(traindata,trainlabels)

# Prediction
Y_pred = classifier.predict(testdata)

print(Y_pred)

# Cross-Validation
truelabelsdict = {"breast_cancer.data":"breast_cancer.labels","climate.data":"climate.labels","qsar.data":"qsar.labels","hill_valley.data":"hill_valley.labels","ionosphere.data":"ionosphere.labels","micromass.data":"micromass.labels"}
trainlabelfile = truelabelsdict[datafile]
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
count = 0
for i in missingLabels:
    if(truelabels[i] != Y_pred[count]):
        error += 1
    if(truelabels[i] == 0 and Y_pred[count] == 1):
        b += 1
    elif(truelabels[i] == 1 and Y_pred[count] == 0):
        c += 1
    count+=1
print('Accuracy Check :', (100 - error/len(missingLabels)*100))
ber = (b+c)/len(missingLabels)*100
print("Error %: ",ber)
