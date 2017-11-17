#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# 
# 编写测试类 从unittest继承
# 以test开头的func 就是测试方法，不以test开头的func 测试的时候不会被执行
# 断言 
# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
# doctest非常有用，不但可以用来测试，还可以直接作为示例代码
import unittest

from unit_test import Dict

class TestDict(unittest.TestCase):
	
	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key,'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	def setUp(self):
		print('setUp')

	def tearDown(self):
		print('tearDown')

# 运行测试单元
# 方法一
# if __name__ == '__main__':
# 	unittest.main()

# 方法二 (推荐)
# python -m unittest mydict_test.py

if __name__ == '__main__':
	import doctest
	doctest.testmod()