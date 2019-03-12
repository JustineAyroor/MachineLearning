# Justine Ayroor (ja573)
# Dominic Devasahayam(dd429)
# Assignment 9
# Please make sure you have all labels file in the same directory while execution of the program only if you want to check the error % in the predictions
# command : python NeauralNet breast_cancer.data breast_cancer.trainlabels.0
import sys,math,random

def Initialize_W(c):
    w = []
    for j in range(0, cols, 1):
        w.append(random.uniform(-1,1))
    return w

def dot_prod_logic(v1, v2):
    result = 0
    for i in range(len(v1)):
        temp = v1[i]*v2[i]
        result += temp
    return result

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
    if(labeldict[int(newlabels[1])] == 0):
        labeldict[int(newlabels[1])] = -1
    l = f.readline()
f.close()

missingLabels = []
for i in range(0, rows, 1):
    if(labeldict.get(i) == None):  
        missingLabels.append(i)

trainlabels = []
for i in labeldict:
    trainlabels.append(labeldict[i])

z = []
zdash = []
for i in range(0,len(labeldict),1):
    z.append([])
# print(z)

for i in range(0, (rows - len(labeldict)),1):
    zdash.append([])

for k in range(0,1000,1):
    w = []
    w = Initialize_W(cols)
    # print(w)
    dot_train= []
    dot_test =[]
    for i in range(0,rows,1):
        if(labeldict.get(i) == None):    
            dot_test.append(dot_prod_logic(data[i],w))
        else: 
            dot_train.append(dot_prod_logic(data[i],w))
    smallwdot_train = min(dot_train)
    largewtdot_train = max(dot_train)
    smallwdot_test = min(dot_test)
    largewtdot_test = max(dot_test)
    w0_train = random.uniform(smallwdot_train,largewtdot_train)
    w0_test = random.uniform(smallwdot_test,largewtdot_test)

    for i in range(0,len(labeldict),1):
        signzi = dot_train[i]+w0_train
        if(signzi < 0):
            z[i].append(-1)
        else:
            z[i].append(1)

    for i in range(0,len(dot_test),1):
        signzidash = dot_test[i]+w0_test
        if(signzidash<0):
            zdash[i].append(0)
        else:
            zdash[i].append(1)
    
from sklearn.svm import LinearSVC
classifier  = LinearSVC(max_iter=10000,C = 1)
classifier.fit(z,trainlabels)

# Prediction
Y_pred = classifier.predict(zdash)

count = 0
for i in missingLabels:
    if(Y_pred[count] == -1):
        Y_pred[count] = 0
    print(i ," - ",Y_pred[count])
    count += 1

# # Cross-Validation
# truelabelsdict = {"breast_cancer.data":"breast_cancer.labels","climate.data":"climate.labels","qsar.data":"qsar.labels","hill_valley.data":"hill_valley.labels","ionosphere.data":"ionosphere.labels","micromass.data":"micromass.labels"}
# trainlabelfile = truelabelsdict[datafile]
# f = open(trainlabelfile, "r")
# truelabels = {}
# l = f.readline()
# while(l != ''):
#     a = l.split()
#     truelabels[int(a[1])] = int(a[0])
#     l = f.readline()
# f.close()

# b = 0
# c = 0

# count = 0
# for i in missingLabels:
#     if(truelabels[i] == -1 and Y_pred[count] == 1):
#         b += 1
#     elif(truelabels[i] == 1 and Y_pred[count] == -1):
#         c += 1
#     count+=1
# ber = (b+c)/len(missingLabels)*100
# print("Error %: ",ber)
