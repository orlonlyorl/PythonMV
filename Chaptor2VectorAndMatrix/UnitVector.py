'''
功能：单位矩阵
'''

import numpy as np

#定义矩阵
a = np.array([3,2,4,5])
t1 =  a.reshape((len(a),1))
print(t1.shape)
print(t1)

#求t1的范数
x1 = np.linalg.norm(t1)

#求单位矩阵
u = t1/x1
print(u)

#求单位矩阵的范数
nu = np.linalg.norm(u)
print(nu)