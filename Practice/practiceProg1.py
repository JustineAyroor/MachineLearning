#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:07:32 2018

@author: justineayroor
"""
# Problem Statement
# 1. Suppose​ ​we​ ​have​ ​a​ ​list​ ​l​ ​=​ ​[1,​ ​20,​ ​40,​ ​30,​ ​2,​ ​5,​ ​4].​ ​Write​ ​a​ ​for​ ​loop​ ​to​ ​determine​ ​if​ ​this​ ​list contains​ ​the​ ​number​ ​30.
# 2. Calculate​ ​the​ ​mean,​ ​max,​ ​min,​ ​median,​ ​and​ ​variance​ ​of​ ​a​ ​set​ ​of​ ​numbers​ ​in​ ​a​ ​list​ ​l​ ​(use the​ ​above​ ​list).

# import required libraries
import math

#define data structure
l = [18, 20, 40, 30, 23, 54, 14]

#define functions
def findNum():
    num = int(input('Enter Number to be Found in the list: '))
    position = 0
    for i in range(len(l)):
        if num == l[i]:
            #print('Number Found in list at position', i)
            position = i
    return position

def mean():
    temp = 0
    for i in range(len(l)):
        temp += l[i]
    mean = temp/len(l)
    return mean

def listmin():
    inival = l[0]
    for i in range(len(l)):
        if inival <= l[i]:
            minival = inival
        else:
            minival = l[i]
        inival = minival
    return minival
    
def listmax():
    inival = l[0]
    for i in range(len(l)):
        if inival >= l[i]:
            maxval = inival
        else:
            maxval = l[i]
        inival = maxval
    return maxval
    
def median():
    med = l[int(len(l)/2)]
    return med

def variance():
    u = mean()
    temp1 = 0
    for i in range(len(l)):
        temp = (l[i] - u)*(l[i] - u)
        temp1 +=temp
    var = temp1/len(l)
    return var

def Stand_Deviation():
    var = variance()
    sd = math.sqrt(var)
    return sd

#Map Function with Keys using a dictionary
allFuncDict = {
        "Min" : listmin(),
        "Max" : listmax(),
        "Mean" : mean(),
        "Median" : median(),
        "Variance" : variance(),
        "S.D" : Stand_Deviation(),
        "FindNum" : findNum()
        }

#Display the results
print(allFuncDict)