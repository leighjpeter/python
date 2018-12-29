#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fire

class Calculator(object):
	"""A simple calculator class."""
	def add(self, num2, num1):
		return num2 + num1
	def multiply(self, num1, num2):
		return num1 * num2

if __name__ == '__main__':
	fire.Fire(Calculator)
