# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:31:00 2019

@author: 徐雪晴
"""

import numpy as np
import pandas as pd

data = pd.Series(np.random.randn(9),
                 index=[['a','a','a','b','b',
                         'c','c','d','d'],
[1,2,3,1,3,1,2,2,3]])

data.index
data['b':'c']

data.loc[:,2]

data.unstack().stack()

frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     index = [['a','a','b','b'],[1,2,1,2]],
                     columns = [['Ohio','Ohio','Colorado'],
                                ['Green','Red','Green']])

frame.index.names = ['key1','key2']
frame.columns.names = ['state','color']

frame['Ohio']

MultiIndex.from_arrays([['Ohio','Ohio','Colorado'],
                                ['Green','Red','Green']],
names = ['state','color'])

frame.swaplevel('key1','key2')

frame.swaplevel(0,1).sort_index(level = 0)

frame.sum(level ='key2')
frame.sum(level ='color',axis=1)

frame = pd.DataFrame({'a':range(7),
                      'b':range(7,0,-1),
                      'c':['one','one','one',
                           'two','two','two','two'],
                           'd':[0,1,2,0,1,2,3]})

frame2=frame.set_index(['c','d'])

frame.set_index(['c','d'],drop=False)
frame2.reset_index()

df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],
                    'data1':range(7)})
df2 = pd.DataFrame({'key':['a','b','d'],
                    'data2':range(3)})

pd.merge(df1,df2,on='key')
pd.merge(df1,df2,how='outer')

df3 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'],
                    'data1':range(7)})
df4 = pd.DataFrame({'rkey':['a','b','d'],
                    'data2':range(3)})

pd.merge(df3,df4,left_on='lkey',right_on = 'rkey')

