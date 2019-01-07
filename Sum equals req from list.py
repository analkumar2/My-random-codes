# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:11:53 2018

@author: analk
"""
#So, what this program does is, take the 'liso' which is a list of numbers. Then it sums these numbers in every combination possible so that the
#sum is equal to the 'req'

import math
import itertools
import numpy as np

req = 70
liso = np.array([10,6,2,6,9,1,9,6,3,9,2,7,7,12,11])
lis = np.array(sorted(liso)) #sorts in ascending order
done = []

   

for i in np.arange(1,len(lis)+1):
    combi = itertools.combinations(range(len(lis)),i)
    while True:
        try:
            pres = next(combi)
        except StopIteration:
            break
        sum = np.sum(lis[[pres]])            
        if sum > req:
            break
        elif sum == req:
            done.append(pres)