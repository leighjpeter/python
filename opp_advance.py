#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type() 判断对象类型

# 判断一个对象是否是函数可以使用types模块中定义的常量

import types
def fn():
	pass

type(fn) == types.FunctionType 
type(abs) == types.BuiltinFunctionType
type(lambda x:x) == types.LambdaType
type(x for x in range(10)) == types.GeneratorType


# isinstance()
# 能用type()判断的基本类型也可以用isinstance()判断
isinstance(d,Dog)

# 还可以判断一个变量是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple)) # True
isinstance((1, 2, 3), (list, tuple)) # True

# dir() 获得一个对象的所有方法和属性

# getattr()、setattr()、hasattr()

# 实例属性 类属性

# 
# __slots__ 
# __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
# 仅对当前类实例起作用

# __str__() 
# __repr__()
# __iter__()
# __getitem__()
# __setitem__()
# __delitem__()
# __getattr__()
# __call__()
# 



# 给实例绑定方法
class Student(object):
	pass

def set_age(self, age):
	self.age = age

s = Student()

from types import MethodType
s.set_age = MethodType(set_age,s)

s.set_age(25)

s.age  # 25

# 给class绑定方法
def set_score(self, score):
	self.score = score

Student.set_score = set_score

s.set_score(100)

s.score






