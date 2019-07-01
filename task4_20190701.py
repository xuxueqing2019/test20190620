# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:32:39 2019

@author: 徐雪晴
"""

import numpy as np
import pandas as pd

string_data = pd.Series(['aardvark','artichoke',np.nan,'avocado'])

string_data.isnull()

string_data[0] = None

from numpy import nan as NA

data  = pd.Series([1,NA,3.5,NA,7])

data.dropna

data[data.notnull()]
data = pd.DataFrame([[1,6.5,3],[1,NA,NA],[NA,NA,NA],[NA,6.5,3]])
cleaned =data.dropna()
data.dropna(axis = 1,how='all')

data[4]=NA

df = pd.DataFrame(np.random.randn(7,3))

df.iloc[:4,1]=NA
df.iloc[:2,2]=NA

df.dropna(thresh=2)

df.fillna(0)

df.fillna({1:0.5,2:0})

df = pd.DataFrame(np.random.randn(6,3))

df.iloc[2:,1]=NA
df.iloc[4:,2]=NA

df.fillna(method = 'ffill',limit=2)


data = pd.Series([1,NA,3.5,NA,7])
data.fillna(data.mean())

data = pd.DataFrame({'k1':['one','two']*3 + ['two'],
                     'k2':[1,1,2,3,3,4,4]})

data.duplicated()

data.drop_duplicates(['k1','k2'],keep = 'last')

data['v1']=range(7)

data = pd.DataFrame({'food':['bacon','pulled pork','bacon',
                             'Pastrami','corned beef','Bacon','pastrami',
                             'honey ham','nova lox'],
'ounces':[4,3,12,6,7.5,8,3,5,6]})

meat_to_animal = {
        'bacon':'pig',
        'pulled pork':'pig',
        'pastrami':'cow',
        'corned beef':'cow',
        'honey ham':'pig',
        'nova lox':'salmon'
        }

lowercased = data['food'].str.lower()

data['animal'] =lowercased.map(meat_to_animal)

data['food'].map(lambda x:meat_to_animal[x.lower()])

data = pd.Series([1,-999,2,-999,-1000,3])

data.replace([-999,-1000],[np.nan,0])

data.replace({-999:np.nan,-1000:0})

ages = [20,22,25,27,21,23,37,61,45,41,32]

bins = [18,25,35,60,100]

cats = pd.cut(ages,bins)
cats.codes
cats.categories
pd.value_counts(cats)

pd.cut(ages,[18,26,36,61,100],right = False)

group_names = ['Youth','YoungAdult','MiddleAged','Senior']

pd.cut(ages,bins,labels = group_names)

data = np.random.randn(20)
pd.cut(data,4,precision = 2)

data = np.random.randn(1000)
cats = pd.qcut(data,4)

cats = pd.qcut(data,[0,0.1,0.5,0.9,1])

data = pd.DataFrame(np.random.randn(1000,4))

data.describe()

col = data[2]

col[np.abs(col)>0.9]

data[(np.abs(data)>3).any(1)]

data[np.abs(data)>3]=np.sign(data)*3

np.sign(data).head()

df = pd.DataFrame(np.arange(5*4).reshape((5,4)))
sampler = np.random.permutation(5)

df.take(sampler)
df.sample(n=3)

df = pd.DataFrame(({'key':['b','b','a','c','a','b'],
                    'data1':range(6)}))

pd.get_dummies(df['key'])
dummies = pd.get_dummies(df['key'],prefix = 'key')
df_with_dummy = df[['data1']].join(dummies)

mnames = ['movie_id','title','genres']

movies =pd.read_table('datasets/movielens/movies.dat',
                      sep='::',
                      header = None,names = mnames)

all_genres = []

for x in movies.genres:
    all_genres.extend(x.split('|'))

genres = pd.unique(all_genres)

zero_matrix = np.zeros((len(movies),len(genres)))

dummies = pd.DataFrame(zero_matrix,columns = genres)

gen = movies.genres[0]

gen.split('|')

dummies.columns.get_indexer(gen.split('|'))

for i,gen in enumerate(movies.genres):
    indices = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i,indices] = 1

movies_windic = movies.join(dummies.add_prefix('Genre_'))

movies_windic.iloc[0]