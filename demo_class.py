#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 在类中定义的函数，第一个参数必须是实例变量self
# __xxx private
# _xxx 可被访问但是不要随意访问
# __xxx__ 特殊变量
# 实力属性会覆盖类属性，所以千万不要对实例属性和类属性使用相同的名字
class Teacher(object):
	def __init__(self, name, score): # __init__ 第一个参数必须是self，有了__init__ 创建实例的时候就不能传入空的参数了
		self.__name = name
		self.__score = score
		self.x = name

	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

	def print_score(self):
		print('%s:%s' %(self.__name,self.__score))


bart = Teacher('Bart Simpson', 59)
lisa = Teacher('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

print(bart._Teacher__name) # special

# 获得一个对象的所有属性和方法
print(dir(bart))
# 优先使用isinstance判断类型
print(isinstance(bart,Teacher))
# getattr() setattr() hasattr()

print(hasattr(bart,'x')) # True


# @property类的内置装饰器
# 不需要set_score/get_score
# 既可以保证对参数进行必要的检查，又可以类似属性方式访问类的变量
# 还可以只定义只读属性
class Student:
	"""docstring for Student"""
	def __init__(self, name, score):
		# super(Student, self).__init__()
		self._name = name
		self._score = score

	@property
	def score(self):
		# get function
		return self._score
	
	@score.setter
	def score(self, value):
		# set function
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 and 100')
		self._score = value

	# 只读属性
	@property
	def	name(self):
		return self._name

s = Student('stan',10)
s.score = 30
print(s.score)

# __slots__ 限制添加实力的属性

class Baby(object):
	__slots__ = ('name','gender')


# @classmethod 类方法
# @staticmethod 静态方法
class Date():
	"""docstring for Date"""
	def __init__(self, year, month, day):
		# super(Date, self).__init__()
		self.year = year
		self.month = month
		self.day = day

	@staticmethod
	def format_date(str_date):
		y,m,d = str_date.split("-")
		return Date(int(y),int(m),int(d))

	@classmethod
	def format_date2(cls,str_date):
		y,m,d = str_date.split("-")
		return cls(int(y),int(m),int(d))

	def yesterday(self):
		self.day -= 1

	def __str__(self):
		return '{}/{}/{}'.format(self.year,self.month,self.day)


d = Date(2018,10,9)
d.yesterday()
print(d)

d2 = Date.format_date('2018-10-09')
d2.yesterday()
print(d2)


d3 = Date.format_date2('2018-10-09')
d3.yesterday()
print(d3)

# 继承
# "鸭子类型" 不需要严格的继承
# 开闭原则：对扩展开放，对修改封闭
#
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

run_twice(c)

# 多重继承

# class Dog(Animal,Runnable):
# 	pass

# MixIn
# MixIn的目的就是给一个类增加多个功能,使得设计类的时候不是去设计复杂的继承关系
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass

# 定制类
# __str__
# __iter__
# __getitem__
# __getattr__

class Chain(object):
	def __init__(self, path=''):
		self.name = 'Michael'
		self._path = path

	def __str__(self):
		return self._path

	def users(self, user):
		return Chain('%s/%s' % (self._path, user))

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	__repr__ = __str__

d = Chain()
print(Chain().status.users('leighj').timeline.list)

# 枚举类 不可变，成员可以直接比较。
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 使用元类
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# 要创建一个class对象，type()函数依次传入3个参数：

# 1 class的名称；
# 2 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3 class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
def fn(self,name='world'):
	print('Hello %s.' %name)

Hello = type('Hello',(object,),dict(hello=fn))


# ABC 模块 完成抽象基类的功能
from abc import ABC,abstractmethod
# Bird 继承ABC也就是说Bird是一个抽象类
# 这个类的目的就是让继承它的子类一定要实例化fly函数，否则子类也永远无法实例化
class Bird(ABC):
	@abstractmethod
	def fly(self):
		pass



