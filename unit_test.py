#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 单元测试
# 文档测试
# 
# 
# 
# 
class Dict(dict):
	'''
	Simple dict but also support access as x.y style.
	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2 = Dict(a=1, b=2, c='3')
	>>> d2.c
	'3'
	>>> d2['empty']
	Traceback (most recent call last):
	    ...
	KeyError: 'empty'
	>>> d2.empty
	Traceback (most recent call last):
	    ...
	AttributeError: 'Dict' object has no attribute 'empty'
	'''
	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no arrtibute '%s'"% key)

	def __setattr__(self, key, value):
		self[key] = value



import unittest
# 一个要测试的方法
from unit_name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""测试name_function.py"""
	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name,'Janis Joplin')


# 一个要测试的类

from unit_survey_class import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	""" 对AnonymousSurvey类的测试"""

	def setUp(self):
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English','Spanish','Mandarin']

	def test_store_single_respinse(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0],self.my_survey.responses)

	def test_store_three_response(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)
unittest.main()


