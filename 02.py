# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:11:06 2019

@author: mob42
"""
import numpy as np
print('arrayA:')
arrayA = np.random.randn(7,5)
print(arrayA)
print(arrayA.shape)
print(arrayA.ndim)
print('-------')
print('arrayB:')
arrayB = np.reshape(arrayA,35)
print(arrayB)
print(arrayB.shape)
print(arrayB.ndim)
print('-------')
print('亂數:')
np.random.shuffle(arrayB)
print(arrayB)
max1 = np.max(arrayB)
min1 = np.min(arrayB)
total1 = np.sum(arrayB)
mean1 = np.mean(arrayB)
print('最大值:',max1)
print('最小值:',min1)
print('種合',total1)
print('平均:',mean1)
print('-------')
listA = [max1,min1,total1,mean1]
print('listA:',listA)
np.random.shuffle(arrayB)
arrayB = np.reshape(arrayB,(7,5))
max2 = np.max(arrayB)
min2 = np.min(arrayB)
total2 = np.sum(arrayB)
mean2 = np.mean(arrayB)
listB = [max2,min2,total2,mean2]
print('listB:',listB)
listC = []
for i in range(len(listA)):
    listC.append(listA[i]+listB[i])
    
print('listC 平均數:',np.mean(listB))