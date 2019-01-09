# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:00:46 2019

@author: mob42
"""

def mm():
    m = ['','January','Febuary','March','April','May','June','July','August','September','October','November','December']
    blank = 1
    for i in range(1,13):
        print(m[i])
        print('Sun\t','Mon\t','Tue\t','Wed\t','Thr\t','Fri\t','Sat\t')
        for j in range(0,blank):
            print('\t',end = ' ')
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 9 or i == 10 or i == 12:
            day = 32
        elif i == 2:
            day = 29
        else:
            day = 31
        for k in range(1,day):
            print(k,end = '\t ')
            blank+=1
            if blank%7 == 0:
                print()
                blank = 0
                
        print()
while 1:
    y = input('Enter the year(2018):')
    if y == '2018':
        mm()
        break
    else:
        print('error')