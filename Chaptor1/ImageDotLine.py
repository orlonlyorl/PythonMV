'''
书：Python计算机视觉编程
第一章：基本的图像操作和处理
1.2.1：绘制图像、点和线
时间：2019年6月7日
作者：吴雅林
'''
from PIL import Image
from pylab import *
import PCV

#读取图像到数组中
im=array(Image.open('C:/Users/Administrator/PycharmProjects/PythonMV/Chaptor1/empire.jpg'))

figure()

# 画有坐标轴的
subplot(121)
imshow(im)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y, 'r*')
plot(x[:2], y[:2])
title('plotting: "empire.jpg"')

# 不显示坐标轴
subplot(122)
imshow(im)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y, 'r*')
plot(x[:4], y[:4])
axis('off')  #显示坐标轴
title('plotting: "empire.jpg"')
show()