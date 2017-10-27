#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 切片
L = [1,2,3,4,5,6,7,78,9,9,9,9,0];
print(L)
L[:10] #前10
L[-10:] #后10
L[10:20] #前11-20
L[:10:2] #前10个，每2个取1个
L[::5] #每5个取1个
L[:] #复制一个list


T = (0,1,2,3,4,5,6,7)

T[:3]

# 字符串也可以使用切片
'abcdfrgfsdsa'[:3] # abc  Python没有针对字符串的截取函数，只需要切片

# 迭代
# 迭代对象 list tuple dict 字符串

l = [1,2,3,4,5,6,7,8,9]

for x in l:
	print(x)
#enumerate 函数可以把一个list变成索引-元素对
for x,v in enumerate(l):
	print(x,v)

t = (0,1,2,3,4,5,6,7)

for x in t:
	print(x)

d = {'a':1,'b':2,'c':3}
for x in d:
	print(x)

for x in d.values():
	print(x)

for x in d.items():
	print(x)

for k ,v in d.items():
	print(k,v)

for x in [(1,2),(3,4),(5,)]:
	print(x)

for x,y in [(1,2),(3,4),(5,6)]:
	print(x,y)


# 列表生成器
[m+n for m in 'ABC' for n in 'XYZ']

# os.listdir

d = {'a':1,'b':2,'c':3}
[k+'='+str(v) for k,v in d.items()]

L = ['Hello', 'World', 18, 'Apple', None]
[s.lower() if isinstance(s,str) else s for s in L ]