# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:18:37 2019

@author: 徐雪晴
"""

import numpy as np

my_arr = np.arange(1000000)

my_list=list(range(1000000))

my_arr2=my_arr *2

 my_list2=[x*2 for x in my_list]
 
 data = np.random.randn(2,3)
 
 data *10
 
 data +data
 
 data.shape
 
 data.dtype
 
 data1 = [6, 7.5, 8, 0, 1]
 
 arr1 = np.array(data1)
 
 data2 = [[1,2,3,4],[5,6,7,8]]
 
 arr2= np.array(data2)
 
 arr2
 
 arr2.ndim
 
 arr2.shape
 
 arr1.dtype
 
 arr2.dtype
 
 np.zeros(10)
 
 np.zeros((3,6))
 
 np.empty((2,3,2))
 
# data_emp = np.empty((2,3,2))
 
 np.arange(15)
 
 arr1 = np.array([1,2,3],dtype =np.float64)
 
 arr2 = np.array([1,2,3],dtype =np.int32)
 
 arr1.dtype
 
 arr2.dtype
 
 arr=np.array([1,2,3,4,5])
 
 arr.dtype
 
 float_arr = arr.astype(np.float64)
 float_arr.dtype
 
 arr =np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])
 
 arr.astype(np.int32)
 
 numeric_strings = np.array(['1.25','-9.6','42'],
                            dtype=np.string_)
 
 numeric_strings.astype(float)
 
 int_array = np.arange(10)
 
 calibers = np.array([.22,.270,.357,.380,.44,.50],
                     dtype = np.float64)
 
 int_array.astype(calibers.dtype)
 
 empty_uint32 = np.empty(8,dtype = 'u4')
 
 empty_uint32
 
 arr = np.array([[1.,2.,3.],[4.,5.,6.]])
 
 
 arr*arr
 
 arr-arr
 
 1/arr
 
 arr**0.5
 
 arr2 = np.array([[0.,4.,1.],[7.,2.,12.]])
 
 arr2 >arr
 
 arr = np.arange(10)
 
 arr[5]
 
 arr[5:8]
 
  arr[5:8]=12
  
  arr_slice = arr[5:8]
  

  arr_slice[1]=12345
  
  arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
  
  arr2d[2]
  
  arr2d[0][2]
  
  arr2d[0,2]
  
  arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
  
  arr3d[0]
  
  old_values = arr3d[0].copy()
  
  arr3d[0]=42
   
  arr3d[0]=old_values
  
arr2d

arr2d[:2]

arr2d[:,:1]

arr2d[:2,1:]

names= np.array(['bob','joe','will','bob','will','joe','joe'])

data = np.random.randn(7,4)

names =='bob'

data[names=='bob']

cond = names =='bob'

data[~cond]

data[data <0]=0

arr = np.empty((8,4))

for i in range(8):
    arr[i]=i
    
    arr[[4,3,0,6]]
    
    arr[[-3,-5,-7]]
    
    arr = np.arange(32).reshape((8,4))
    
    arr[[1,5,7,2],[0,3,1,2]]
    
    arr=np.arange(15).reshape((3,5))
    
    arr.T
    
    arr = np.random.randn(6,3)
    
    np.dot(arr.T,arr)
    
    arr = np.arange(16).reshape((2,2,4))
    
    arr.transpose((1,0,2))
    
    arr.swapaxes(1,2)
    
    arr = np.arange(10)
    
    np.sqrt(arr)
    
    np.exp(arr)
    
    x=np.random.randn(8)
    y=np.random.randn(8)
    
    np.maximum(x,y)
    
    arr = np.random.randn(7)*5
    
    remainder,whole_part = np.modf(arr)
    
    np.sqrt(arr)
    
    np.sqrt(arr,arr)
    
    points= np.arange(-5,5,0.01)
    
    xs,ys = np.meshgrid(points,points)
    
    z=np.sqrt(xs**2+ys**2)
    
    import matplotlib.pyplot as plt
    
    plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
    
    xarr = np.array([1.1,1.2,1.3,1.4,1.5]) 
    yarr=np.array([2.1,2.2,2.3,2.4,2.5])
    
    cond = np.array([True,False,True,True,False])
    
    result = [(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
    
    result = np.where(cond,xarr,yarr)
    
    arr = np.random.randn(4,4)
    
    arr >0
    
    np.where(arr>0,2,-2)
    
    arr = np.random.randn(5,4)
    
    arr.mean()
    np.mean(arr)
    
    arr.sum()
    
    arr.mean(axis=1)
    
    arr.sum(axis=0)
    
    arr = np.array([0,1,2,3,4,5,6,7])
    
    arr.cumsum()
    
    arr = np.random.randn(100)
    
    (arr>0).sum()
    
    bools =np.array([False,False,True,False])
    
    bools.any()
    
    bools.all()
    
    arr =np.random.randn(6)
    
    arr.sort()
    
    arr = np.random.randn(5,3)
    
    arr.sort(1)
    
    large_arr = np.random.randn(1000)
    
    large_arr.sort()
    
    large_arr[int(0.05*len(large_arr))]
    
  names= np.array(['bob','joe','will','bob','will','joe','joe'])
np.unique(names)  
sorted(set(names))
    
values = np.array([6,0,0,3,2,5,6])
np.in1d(values,[2,3,6])

arr = np.arange(10)
np.save('some_array',arr)

np.load('some_array.npy')

np.savez('array_archive.npz',a=arr,b=arr)
arch = np.load('array_archive.npz')
arch['b']
np.savez_compressed('array_archive.npz',a=arr,b=arr)

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[6,23],[-1,7],[8,9]])

x.dot(y)
#x.dot(y)等价于np.dot(x,y)
np.dot(x,y)

import random
position = 0

walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
    
    plt.plot(walk[:100])
    
    nsteps = 1000
    draws = np.random.randint(0,2,size = nsteps)
    steps = np.where(draws >0,1,-1)
    walk = steps.cumsum()
    
   walk.min()
    walk.max()
    (np.abs(walk)>=10).argmax