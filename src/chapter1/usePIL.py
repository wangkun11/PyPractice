#coding=utf-8
import Image
im = Image.open("../image/dog.jpg")
#1、生成灰度图：convert('L')表示将彩色Image转化为灰度Image
#imGray=im.convert('L')
#imGray.save("../image/dog_gray.jpg")
#2、创建缩略图：此方法会直接改变Image
#im.thumbnail((128,128))
#im.save('../image/dog_thumb.jpg')
#3、裁剪、旋转、粘贴
#box=(100,100,400,400)
#region=im.crop(box)
#region=region.transpose(Image.ROTATE_180)
#im.paste(region,box)
#im.save('../image/dog_transpose.jpg')