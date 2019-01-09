# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:56:58 2019

@author: mob42
"""
import pandas as pd
minder = pd.read_csv('gapminder.csv')
print('內容')
print(minder)
print('長度',minder.index)
print('形狀',minder.shape)
print('維度',minder.ndim)

print('前五筆資料')
print(minder.head())
print('後五筆資料')
print(minder.tail())
print('分別樹出第0列、第四列的所有資料:')
print(minder.iloc[[0]])
print(minder.iloc[[4]])
print('別輸出第0行:')
print(minder.iloc[:,0])
print('第二航的所有資料:')
print(minder.iloc[:,2])
print('輸出前30筆的第三行所有資料:')
print(minder.iloc[:,3].head(30))
print('輸出篩選條件為國家貝南、地區為北非且年份是1972或是1957的所有資料:')
print(minder[(minder['country'] == 'Benin')&(minder['continent'] == 'Africa') & ((minder['year']==1972)|(minder['year'] == 1957))])
print('輸出篩選條件為含有A開頭國家的所有資料:')
print(minder[(minder['country'] < 'B')])