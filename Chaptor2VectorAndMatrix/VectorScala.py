'''
功能：向量与实数的乘法
'''
import numpy as np

#建立向量
a = np.array([3,2,4,5])
t1 = a.reshape((len(a),1))
print(t1)
print(t1.shape)

scala = input("请输入实数：")
print(scala)

#向量与实数相乘
x = np.multiply(int(scala),t1)
print(x)

for i in range(np.size(t1,0)):
    for j in range(np.size(t1,1)):
        x1 = int(scala) * t1[i][j]
        print(x1)
