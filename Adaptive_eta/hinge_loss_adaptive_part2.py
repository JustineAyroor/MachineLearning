# Assignment 5
# Name : Justine Ayroor UCID: ja573
# Program will take 2 arguments as input on the terminal 
# For Eg:
# python Hinge_loss.py ionosphere.data ionosphere.trainlabels.0 ionosphere.labels
# 1st Arg: Dataset, 2nd Arg: Missing labels file

import sys,math,random

def dot_prod_logic(v1, v2):
    result = 0
    for i in range(len(v1)):
        temp = v1[i]*v2[i]
        result += temp
    return result

def Initialize_W(c):
    w = []
    for j in range(0, cols, 1):
        w.append(0.02 * random.random() - 0.01)
    return w

def normalize_W(wt, c):
    normw = 0
    for j in range(0, c-1, 1):
        normw += wt[j]**2
    normw = math.sqrt(normw)
    return normw

def Update_W(wt, c, n, grad):
    for j in range(0, c, 1):
        wt[j] -= n*grad[j]
    return wt

def Re_Update_W(wt,c,n,grad):
    for j in range(0,c,1):
        wt[j] += n*grad[j] 
    return wt


def dist_origin(wt, normw):
    d_org = wt[len(wt)-1]/normw
    d_org = abs(d_org)
    return d_org

def compute_Delf(r, c, labels, wt, data):
    delf = [0]*c
    for i in range(0, r, 1):
        for j in range(0, c, 1):
            if(labels.get(i) != None):
                tempdell = labels[i]*dot_prod_logic(wt,data[i])
                if(tempdell<1):
                    delf[j] += (-labels[i]*data[i][j])
                elif(tempdell>=1):
                    delf[j] += 0
    return delf

def Compute_Error(r, label, wt, data):
    error = 0 
    for i in range(0, r, 1):
        if(label.get(i) != None):
            errlist = [0,(1 - (label[i]*dot_prod_logic(wt, data[i])))] 
            error += max(errlist)  
    return error

def prediction(r, label, wt, data):
    for i in range(0, rows, 1):
        if(label.get(i) == None):
            labels_missing.append(i)
            dp = dot_prod_logic(wt, data[i])
            if(dp > 0):
                label[i] = 1
                print(i,"1")
            else:
                label[i] = 0
                print(i,"0")

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

# Initialize W
w = Initialize_W(cols)

# Gradient Decent
k = 0
# lamda = 0.01 # Can keep changing the value to get optimized results
eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001, .000000000001, .0000000000001, .00000000000001, .000000000000001, .0000000000000001, .00000000000000001 ]
# eta = 0.000000001
labels_missing = []
currentErr = 0 
previousErr = 0
isConverged = False
while(isConverged != True):
    previousErr = currentErr
    # Normalize W
    # normw = normalize_W(w, cols)
    errobj = []
    for a in range(0, len(eta_list), 1):
        eta = eta_list[a]
        # Compute Dell fuction/Gradient Function
        Delf = compute_Delf(rows, cols, labeldict, w, data)
        # Update W
        w = Update_W(w, cols, eta, Delf)
        # Compute Objective/Error
        Error = Compute_Error(rows, labeldict, w, data)
        errobj.append(Error)
        # Re Update w
        w = Re_Update_W(w, cols, eta, Delf)
    
    currentErr = min(errobj)
    bestEtaIndex = errobj.index(currentErr)
    eta = eta_list[bestEtaIndex]
    w = Update_W(w, cols, eta, Delf)
    # currentErr = Error + (normw**2)*lamda # To work with regularizer
    print("Objective Difference: ", abs(currentErr-previousErr), " Iteration No. ", k)
    if(abs(currentErr-previousErr)<0.001):
        isConverged = True
    # if(abs(currentErr-previousErr)==0):
    #     isConverged = True
    k+=1

# print(w) # Uncomment to chech W when working with practice Dataset 
# print("Distance from Origin: ",dist_origin(w, normw))
# Prediction
prediction(rows, labeldict, w,data)

# # Accuracy Check & Balanced Error Rate
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

# error = 0
# a = 0
# b = 0
# c = 0
# d = 0
# for i in labels_missing:
#     if(truelabels[i] != labeldict[i]):
#         error += 1
#     if(truelabels[i] == 0 and labeldict[i] == 0):
#         a += 1
#     elif(truelabels[i] == 0 and labeldict[i] == 1):
#         b += 1
#     elif(truelabels[i] == 1 and labeldict[i] == 0):
#         c += 1
#     elif(truelabels[i] == 1 and labeldict[i] == 1):
#         d += 1
# # print('Accuracy Check :', (100 - error/len(labels_missing)*100))
# ber = 0.5*(b/(a+b)) + (c/(c+d))
# print(ber)