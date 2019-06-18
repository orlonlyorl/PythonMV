'''
功能：计算向量的范数
'''
import numpy as np

#建立向量
a = np.array([3,2,5,4])
print(a)
print(a.shape)

#计算向量的范数（norm）
x = np.linalg.norm(a)
print(x)

x1 = 0
for index in range(len(a)):
    x1 = x1+a[index]*a[index]

x2 = np.sqrt(x1)
print(x2)