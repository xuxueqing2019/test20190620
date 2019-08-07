# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:33:16 2019

@author: 徐雪晴
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


iris = datasets.load_iris()
X = iris.data
y = iris.target
X = X[y<2, :2]
y = y[y<2]

from playML.train_test_split import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, seed=666)


from playML.LogisticRegression import LogisticRegression

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

log_reg.score(X_test, y_test)
# 输出：1.0

# 查看测试数据集的样本发生的概率
log_reg.predict_proda(X_test)
# 输出：array([0.92972035, 0.98664939, 0.14852024, 0.17601199, 0.0369836 ,
      # 0.0186637 , 0.04936918, 0.99669244, 0.97993941, 0.74524655,
      # 0.04473194, 0.00339285, 0.26131273, 0.0369836 , 0.84192923,
      # 0.79892262, 0.82890209, 0.32358166, 0.06535323, 0.20735334])