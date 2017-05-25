# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 08:10:20 2016

@author: theresa
"""
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] 
# then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """

    for item in L:
        item.reverse()
    L.reverse()


#list = [[1, 2], [3, 4], [5, 6, 7]] 
#deep_reverse(list)

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L) 
print(L)