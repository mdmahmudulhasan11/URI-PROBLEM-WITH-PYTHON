# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:14:18 2021

@author: Lenovo
"""

n = int(input("the input value is: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        x = i
        if x>j:
            x=j
        if x>n-i+1:
            x = n-i+1
        if x>n-j+1:
            x = n-j+1
        print(f'{x:3d}',end='')
    print()