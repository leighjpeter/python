#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#生成器  一边循环一边计算的机制generator
g=( x*x for x in range(10) )

def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n=n+1
	return 'done'

# 函数改为generator后 基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
# 但是for循环拿不到return，如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
for x in fib(6):
	print(x)

g = fib(6)
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break

# 如果函数定义中有yield关键字 就是一个 生成器 generator
# 判断是否是特殊的函数     通过 inspect 模块的 isgeneratorfunction 
from inspect import isgeneratorfunction 
isgeneratorfunction(fib)  #True

# 杨辉三角
def triangles():
	l=[1]
	while True:
		yield l
		l.append(0)
		l = [l[i-1] + l[i] for i in range(len(l))]
n=0
a = input("请输入杨辉三角的行数：")
for t in triangles():
    print(t)
    n = n+1
    if n == int(a):
        break


# 迭代器 Iterator

# 可用for循环的对象 统称为可迭代的对象 Iterable （list、tuple、dict、set、str、generator、生成器、generator function等）
# 判断是否是可迭代的对象 通过collections模块的 Iterable 类型判断
from collections import Iterable
isinstance('abc',Iterable) # true

# 迭代器 不仅可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了

from collections import Iterator
isinstance((x for x in range(10)), Iterator) # true
isinstance([], Iterator) # false
isinstance({}, Iterator) # false
isinstance('abc', Iterator) # false

# 生成器都是Iterator,但是 str dict list 是Iterable 却不是 Iterator 不过可以通过iter()函数获得一个Iterator对象。
isinstance(iter('abc'), Iterator) # true