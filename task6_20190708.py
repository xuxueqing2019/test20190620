# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:49:46 2019

@author: 徐雪晴
"""

import numpy as np
import pandas as pd

df=pd.DataFrame({'key1':['a','a','b','b','a'],
                 'key2':['one','two','one','two','one'],
                 'data1':np.random.randn(5),
                 'data2':np.random.randn(5)})

grouped = df['data1'].groupby(df['key1'])

grouped.mean()

states = np.array(['O','C','C','O','O'])

years=np.array([2005,20005,2006,2005,2006])

df['data1'].groupby([states,years]).mean()

df.groupby('key1').mean()

df.groupby(['key1','key2']).mean()

df.groupby(['key1','key2']).size()

for name,group in df.groupby('key1'):
    print(name)
    print(group)
    
for (k1,k2),group in df.groupby(['key1','key2']):
    print(k1,k2)
    print(group)
    
pieces = dict(list(df.groupby('key1')))

pieces['b']

df.dtypes

grouped = df.groupby(df.dtypes,axis=1)

for dtype,group in grouped:
    print(dtype)
    print(group)
    
grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)

def peak_to_peak(arr):
    return arr.max()-arr.min()

grouped.agg(peak_to_peak)
grouped.describe()

tips = pd.read_csv('examples/tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']
grouped = tips.groupby(['day','smoker'])
grouped_pct = grouped['tip_pct']

grouped_pct.agg(['mean','std',peak_to_peak])

grouped_pct.agg([('foo','mean'),('bar',np.std)])

grouped.agg({'tip':np.max,'size':'sum'})

tips.groupby(['day','smoker'],as_index = False).mean()

def top(df,n=5,column = 'tip_pct'):
    return df.sort_values(by=column)[-n:]

top(tips,n=6)

tips.groupby('smoker').apply(top)

tips.groupby(['smoker','day']).apply(top,n=1,
            column = 'total_bill')

s= pd.Series(np.random.randn(6))
s[::2]=np.nan

s.fillna(s.mean())

states = ['Ohio','New York','Vermont','Florida',
          'Oregon','Nevada','California','Idaho']

group_key = ['East']*4+['West']*4

data = pd.Series(np.random.randn(8),index = states)

data[['Vermont','Nevada','Idaho']]=np.nan

data.groupby(group_key).mean()

fill_mean = lambda g:g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean)

fill_values={'East':0.5,'West':-1}

fill_func = lambda g:g.fillna(fill_values[g.name])

data.groupby(group_key).apply(fill_func)

suits = ['H','S','C','D']
card_val = (list(range(1,11))+[10]*3)*4

base_names = ['A']+list(range(2,11))+['J','K','Q']

cards=[]
for suit in ['H','S','C','D']:
    cards.extend(str(num)+suit for num in base_names)
    
deck =pd.Series(card_val,index=cards)

def draw(deck,n=5):
    return deck.sample(n)

draw(deck)

get_suit =lambda card:card[-1]

deck.groupby(get_suit).apply(draw,n=2)

df = pd.DataFrame({'category':['a','a','a','a',
                               'b','b','b','b'],
    'data':np.random.randn(8),
    'weights':np.random.randn(8)})
    
grouped = df.groupby('category')
get_wavg = lambda g:np.average(g['data'],
                               weights=g['weights'])
grouped.apply(get_wavg)

close_px = pd.read_csv('examples/stock_px_2.csv',
                       parse_dates=True,
                       index_col = 0)

close_px.info()

close_px[-4:]

spx_corr = lambda x:x.corrwith(x['SPX'])

rets=close_px.pct_change().dropna()

get_year = lambda x:x.year
by_year = rets.groupby(get_year)
by_year.apply(spx_corr)
by_year.apply(lambda g:g['AAPL'].corr(g['MSFT']))


import statsmodels.api as sm
def regress(data,yvar,xvars):
    Y=data[yvar]
    X=data[xvars]
    X['intercept']=1.
    result = sm.OLS(Y,X).fit()
    return result.params

by_year.apply(regress,'AAPL',['SPX'])

tips.pivot_table(index=['day','smoker'])

tips.pivot_table(['tip_pct','size'],index = ['time','day'],
                 columns='smoker',
                 margins=True)
tips.pivot_table('tip_pct',index=['time','smoker'],
                 columns = 'day',
                 aggfunc = len,
                 fill_value = 0,
                 margins=True)


pd.crosstab([tips.time,tips.day],tips.smoker,
            margins=True)


