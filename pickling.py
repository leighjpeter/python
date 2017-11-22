#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 序列化 把变量从内存中变成可存储或传输的过程			python中称之为pickling
# 变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
import pickle
d = dict(name='Bob',age=20,score=80)
# pickle.dumps()方法把任意对象序列化成一个bytes
pickle.dumps(d)
# pickle.dump()方法把任意对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d,f) 
f.close()

# 反序列化
# pickle.loads()
# pickle.load()

# JSON
import json
d = dict(name='Bob',age=20,score=80)
json.dumps(d) # '{"name": "Bob", "age": 20, "score": 90}'
json.dump() 
json_str = '{"name": "Bob", "age": 20, "score": 90}'
json.loads(json_str)  #{'name': 'Bob', 'age': 20, 'score': 90}
json.load()

# class实例序列化为json对象
# 需要一个转换函数
# https://docs.python.org/3/library/json.html#json.dumps
import json

def student2dict(std):
	return {
		'name':std.name,
		'age':std.age
	}

class Student(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

s = Student('Bob', 20)
print(json.dumps(s,default=student2dict))

# 通常class的实例都有__dict__属性，除了定义了__slots__的class
print(json.dumps(s,default=lambda obj:obj.__dict__))

# 反序列化class实例
def dict2student(d):
	return Student(d['name'], d['age'])
json_str = '{"age": 20, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))