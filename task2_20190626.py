# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:33:07 2019

@author: 徐雪晴
"""
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randn(4,3),
                     columns = list('bde'),
                     index=['Utah','Ohio','Texas','Oregon'])

np.abs(frame)

f= lambda x:x.max()-x.min()
frame.apply(f)
frame.apply(f,axis='columns')

def f(x):
    return pd.Series([x.min(),x.max()],
                      index=['min','max'])
    
    frame.apply(f)
    
    format =lambda x:'%.2f'%x
    
    frame.applymap(format)
    
    frame['e'].map(format)
    
obj = pd.Series(range(4),index = ['d','a','b','c'])

obj.sort_index()

obj = pd.Series([7,-5,7,4,2,0,4])

obj.rank()

obj.rank(method = 'first')

obj.rank(ascending = False,method = 'max')

frame = pd.DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],
                      'c':[-2,5,8,-2.5]})
    
    frame
    
    frame.rank(axis='columns')
    
    df =pd.DataFrame([[1.4,np.nan],[7.1,-4.5]],
                     index=['a','b'],
                     columns=['one','two'])
    
   df1= df.sum()
   
   df.sum(axis=1)
   
   df.idxmax()
   
   df.cumsum()
   
   df.describe()
   
   obj=pd.Series(['a','a','b','c']*4)
   obj.describe()
   
   conda install pandas-datareader
   import pandas_datareader.data as web
   
   import datetime
   start =datetime.datetime(2016,1,1)   
   end = datetime.date.today()
   prices=web.DataReader('AAPL','yahoo',start,end)
   
   print prices.head()
   
   all_data = {ticker:web.get_data_yahoo(ticker)
   for ticker in ['AAPL','IBM','MSFT','GOOG']}
   
   price = pd.DataFrame({ticker:data['Adj Close']
   for ticker,data in all_data.items()})
   
   volume = pd.DataFrame({ticker:data['Volume']
   for ticker,data in all_data.items()})
   
   returns = price.pct_change()
   
   returns.tail()
   
   returns['MSFT'].corr(returns['IBM'])
      returns['MSFT'].cov(returns['IBM'])
      returns.corr()
      
      returns.corrwith(returns.IBM)
       returns.corrwith(volume)
       
       data = pd.DataFrame({'Q1':[1,3,4,3,4],
                            'Q2':[2,3,1,2,3],
                            'Q3':[1,5,2,4,4]}
  )
       
       result =data.apply(pd.value_counts).fillna(0)
       
              result =data.apply(pd.value_counts)