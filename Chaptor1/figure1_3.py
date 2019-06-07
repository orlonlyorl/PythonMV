'''
题目：用Matplotlib绘制图像等轮廓线和直方图
时间：2019年6月7日
'''
from PIL import Image
from pylab import *

# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

# 打开图像，并转成灰度图像
im = array(Image.open('C:/Users/Administrator/PycharmProjects/PythonMV/Chaptor1/empire.jpg').convert('L'))

figure()
subplot(121)
gray()
contour(im, origin='image')
axis('square')#横纵坐标范围相同
axis('off')
title(u'图像轮廓', fontproperties=font)

subplot(122)
hist(im.flatten(),128)
title(u'图像直方图', fontproperties=font)
plt.xlim([0,260])
#plt.ylim([0,100])


show()