# Assignment 2
# Name : Justine Ayroor UCID: ja573
# Program will take 2 arguments as input on the terminal 
# For Eg:
# python Grad_decent.py ionosphere.data ionosphere.trainlabels.0
# 1st Arg: Dataset, 2nd Arg: missing labels file

import sys,math,random

# Define Functions
def initialize_W(wt):
    wt.append(0.02 * random.random() - 0.0001)
    return wt

def dot_prod_logic(v1,v2):
    result = 0
    for i in range(len(v1)):
        temp = v1[i]*v2[i]
        result += temp
    return result

def compute_Delf(r,c,labels,wt,data):
    delf = [0]*c
    for i in range(0, r, 1):
        dp = dot_prod_logic(wt, data[i])
        if(labels.get(i) != None):
            for j in range(0, c, 1):
                # delf[j] += ((labels[i] - dp) * data[i][j])
                delf[j] += 2*((labels[i] - dp)* data[i][j])
    return delf

def Update_W(wt,c,n,grad):
    for j in range(0,c,1):
        wt[j] += n*grad[j] 
        print(w[j])
    return wt

def Compute_Error(r,label,wt,data):
    error = 0 
    for i in range(0, r, 1):
        if(labeldict.get(i) != None):
            error += (label[i] - dot_prod_logic(wt, data[i]))**2
    return error

def normalize_W(wt,c):
    normw = 0
    for j in range(0, c-1, 1):
        normw += wt[j]**2
    normw = math.sqrt(normw)
    return normw

def dist_origin(wt, normw):
    d_org = wt[len(wt)-1]/normw
    d_org = abs(d_org)
    return d_org

def prediction(r,label,wt,data):
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
    if(labeldict[int(newlabels[1])] == 0):
        labeldict[int(newlabels[1])] = -1
    l = f.readline()
f.close()

# Initialize W
w = []
for j in range(0, cols, 1):
    w = initialize_W(w)
print("Initialized W:",w)

# Gradient Decent Iteration
# eta = 0.001 # Uncomment for Assignment 2 Example
eta = 0.0001 # Use for Ionosphere dataset
currentErr = 0 
previousErr = 0
for k in range(0, 100000, 1): # Reduce No. of iterations for Assignment 2 Example
    delF = [0]*cols
    previousErr = currentErr
    delF = compute_Delf(rows,cols,labeldict,w,data)

    # Update W
    w = Update_W(w,cols,eta,delF)

    # Error Computation
    Err = Compute_Error(rows,labeldict,w,data)
    currentErr = Err
    if(currentErr > previousErr):
        Stp_rate = currentErr - previousErr
    else:
        Stp_rate = previousErr - currentErr
    if(Stp_rate == 0): # Uncomment for 0 convergence
        break
    # Stop condition = 0.001
    # if(Stp_rate < 0.001):
    #     break
    print("Objective Difference: ", Stp_rate, "Iteration: ", k)
# print("New W:", w)

# Compute Noramalized W 
normw = normalize_W(w,cols)
print("||W||: ", normw)

# Compute Distance from the origin 
d_origin = dist_origin(w,normw)
print("Distance from Origin: ", d_origin)

# Prediction
prediction(rows,labeldict,w,data)