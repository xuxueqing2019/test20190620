# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 19:46:55 2019

@author: 徐雪晴
"""

import numpy as np
import pandas as pd

val = 'a,b, guido'
pieces = [x.strip() for x in val.split(',')]

'::'.join(pieces)

'guido' in val

val.find(':')

val.count(',')

val.replace(',','')

import re

text = "foo   bar\t baz   \tqux"

re.split('\s+',text)

regex = re.compile('\s+')

regex.split(text)

regex.findall(text)

text = """Dave dave@google.com 
Steve steve@gmail.com 
Rob rob@gmail.com 
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9._-]+\.[A-Z]{2,4}'
regex.findall(text)

m = regex.search(text)


text[m.start():m.end()]


data= {'Dave':'dave@google.com',
'Steve':'steve@gmail.com', 
'Rob':'rob@gmail.com',
'Ryan':'ryan@yahoo.com',
'Wes':np.nan}

data.isnull()

data.str.contains('gmail')


