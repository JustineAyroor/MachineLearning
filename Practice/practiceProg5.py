#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 07:13:00 2018

@author: justineayroor
"""
# Write​ ​a​ ​Python​ ​program​ ​to​ ​multiply​ ​a​ ​matrix​ ​given​ ​in​ ​M​ ​with​ ​a​ ​vector​ ​u.
# Write​ ​a​ ​Python​ ​program​ ​to​ ​determine​ ​the​ ​transpose​ ​of​ ​a​ ​matrix
# Write​ ​a​ ​Python​ ​program​ ​to​ ​read​ ​a​ ​matrix​ ​from​ ​a​ ​file​ ​and​ ​transpose

# M = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
#
# u = [1,2,4]

def MakeMatrix(n,m):
    M = [0] * n
    for i in range(n):
        M[i] = [0] * m
    return M

def MakeVec(n):
    u = [0]*n
    return u

def fillMatrix(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("Value for ", i, "th Row &", j, "th Col")
            M[i][j] = int(input("Enter the Values: " ))
    return M

def fillVec(u):
    for i in range(len(u)):
        u[i] = int(input("Enter the Value of each Vectoe Elements:"))
    return u

def MatrixMul(M,u):
    result = [0]*len(M[0])
    for i in range(len(M[0])):
        for j in range(len(u)):
            result[i] = result[i] + M[j][i] * u[j]
    return result

def TransMatrix(M):
    tM = MakeMatrix(len(M[0]),len(M))
    for i in range(len(tM)):
        for j in range(len(tM[0])):
            tM[i][j] = M[j][i]
    return tM

# Matrix and Vector mul
n  = int(input("Enter number of Rows: "))
m  = int(input("Enter number of Cols: "))
Matrix = MakeMatrix(n,m)
Vector = MakeVec(n)
Matrix = fillMatrix(Matrix)
print(Matrix)
Vector = fillVec(Vector)
print(Vector)
res = MatrixMul(Matrix,Vector)
print('Multiplication Result:',res)

# Transpose of a matrix
tM = TransMatrix(Matrix)
print('Transpose Matrix Result:',tM)
