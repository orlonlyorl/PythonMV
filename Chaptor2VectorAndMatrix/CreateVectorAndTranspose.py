'''
功能：向量的建立与转置
'''
import numpy as np

#建立向量
a = np.array([3,2,5,4])
print(a)
print(a.shape)

print('**向量的重置**')
t1 = a.reshape((1,len(a)))
t2 = t1.T
print(t1)
print(t1.shape)
print(t2)
print(t2.shape)
print('**向量的重置**')

#计算向量的范数（norm）
x = np.linalg.norm(a)
print(x)

x1 = 0
for index in range(len(a)):
    x1 = x1+a[index]*a[index]

x2 = np.sqrt(x1)
print(x2)