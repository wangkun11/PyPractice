#coding=utf-8
import Image
from pylab import *
#1、绘制图像、点、线==================================
#读取图像到数组中
# im=array(Image.open('../image/dog.jpg'))
# #用图像数组创建窗口
# imshow(im)
# #创建表示点坐标的列表
# x=[100,100,400,400]
# y=[200,500,200,500]
# #使用红色*标记绘制4个点
# plot(x,y,"r.")
# #绘制连接前两个点的直线
# plot(x[:2],y[:2],'ks:')
# #给窗口添加标题
# title('Plotting:dog.jpg')
# #不显示坐标轴
# axis('off')
# #显示窗口
# show()

#2、绘制轮廓图、直方图====================================================
im=array(Image.open('../image/dog.jpg').convert('L'))
#初始化一个窗口
figure()
#将此窗口设置为灰度
gray()
#对im中每一个点施加相同阈值，然后绘制轮廓
contour(im,origin='image')
axis('equal')
axis('off')
 
#初始化第二个窗口
figure()
#flatten：将任意数组按照行优先准则转换成一维数组，
#hist:绘制一维数组的直方图，表示图像中的像素分布情况
hist(im.flatten(),128)
show()
#3、交互式标注=====================================
# im=array(Image.open('../image/dog.jpg'))
# imshow(im)
# print 'Please select 3 points'
# x=ginput(3)
# print 'your clicked point is:',x
# show()

