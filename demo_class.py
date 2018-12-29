#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mobile(mobile,**detailed):
	# print('mobile:',mobile,'detailed:',detailed)
	print('mobile:{},detailed:{}'.format(mobile,detailed))

# mobile('iphone8',price=800,cpu=4)

# @property类的内置装饰器
class Student:
	"""docstring for Student"""
	def __init__(self, name, score):
		super(Student, self).__init__()
		self.name = name
		self._score = score

	@property
	def score(self):
		# get function
		return self._score
	
	@score.setter
	def score(self, value):
		# set function
		self._score = value

s = Student('stan',10)
print(s._score)
s.score = 30
print(s.score)

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

# ABC 模块 完成抽象基类的功能
from abc import ABC,abstractmethod
# Bird 继承ABC也就是说Bird是一个抽象类
# 这个类的目的就是让继承它的子类一定要实例化fly函数，否则子类也永远无法实例化
class Bird(ABC):
	@abstractmethod
	def fly(self):
		pass



