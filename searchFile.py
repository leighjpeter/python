#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
def searchFile(filename,filepath):

	if not os.path.isdir(filepath):
		filepath = '.'

	for d in os.listdir(filepath):
		if os.path.isdir(d):
			searchFile(filename,d)
		elif os.path.isfile(d):
			if os.path.split(d)[1].find(filename) != -1:
				print(os.path.abspath(d),os.path.split(d)[1])



filename = input('请输入查询文件名：')
filepath = input('请输入查询目录：')
searchFile(filename,filepath)