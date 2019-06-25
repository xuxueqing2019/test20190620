# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:45:15 2019

@author: 徐雪晴
"""
import numpy as np
import pandas as pd

from pandas import Series,DataFrame

obj = pd.Series([4,7,-5,3])

obj.values

obj.index

obj2 = pd.Series([4,7,-5,3],index = ['d','b','a','c'])

obj2.index

obj2['a']

obj2[['a','d']]

obj2[obj2>0]

obj2*2

np.exp(obj2)

'b' in obj2

'e' in obj2

sdata ={'Ohio':3500,'Texas':71000,'Oregon':16000,'Utah':5000}

obj3 = pd.Series(sdata)

states = ['California','Ohio','Oregon','Texas']

obj4=pd.Series(sdata,index = states)

pd.isnull(obj4)

pd.notnull(obj4)

obj4.isnull()

obj3+obj4

obj4.name = 'population'

obj4.index.name = 'sate'

obj4

obj

obj.index = ['Bob','Steve','Jeff','Ryan']

data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002,2003],
        'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}

frame = pd.DataFrame(data)

frame
frame.head()
pd.DataFrame(data,columns = ['year','state','pop'])

frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],
                    index = ['one','two','three','four','five','six'])

frame2

frame2.columns

frame2['state']

frame2.year
frame2.loc['three']
frame2['debt']=16.5

frame2['debt']=np.arange(6)

val = pd.Series([-1.2,-1.5,-1.7],index = ['two','four','five'])
frame2['debt']=val
frame2['eastern']= frame2.state =='Ohio'

del frame2['eastern']

pop = {'Nevada':{2001:2.4,2002:2.9},
       'Ohio':{2000:1.5,2001:1.7,2002:3.6}}

frame3 = pd.DataFrame(pop)

frame3.T

pd.DataFrame(pop,index=[2001,20002,2003])

frame2.values

obj = pd.Series(range(3),index = ['a','b','c'])

index = obj.index

index

index[1:]

index[1] = 'd'

frame3

'Ohio' in frame3.columns

2003 in frame3.index

dup_labels = pd.Index(['foo','foo'])
dup_labels

obj =  pd.Series([4.5,7.2,-5.3,3.6],index = ['d','b','a','c'])

obj2 = obj.reindex(['a','b','c','d','e'])

obj3 = pd.Series(['blue','purple','yellow'],
                 index=[0,2,4])

obj3.reindex(range(6),method = 'ffill')

frame =pd.DataFrame(np.arange(9).reshape((3,3)),
                              index = ['a','c','d'],
                              columns=['Ohio','Texas','California'])

frame2 = frame.reindex(['a','b','c','d'])

states = ['Texas','Utah','California']

frame.reindex(columns = states)

obj = pd.Series(np.arange(5),index = ['a','b','c','d','e'])

new_obj = obj.drop('c')

obj.drop(['d','c'])

data = pd.DataFrame(np.arange(16).reshape(4,4),
                    index = ['Ohio','Colorado','Utah','NewYork']
                    ,columns = ['one','two','three','four'])

data.iloc[2]

data.loc[:'Utah','two']

data.iloc[:,:3][data.three >5]

ser = pd.Series(np.arange(3))

ser[-1]
ser2 = pd.Series(np.arange(3),index = ['a','b','c'])
ser2[-1]

ser[:1]
ser.loc[:1]
ser.iloc[:1]

df1 = pd.DataFrame({'A':[1,2]})
df2 = pd.DataFrame({'B':[3,4]})

df1-df2

frame = pd.DataFrame(np.arange(12).reshape((4,3)),
                     columns = list('bde'),
                     index =['Utah','Ohio','Texas','Oregon'])

series2 = pd.Series(range(3),index =['b','e','f'])

frame + series2