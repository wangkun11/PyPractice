#encoding=utf-8
import Image
from numpy import *
from pylab import *
#1、图像的数组表示及常见用法=================================
# im =array(Image.open('../image/dog.jpg').convert('L'))
# print im.shape,im.dtype
# im[:,1] = 100                # 将第 i 列的所有数值设为100
# print im[:100,:50].sum()     # 计算前100 行、前 50 列所有数值的和
# print im[50:55,50:55]        # 50~100 行，50~100 列（不包括第 100 行和第 100 列）
# print im[1].mean()           # 第 i 行所有数值的平均值
# print im[:,-1]               # 最后一列
# print im[-2,:]               # 倒数第二行
# print im[-2]                 # 倒数第二行
#2、灰度变换========================================
im = array(Image.open('../image/dog.jpg').convert('L'))
#array的好处：直接对整个数组进行四则运算以及乘方开方运算
im2 = 255 - im # 对图像进行反相处理
im3 = (100.0/255) * im + 100 # 将图像像素值变换到100...200 区间
im4 = 255.0 * (im/255.0)**2 # 对图像像素值求平方后得到的图像
figure()
imshow(im)
figure()
imshow(im2)
figure()
imshow(im3)
figure()
imshow(im4)
show()