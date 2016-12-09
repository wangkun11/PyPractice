#coding=utf-8
'''
Created on 2016年10月18日

@author: Administrator
'''

#计算平均数、中位数、众数
import random

list=[random.randint(0,10) for i in range(11)]
s=sum(list)
length=len(list)
average=s/length
print "The List is:",str(list)
print "The average is:",average

list.sort()
print "Sorted list is:",list
middle=list[length/2]
print "The milddle is:",middle

m={}
for i in list:
    if i in m:
        m[i]+=1
    else:
        m[i]=1
print m

max_number=max(m.values())
print max_number
for k,v in m.items():
    if v==max_number:
        print "The Mode is:",k
if __name__ == '__main__':
    print "hello world!"