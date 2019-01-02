#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list []有序集合 随时添加删除其中的元素

classmate = [1,2,3]
del classmate[0]
classmate.append('d') # ['a','b','c','d']
classmate.insert(2,'f') # ['a','b','c','d','f']
classmate.pop() #删除末尾 # classmate.pop(i) 删除指定位置
# classmate.extend(L)
# classmate.remove(x) # remove方法只删除第一个指定的值，如果有
# classmate.reverse() # 反转列表(可再次reverse恢复)
# del classmate
# classmate.count(x)
# classmate.sort() # 永久性排序(不可恢复)
# classmate.sort(reverse=True)
# sorted(classmate) # 临时性排序
# len(classmate)



# tuple () 不可修改
# 可以用 + 连接两个元组
# ===========常见操作=============== #
# tup.index(x, [start, [stop]])) 返回元组中start到stop索引中第一个值为 x 的元素在整个列表中的索引。如果没有匹配的元素就会返回一个错误。
# tup.count(x) 返回 x 在元组中出现的次数。
# cmp(tuple1, tuple2) 比较元组中两个元素。
# len(tuple) 计算元组元素个数。
# max(tuple) 返回元组中元素最大值。
# min(tuple) 返回元组中元素最小值。
# tuple(seq) 将列表转换为元组。
# ===========常见操作=============== #
t1=(1,2,3)
t2=('a','b')
t3 = t1+t2 # (1,2,3,'a','b')

class_t = ('a','b','c')
class_t = (1,)
# 但是 tuple 包含list 可以修改list
class_t = ('a','b','c',['A','B'])
class_t[3][0] = 'C';
print(class_t) # ('a', 'b', 'c', ['C', 'B'])

del t1


# dict {}key-value
# value可覆盖，但是不能没有key
# key必须是不可变对象
#dict内部存放的顺序和key放入的顺序是没有关系的
#dict查找和插入的速度极快，不会随着key的增加而增加，但是需要占用大量的内存，内存浪费多

# ===========常见操作=============== #
# D.clear() 删除字典内所有元素
# D.copy() 返回一个字典的复制
# dict.fromkeys(iterable[,value=None])创建一个新字典，以iterable中元素做字典的键，value为字典所有键对应的初始值
# D.has_key(key) 如果键在字典dict里返回true，否则返回false
# D.items() 以列表返回可遍历的(键, 值) 元组数组
# D.keys() 以列表返回一个字典所有的键
# D.values() 以列表返回字典中的所有值
# D.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# D.update(dict2) 把字典dict2的键/值对更新到dict里
# D.pop(key) 删除一个键并返回它的值，类似于列表的pop,只不过删除的是一个键不是一个可选的位置
# del D[key] 删除键
# D[key] = 42 新增或修改键
# OrderedDict模块可以记录添加的顺序，兼具列表和字典的优点
# ===========常见操作=============== #

d = {'mike':99,'bob':80}
# 判断key是否存在
print('mike' in d)
print(d.get('bob'))
# D.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
print(d.get('bo',0))

d[(1,)] = 2121 # special tuple 可作为dist的key
# dict.fromkeys(iterable[,value=None])创建一个新字典，以iterable中元素做字典的键，value为字典所有键对应的初始值
iterable1 = '12'
iterable2 = [1,2]
iterable3 = (1,2)
iterable4 = {1:'one',2:'two'}
v1 = dict.fromkeys(iterable1,'字符串') # {'1': '字符串', '2': '字符串'}
v2 = dict.fromkeys(iterable2,'列表') # {'1': '列表', '2': '列表'}
v3 = dict.fromkeys(iterable3,'元祖') # {'1': '元祖', '2': '元祖'}
v4 = dict.fromkeys(iterable4,'列表') # {'1': None, '2': None}

# set 没有重复的key，重复元素自动过滤
# 需要提供一个list
# add
# remove
# update
# 交集& 并集| 差集-
s = set([1,2,3])
print(s)
s.add(4)
print(s)
s.remove(2)
print(s)
s.add(('a','b',('c','d')))
print(s)
s.update([8,9])
print(s)



print(tuple(classmate)) # list 转 tuple
list(class_t) # tuple 转 list


# lambda 表达式
# Explicit is better than implicit
# 主要应用在函数式编程和闭包中

list1 = [3,5,-4,-1,0,-2,-6]
sorted(list1, key=lambda x: abs(x))

def get_y(a,b):
	return lambda x:a*x+b
y = get_y(1,1)

## 等价于
def	get_y_l(a,b):
	def func(x):
		return a*x+b
	return func
y = get_y_l(1,1)
y(1) # 2
