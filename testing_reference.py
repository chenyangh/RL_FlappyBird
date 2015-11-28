# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:14:10 2015

@author: ravi
"""
def change(list_L):
    list_L[0] = [x+2 for x in  list_L[0]]
    k = actual(list_L)
    return list_L


def actual(l):
    l[1] = l[1]+1
    inception(l)
    return 2


def inception(l):
    l[1] = l[1]+1

a = [[23,45],86]



print (change(a))