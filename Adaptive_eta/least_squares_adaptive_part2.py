# Assignment 5
# Name : Justine Ayroor UCID: ja573
# Program will take 3 arguments as input on the terminal 
# For Eg:
# python least_squares_adaptive.py ionosphere.data ionosphere.trainlabels.0 ionosphere.labels
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
                delf[j] += ((labels[i] - dp) * data[i][j])
                # delf[j] += 2*((labels[i] - dp)* data[i][j])
    return delf

def Update_W(wt,c,n,grad):
    for j in range(0,c,1):
        wt[j] += n*grad[j] 
        # print(w[j])
    return wt

def Re_Update_W(wt,c,n,grad):
    for j in range(0,c,1):
        wt[j] -= n*grad[j] 
        # print(w[j])
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
w = []
for j in range(0, cols, 1):
    w = initialize_W(w)


# Gradient Decent Iteration

eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001, .000000000001, .0000000000001, .00000000000001, .000000000000001, .0000000000000001, .00000000000000001 ]
currentErr = 0 
previousErr = 0
for k in range(0, 100000, 1): # Reduce No. of iterations for Assignment 2 Example
    delF = [0]*cols
    previousErr = currentErr
    delF = compute_Delf(rows,cols,labeldict,w,data)
    errobj = []
    for a in range(0, len(eta_list), 1):
        eta = eta_list[a]
        w = Update_W(w,cols,eta,delF)
        ##update error
        error = Compute_Error(rows,labeldict,w,data)
        errobj.append(error)
        ##remove the eta for the next
        w = Re_Update_W(w,cols,eta,delF)
    ##update bestobj and best_eta
    #find the minimum obj from obj list and give the best eta
    Err = min(errobj)
    bestetaindex = errobj.index(Err)
    eta = eta_list[bestetaindex]
    # Update W
    w = Update_W(w,cols,eta,delF)
    # Error Computation
    currentErr = Err
    print("Objective Difference: ", abs(currentErr-previousErr), " Iteration No. ", k)
    if(currentErr > previousErr):
        Stp_rate = currentErr - previousErr
    else:
        Stp_rate = previousErr - currentErr
    # if(Stp_rate == 0): # Uncomment for 0 convergence
    #     break
    # Stop condition = 0.001
    if(Stp_rate < 0.001):
        break

# Compute Noramalized W 
# normw = normalize_W(w,cols)
# print("||W||: ", normw)

# Compute Distance from the origin 
# d_origin = dist_origin(w,normw)
# print("Distance from Origin: ", d_origin)

labels_missing = []
for i in range(0, rows, 1):
    if(labeldict.get(i) == None):
        labels_missing.append(i)

# Prediction
prediction(rows,labeldict,w,data)


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