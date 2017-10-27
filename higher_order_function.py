#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map/reduce

# map(fucntion,Iterable) 接受一个函数和一个序列，把结果作为新的Iterator返回
# reduce(function(x,y),[x1, x2, x3, ...]) reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def char2num(s):
	return	{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

from functools import reduce
def add(x,y):
	return x+y

reduce(add,[1,3,5,7,9]) #25

def fn(x,y):
	return x * 10 + y

reduce(fn,map(char2num,'13579') # 13579

# case 1
def normalize(name):
    return name[0].upper()+name[1:].lower()

list(map(normalize,['adam', 'LISA', 'barT']))

# case 2 利用reduce给list求积
from functools import reduce
def prod(L):
	return reduce(lambda x,y:x*y,L)
print('1*3*5 =',prod([1,3,5]))

# case 3 字符串'123.456'转换成浮点数123.456：
from functools import reduce

def str2float(s):
	def char2num(s):
		return	{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	i=s.index('.')
	a=s[:i] # 123
	b=s[i+1:] # 456
	return ( reduce(lambda x,y: x * 10 + y,list(map(char2num,a)) ) * pow(10,len(b)) + reduce(lambda x,y: x * 10 + y,map(char2num,b)) ) / pow(10,len(b))

print('str2float(\'123.00\') =', str2float('123.00')) # 123.0
print('str2float(\'123.34566\') =', str2float('123.34566')) # 123.34566



# filter()函数 用于过滤序列 ，接受函数和序列 ，传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def not_empty(s):
	return s and s.strip()

list(filter(not_empty,['','Avc','123']))


# 用filter筛选素数

# 创建一个生成器,并且是一个无限序列
def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n

# 创建一个筛选器
def _not_divisible(n):
	return lambda x : x % n > 0

# 定义一个生成器，不断返回下一个素数：
def primes():
	yield 2 
	it = _odd_iter() # 初始序列
	while True:
		n = next(it) # 返回序列的第一个数
		yield n
		it = filter(_not_divisible(n),it)	# 构造新序列

# primes() 是一个无限序列，所以调用的时候需要一个退出循环的条件
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
            
if __name__ == '__main__':
    main()


# 是否是回文数
def is_palindrome(n):
	a = str(n)
	b = str(n)[::-1]
	if a == b:
		return True
	else:
		return False


def is_palindrome(n):
    new = list(str(n))
    new.reverse()
    return n == int(''.join(new))   # ''.join(new)  list2str
    
output = filter(is_palindrome, range(1, 1000))
print(list(output))



# sorted 高阶函数  sorted(序列, key='', reverse=True)
# 
# sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

L = [('Bob', 75), ('Adam', 92), ('bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0]

L2 = sorted(L, key=by_name, reverse=True)

print(L2)


# 闭包
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1, f2, f3 = count()

f1() # 9
f2() # 9
f3() # 9
# 返回的函数f()引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()

f1() # 1
f2() # 4
f3() # 9

# 匿名函数
# lambda 表达式就是一个匿名函数

# 函数对象有一个__name__属性
 now.__name__
# 装饰器
# 偏函数
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
import functools
int2 = functools.partial(int, base=2)