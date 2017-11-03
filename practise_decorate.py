#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# 装饰器 参考http://python.jobbole.com/82344/


def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper


@log
def now():
	print('2017-10-30')

# now()  # now = log(now)


def logs(test):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (test, func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@logs('execute')
def nows():
	print('2017-10-30')
nows() # nows = logs('execute')(nows)



class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def grade(self):
        if self.score > 60:
        	self._grade = 'A'
        else:
        	self._grade = 'B'
        return self._grade
    
s = Student()

s.score = 60

print(s.score)
print(s.grade)

# 装饰器可以叠加使用
# 装饰器的调用顺序与使用 @ 语法糖声明的顺序相反
def deco_1(func):
	print('enter deco_1')
	def wrapper(a,b):
		print('enter deco_1 wrapper')
		func(a,b)
	return wrapper

def deco_2(func):
	print('enter deco_2')
	def wrapper(a,b):
		print('enter deco_2 wrapper')
		func(a,b)
	return wrapper

@deco_1
@deco_2
def addFunc(a,b):
	print('result %d' % (a+b))

addFunc(3,8)



class Screen(object):

	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise ValueError('width must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('width must between 0 ~ 100!')
		self._width = value
	
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, value):
		if isinstance(value,int) and value > 0:
			self._height = value
		else:
			print('height illegal!')

	@property
	def resolution(self):
		return self._height * self._width
	
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution