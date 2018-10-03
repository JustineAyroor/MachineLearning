#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 06:14:00 2018

@author: justineayroor
"""
# Write​ ​a​ ​Python​ ​program​ ​to​ ​sort​ ​a​ ​list​ ​of​ ​numbers​ ​using​ ​the​ ​bubblesort​ ​algorithm Bubblesort​ ​algorithm​ ​to​ ​sort​ ​a​ ​list​ ​of​ ​numbers​ ​called​ ​l:
# for​ ​i​ ​=​ ​0​ ​to​ ​length(l),​ ​i=i+1​ ​{
# for​ ​j​ ​=​ ​i+1​ ​to​ ​length(l),​ ​i=i+1​ ​{
# if(l[i]​ ​>​ ​l[j]​ ​then​ ​switch​ ​l[i]​ ​and​ ​l[j] }
# }

l = []
n = int(input("Enter elements for the list:"))
for i in range(n):
    inp = int(input("Enter Elements in the list:"))
    l.append(inp)
#l = [20, 5, 50, 34, 47, 16, 12, 64, 40, 32]
tempvar = 0
print('Ascending Order')
for i in range(len(l)):
    for j in range(len(l)):
        if(l[i]<l[j]):
            tempvar = l[i]
            l[i] = l[j]
            l[j] = tempvar
print(l)
print('Decending Order')
for i in range(len(l)):
    for j in range(len(l)):
        if(l[i]>l[j]):
            tempvar = l[i]
            l[i] = l[j]
            l[j] = tempvar
print(l)
