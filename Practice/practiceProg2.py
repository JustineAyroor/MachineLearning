#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:07:32 2018

@author: justineayroor
"""
# Problem Statement
# 7. Write​ ​a​ ​Python​ ​program​ ​to​ ​do​ ​the​ ​dot​ ​product​ ​between​ ​two​ ​vectors​ ​given​ ​as​ ​lists​ ​of​ ​the same​ ​length

# Define 2 tuples as vectors
v1 = []
v2 = []
# Make User enter number of elements in both vectors
n = int(input('Enter the number of elements in the vectors:'))
    
def init():
    # Set the vector elements
    set_elements()
    # Display the vectors
    display_elements()
    # Use the dot product formula and display the result
    print('Dot Product of the 2 Vectors :', dot_prod_logic())

 # Set the vector elements
def set_elements():
    for i in range(n):
        inpt1 = int(input('Enter the elements in v1:'))
        v1.append(inpt1)
    
    for i in range(n):
        inpt2 = float(input('Enter the elements in v2:'))
        v2.append(inpt2)
# Display the vectors
def display_elements():
    print(v1)
    print(v2)        

# Use the dot product formula and display the result
def dot_prod_logic():
    result = 0
    for i in range(n):
        temp = v1[i]*v2[i]
        result += temp
    return result

#Call the initialization function to run the whole code 
init()