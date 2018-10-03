#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 04:45:53 2018

@author: justineayroor
"""
# Suppose​ ​you​ ​have​ ​a​ ​list​ ​of​ ​DNA​ ​sequences.​ ​What​ ​is​ ​the​ ​average​ ​sequence​ ​length​ ​of​ ​the list?
# Suppose​ ​the​ ​list​ ​contains​ ​the​ ​organism​ ​name​ ​followed​ ​by​ ​the​ ​sequence.​ ​What​ ​is​ ​the average​ ​sequence​ ​length?​ ​Print​ ​the​ ​name​ ​of​ ​the​ ​organism​ ​with​ ​the​ ​longest​ ​sequence.
# Suppose​ ​you​ ​are​ ​given​ ​a​ ​DNA​ ​sequence​ ​in​ ​the​ ​variable​ ​seq.​ ​Write​ ​code​ ​to​ ​determine the​ ​reverse​ ​complement.
# Suppose​ ​you​ ​have​ ​a​ ​DNA​ ​sequence​ ​in​ ​the​ ​variable​ ​seq.​ ​Produce​ ​a​ ​new​ ​sequence exactly​ ​the​ ​same​ ​except​ ​the​ ​first​ ​letter​ ​is​ ​‘C’.

import math
#l = ['abcdefghijk','hdgdgsygsvai','dghsduhgusghsub','vsduvihsdugeshdz','hdvsgyeyfrughvfjkbvaksbvkdabv','dvgiudsgvuidabkdbcd']
l = {'Justine':'AJFAIVSDVHDBVHDZBVVB','Divya':'UDSHVSIUGVUDISGVBVU',
'Kevin':'DSKVHSDSJNVDJBV','Ronald':'VDVBVBXBVXBXCKBVVAIZND',
'Domnic':'KJVZBVZDBVDBVZDVDVDU','Hursh':'EIUYEUTYAGHAORHGIORHAZK',
'Vishal': 'SIUGHAIUGURSHGAEIOGVJC', 'Julian': 'DHSIUHVDUFVXIVDU'}
a = []
reverseVals = []
keyDets = []
newDictwithC = []
lengthlist = []
j = 0
meanlength = 0
for i in l:
    a.append(l.get(i))
    meanlength += len(a[j])
    lengthlist.append(len(a[j]))
    j += 1
# print(a)
print('-------------------------------------------------')
print('Average length of the elements in the list:', meanlength/len(a))
print('-------------------------------------------------')
lengthlist.sort()
maxlength = lengthlist[(len(a)-1)]
for i in l:
    if(maxlength == len(l.get(i))):
        print('Name:', i, '\tMax Length of sequence: ', maxlength)
print('-------------------------------------------------')

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
def add_and_Replace_with_C(s):
    str = ""
    listofchar = []
    for i in s:
        listofchar.append(i)
    listofchar[0] = 'C'
    for j in range(0,len(listofchar),1):
        str += listofchar[j]
    return str
for i in l:
    reverseVals.append(reverse(l.get(i)))
    newDictwithC.append(add_and_Replace_with_C(l.get(i)))
    keyDets.append(i)
# print(reverseVals)
# print(keyDets)
zipbObj1 = zip(keyDets, reverseVals)
zipbObj2 = zip(keyDets, newDictwithC)
dict_with_reverseSeq = dict(zipbObj1)
dict_with_C = dict(zipbObj2)
print(l)
print('-------------------------------------------------')
print(dict_with_reverseSeq)
print('-------------------------------------------------')
print(dict_with_C)
