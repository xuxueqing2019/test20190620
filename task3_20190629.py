# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:52:16 2019

@author: 徐雪晴
"""

import numpy as np
import pandas as pd

import os 
os.getcwd()

!type examples\ex1.csv

df = pd.read_csv('examples/ex1.csv')

df

pd.read_table('examples/ex1.csv',sep=',')


!type examples\ex2.csv

pd.read_csv('examples/ex2.csv',header=None)

pd.read_csv('examples/ex2.csv',
            names =['a','b','c','message'])

 names =['a','b','c','d','message']
 
 pd.read_csv('examples/ex2.csv',names=names,
             index_col = 'message')
 
 !type examples\csv_mindex.csv
 
 parsed =pd.read_csv('examples/csv_mindex.csv',
                     index_col=['key1','key2'])
 
 list(open('examples/ex3.txt'))
 
 result =pd.read_table('examples/ex3.txt',sep='\s+')
 
  !type examples\ex4.csv
  
 pd.read_csv('examples/ex4.csv',skiprows=[0,2,3])

    !type examples\ex5.csv
 result =pd.read_table('examples/ex5.csv',sep=',')
 result
 
 pd.isnull(result)
 
result =pd.read_table('examples/ex5.csv',
                      sep=',',
                      na_values=['NULL'])

sentinels = {'message':['foo','NA'],
             'something':['two']}
 
result =pd.read_table('examples/ex5.csv',
                      sep=',',
                      na_values=sentinels)

pd.options.display.max_rows=10

result =pd.read_table('examples/ex6.csv',sep=',')


pd.read_csv('examples/ex6.csv',sep=',',nrows=5)

chunker = pd.read_csv('examples/ex6.csv',sep=',',chunksize=1000)

chunker

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(),fill_value=0)
    
    tot = tot.sort_values(ascending = False)
    
tot[:10]

data = pd.read_csv('examples/ex5.csv')

data.to_csv('examples/out.csv')

import sys

data.to_csv(sys.stdout,sep='|')

data.to_csv(sys.stdout,na_rep='NULL')

dates = pd.date_range('1/1/2000',periods=7)

ts = pd.Series(np.arange(7),index = dates)

ts.to_csv('examples/tseries.csv')

!type examples\tseries.csv

!type examples\ex7.csv

import csv
f=open('examples/ex7.csv')

reader = csv.reader(f)

for line in reader:
    print(line)
    
with open('examples/ex7.csv') as f:
    lines = list(csv.reader(f))
    
    header,values = lines[0],lines[1:]
    
data_dict = {h:v for h,
            v in zip(header,zip(*values))}
f

class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
    reader =csv.reader(f,dialect=my_dialect)
    
reader = csv.reader(f,delimiter = '|')

with open('mydata.csv','w') as f:
    writer = csv.writer(f,dialect = my_dialect)
    writer.writerow(('one','two','three'))
    writer.writerow(('1','2','3'))
    writer.writerow(('4','5','6'))
    
obj = """
{"name":"Wes",
"places_lived":["United States","Spain","Germany"],
"pet":null,
"siblings":
    [{"name":"Scott","age":30,"pets":["Zeus","Zuko"]},
{"name":"Katie","age":38,"pets":["Sixes","Stache","Cisco"]}
]}"""
   
    import json
  result=json.loads(obj)  
  
  asjson = json.dumps(result)
  
  siblings = pd.DataFrame(result['siblings'],
                          columns=['name','age'])
  
  !type examples\example.json
  
  data = pd.read_json('examples/example.json')
  
  print(data.to_json(orient='records'))
 
    conda install lxml
pip install beautifulsoup4 html5lib  
  
tables = pd.read_html('examples/fdic_failed_bank_list.html')

len(tables)

failures=tables[0]

failures.head()

from lxml import objectify

path = 'datasets/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []
skip_fields = ['PRENT_SEQ','INDICATOR_SEQ',
               'DESIRED_CHANGE','DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag]=child.pyval
        data.append(el_data)
        
perf = pd.DataFrame(data)
perf.head()

from io import StringIO
tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()

root.get('href')

root.text

frame = pd.read_csv('examples/ex1.csv')

frame.to_pickle('examples/frame_pickle')

pd.read_pickle('examples/frame_pickle')

frame=pd.DataFrame({'a':np.random.randn(100)})

store = pd.HDFStore('mydata,h5')

store['obj1']=frame

store['obj1_col']=frame['a']

store.put('obj2',frame,format = 'table')

store.select('obj2',where=['index >=10 and index <=15'])

store.close()

frame.to_hdf('mydata.h5','obj3',format = 'table')
pd.read_hdf('mydata.h5','obj3',where = ['index<5'])

xlsx = pd.ExcelFile('examples/ex1.xlsx')

pd.read_excel(xlsx,'Sheet1')

frame = pd.read_excel('examples/ex1.xlsx','Sheet1')

writer = pd.ExcelWriter('examples/ex2.xlsx')
frame.to_excel(writer,'Sheet1')
writer.save()

frame.to_excel('examples/ex2.xlsx')

import requests

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)

data = resp.json()

data[0]['title']

issues = pd.DataFrame(data,columns = ['number','title',
                                      'labels','state'])
    
import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20),b VARCHAR(20),
c REAL,d INTEGER);"""

 con = sqlite3.connect('mydata.sqlite')
 con.execute(query)
 con.commit()
 
 data = [('Atlanta','Georgia',1.25,6),
 ('Tallahassee','Florida',2.6,3),
 ('Sacramento','California',1.7,5)]
 
 stmt = "INSERT INTO test VALUES(?,?,?,?)"
 
 con.executemany(stmt,data)
 
 cursor = con.execute('select * from test')
 
 rows = cursor.fetchall()
 cursor.description
 
 pd.DataFrame(rows,columns=[x[0] for x in
                            cursor.description])
 
 import sqlalchemy as sqla
 
 db = sqla.create_engine('sqlite:///mydata.sqlite')
 
 pd.read_sql('select * from test',db)