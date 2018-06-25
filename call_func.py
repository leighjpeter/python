#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 内置函数
# https://docs.python.org/3/library/functions.html#abs
# 位置参数


x = int(input('数字:'))
def power(x,n=2):
	s = 1
	while n > 0:
		n = n-1
		s = s * x
	return s;
a = power(x)
print(a)

# 定义默认参数，必须指向不变对象
#
def add_end(l=[]):
	l.append('end')
	return l

add_end() #[end]
add_end() #[end,end]


def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

calc([1,2]) # 5

# 可变参数
def calc(*numbers): # 参数numbers接收到的是一个tuple
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

calc() # 0
calc(1,2) # 5

# *nums 表示把nums这个list的所有元素作为可变参数传进去
nums = [1,2,3]
calc(*nums) # 14
nums=(1,2,3)
calc(*nums) # 14
#

# 关键字参数
def person(name,age,**kw):
	print('name:', name, 'age:', age, 'other:',kw)

extra = {'city':'hz','job':'engineer'}
person('leighj','26',city=extra['city']) ## name: leighj age: 26 other: {'city': 'hz'}
person('leighj','26',**extra) # name: leighj age: 26 other: {'city': 'hz', 'job': 'engineer'}

# 命名关键字参数      限制关键字参数的名字 只接受  city job
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name,age,*,city,job):
	print(name,age,city,job)

# 如果函数定义中已经有一个可变参数，后面跟着的命名关键字参数就不需要一个特殊分隔符了
def person(name,age,*args,city,job):
	print(name,age,args,city,job)

person('Jack', 24, city='hangzhou', job='Engineer') # Jack 24 () hangzhou Engineer

# 命名关键字参数可以有缺省值，命名关键字参数必须传入参数名
def person(name,age,*args,city='hangzhou',job):
	print(name,age,args,city,job)

person('Jack', 24, job='Engineer') # Jack 24 () hangzhou Engineer


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a,b,c=0,*,d,**kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)



f1(1, 2) # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, 3, 'a', 'b') # a = 1 b = 2 c = 0 args = ('a','b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99) # a = 1 b = 2 c = 0 args= ('a','b') kw = {'x':99}
f1(1, 2, d=99, ext=None) # a = 1 b = 2 c = 0 args = () kw = {'d': 99, 'ext': None}
f2(1, 2, d=99, ext=None) # a = 1 b = 2 c = 0 d=99 kw={'ext':None}

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args,**kw) # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1,2,3)
f2(*args,**kw) # a = 1 b = 2 c = 3 d = 99 kw = {'x': '#'}


# 小结：
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它

# 可变参数既可直接传入func(1,2,3) 又可先组装list或tuple 再通过*args传入 func(*(1,2,3))
# 关键字参数既可直接传入 func(a=1,b=2) 又可先组装dist再通过**kw传入 func(**{'a':1,'b':2})


# 递归函数
# 使用递归函数需要注意防止栈溢出
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的
# 尾递归是指在函数返回的时候调用函数本身，并且return语句不能包含表达式
# python解释器没有针对尾递归做优化，so任何递归函数都存在栈溢出的问题
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

# fact(1000) RecursionError: maximum recursion depth exceeded in comparison 导致栈溢出




def fact(n):
    return fact_iter(n, 1)

def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num-1,num*product)




def move(n,a,b,c):
	if n == 1:
		print('move',a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
move(2,'A','B','C')