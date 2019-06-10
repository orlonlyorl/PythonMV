'''
向量a在向量b上的投影
'''
import numpy as np

def get_projection(a,b):
    c = (a.dot(b)/b.dot(b))*b*1.0
    return c

a = np.array([2,1])
b = np.array([1,1])

print(get_projection(a,b))