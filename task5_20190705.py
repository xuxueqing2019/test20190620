# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:17:26 2019

@author: 徐雪晴
"""

import numpy as np
import pandas as pd

left = pd.DataFrame({'key1':['foo','foo','bar'],
                     'key2':['one','two','one'],
                     'lval':[1,2,3]})
right = pd.DataFrame({'key1':['foo','foo','bar','bar'],
                     'key2':['one','one','two','two'],
                     'rval':[4,5,6,7]
                    })

pd.merge(left,right,on=['key1','key2'],how = 'outer')
pd.merge(left,right,on='key1')
pd.merge(left,right,on='key1',suffixes=('_left','_right'))

left1 = pd.DataFrame({'key':['a','b','a','a',
                             'b','c'],
                      'value': range(6)})


right1 = pd.DataFrame({'group_val':[3.5,7]},
                      index = ['a','b'])

pd.merge(left1,right1,left_on = 'key',right_index = True,
         how='outer')

arr = np.arange(12).reshape((3,4))
np.concatenate([arr,arr],axis=1)

s1=pd.Series([0,1],index = ['a','b'])
s2=pd.Series([2,3,4],index = ['c','d','e'])
s3=pd.Series([5,6],index = ['f','g'])

pd.concat([s1,s2,s3],axis=1)
s4= pd.concat([s1,s3])

pd.concat([s1,s4],axis = 1,join = 'inner')

pd.concat([s1,s4],axis = 1,join_axes = [['a','c','b','e']])

result=pd.concat([s1,s1,s3],
                 keys = ['one','two','three'])

result.unstack()

pd.concat([s1,s2,s3],axis =1, keys = ['one','two','three'])

df1  = pd.DataFrame(np.random.randn(3,4),
                    columns = ['a','b','c','d'])
df2  = pd.DataFrame(np.random.randn(2,3),
                    columns = ['b','d','a'])

pd.concat([df1,df2],ignore_index=True)

data = pd.read_csv('examples/macrodata.csv')

data.head()

periods=pd.PeriodIndex(year=data.year,quarter=data.quarter,
                       name='date')
columns = pd.Index(['realgdp','infl','unemp'],
                   name = 'item')

data = data.reindex(columns=columns)

data.index = periods.to_timestamp('D','end')

ldata = data.stack().reset_index().rename(columns={0:'value'})

pivoted = ldata.pivot('date','item','value')

ldata['value2']=np.random.randn(len(ldata))

pivoted = ldata.pivot('date','item')

pivoted['value'][:5]

unsacked = ldata.set_index(['date','item']).unstack('item')

unsacked[:7]

df = pd.DataFrame({'key':['foo','bar','baz'],
                   'A':[1,2,3],
                   'B':[4,5,6],
                   'C':[7,8,9]})
melted = pd.melt(df,['key'])
reshaped=melted.pivot('key','variable','value')

reshaped.reset_index()

pd.melt(df,id_vars=['key'],value_vars=['A','B'])

pd.melt(df,value_vars=['key','A','B'])