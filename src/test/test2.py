#coding=utf-8
'''
Created on 2016年10月27日
按照by_string 的顺序对words排序
@author: Administrator
'''
by_string=['a','e','i','o','u']
words=['suzhou','shanghai','hangzhou','nanjing','beijing']

result={}
for word in words:
    n=[]
    for i in word:
        if i in by_string:
            n.append(by_string.index(i))
        else:
            n.append(8)
    result[word]=n
print result

val=result.values()
val.sort()  #sort函数已经帮我们排好序
print val

sorted_word=[]
for i in val:
    for k,v in result.items():
        if v==i:
            sorted_word.append(k)
print sorted_word
