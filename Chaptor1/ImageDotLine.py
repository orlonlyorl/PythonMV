'''
书：Python计算机视觉编程
第一章：基本的图像操作和处理
1.2.1：绘制图像、点和线
时间：2019年6月7日
作者：吴雅林
'''
from PIL import Image
from pylab import *

#读取图像到数组中
im=array(Image.open('C:/Users/Administrator/PycharmProjects/PythonMV/Chaptor1/empire.jpg'))

#绘制图像
imshow(im)

#一些点
x = [100,100,400,400]
y = [200,500,200,500]

#使用红色星型标志绘制点
plot(x,y,'r*')

#链接前两个点的线
plot(x[:4],y[:4])

#添加标题显示绘制图像
title('Plotting:"empire.jpg"')
axis('off')
show()