#coding=utf-8

'''
Created on 2016年10月27日
斐波那契数列
@author: Administrator
'''
a,b=0,1

r=[0]
for i in range(99):
    a,b=b,a+b
    r.append(a)
print r