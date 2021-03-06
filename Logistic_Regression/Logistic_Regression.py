# Assignment 4
# Name : Justine Ayroor UCID: ja573
# Program will take 2 arguments as input on the terminal 
# For Eg:
# python Logistic_Regression.py climate.data climate.trainlabels.0
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
    # print("Initialized W:",w)
    return w

def normalize_W(wt, c):
    normw = 0
    for j in range(0, c-1, 1):
        normw += wt[j]**2
    normw = math.sqrt(normw)
    # print("||W||:", normw)
    return normw

def Update_W(wt, c, n, grad):
    for j in range(0, c, 1):
        wt[j] += n*grad[j]
    return wt

def dist_origin(wt, normw):
    d_org = wt[len(wt)-1]/normw
    d_org = abs(d_org)
    return d_org

def compute_Delf(r, c, labels, wt, data):
    delf = [0]*c
    for i in range(0, r, 1):
        dp = dot_prod_logic(wt,data[i])
        for j in range(0, c, 1):
            if(labels.get(i) != None):
                delf[j] += ((labels[i] - (1/(1+(math.exp(-dp)))))*data[i][j])                
    return delf

def Compute_Error(r, label, wt, data):
    error = 0 
    for i in range(0, r, 1):
        if(label.get(i) != None):
            dp = dot_prod_logic(wt,data[i])
            error += ((-label[i]*(math.log(1/(1+math.exp(-dp))))) - ((1-label[i])*(math.log((math.exp(-dp))/(1+math.exp(-dp))))))
    return error

def prediction(r, label, wt, data):
    for i in range(0, rows, 1):
        if(label.get(i) == None):
            dp = dot_prod_logic(wt, data[i])
            if(dp > 0):
                print("Label No.:", i, "Prediction: 1")
            else:
                print("Label No.:", i, "Prediction: 0")

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

# Initialize W
w = Initialize_W(cols)

# Gradient Decent
k = 0
eta = 0.001
# eta = 0.01 # Uncomment for Practice Dataset
currentErr = 0 
previousErr = 0
isConverged = False
while(isConverged != True):
    previousErr = currentErr
    # Normalize W
    normw = normalize_W(w, cols)
    # Compute Dell fuction/Gradient Function
    Delf = compute_Delf(rows, cols, labeldict, w, data)
    # Update W
    w = Update_W(w, cols, eta, Delf)
    # Compute Objective/Error
    Error = Compute_Error(rows, labeldict, w, data)
    currentErr = Error
    print("Objective Difference: ", abs(currentErr-previousErr), " Iteration No. ", k)
    # if(abs(currentErr-previousErr)<0.0000001):  # Use for Practice Dataset provided for Assignment 3
    if(abs(currentErr-previousErr)<0.001):
        isConverged = True
    k+=1

# print(w) # Uncomment to chech W when working with practice Dataset 
print("Distance from Origin: ",dist_origin(w, normw))

# Prediction
prediction(rows, labeldict, w,data)