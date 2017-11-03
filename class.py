#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 在类中定义的函数，第一个参数必须是实例变量self
# __xxx private 
# _xxx 可被访问但是不要随意访问
# __xxx__ 特殊变量
class Student(object):
	def __init__(self, name, score): # __init__ 第一个参数必须是self，有了__init__ 创建实例的时候就不能传入空的参数了
		self.name = name
		self.score = score
	def print_score(self):
		print('%s:%s' %(self.name,self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


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

class Timer(object):
	def run(self):
		print('Start...')

t = Timer()
run_twice(t)

# 多重继承

# class Dog(Animal,Runnable):
# 	pass
		
# MixIn
# MixIn的目的就是给一个类增加多个功能,是的设计类的时候不是去设计复杂的继承关系
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass

# 定制类

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# 枚举类 不可变，成员可以直接比较。
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 使用元类
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
#要创建一个class对象，type()函数依次传入3个参数：

# 1 class的名称；
# 2 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3 class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
def fn(self,name='world'):
	print('Hello %s.' %name)

Hello = type('Hello',(object,),dict(hello=fn))