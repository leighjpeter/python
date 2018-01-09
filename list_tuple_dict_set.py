#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# list []有序集合 随时添加删除其中的元素
classmate = ['a','b','c']
print(classmate)
len(classmate) # 3
classmate.append('d') # ['a','b','c','d']
print(len(classmate)) # 4
classmate.insert(8,'f')
print(len(classmate)) # 5
classmate.pop() #删除末尾 # classmate.pop(i) 删除指定位置
print(len(classmate))

# tuple () 不可修改
class_t = ('a','b','c')
class_t = (1,)
# 但是 tuple 包含list 可以修改list
class_t = ('a','b','c',['A','B'])
class_t[3][0] = 'C';
print(class_t) # ('a', 'b', 'c', ['C', 'B'])

# dict {}key-value
# value可覆盖，但是不能没有key
# key必须是不可变对象
d = {'mike':99,'bob':80}
print(d['mike'])
# 判断key是否存在
print('mike' in d)
print(d.get('bob'))

d['bo'] = class_t
print(d.get('bo',0))
d[(1,)] = 2121 # special tuple 可作为dist的key
print(d) # {'mike': 99, 'bob': 80, 'bo': ('a', 'b', 'c', ['C', 'B']), (1,): 2121}
print(d.pop('bob'))
print(d)

# set 没有重复的key，重复元素自动过滤
# 需要提供一个list
# add
# remove
# 交集& 并集|
s = set([1,2,3])
print(s)
s.add(4)
print(s)
s.remove(2)
print(s)
s.add(('a','b',('c','d')))
print(s)