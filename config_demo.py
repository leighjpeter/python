#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import configparser

# config = configparser.ConfigParser()
# config.read(configFilePath)
# config.get(section=section, option=option)

# 项目路径
rootDir = os.path.split(os.path.realpath(__file__))[0]
# 配置文件路径
configFilePath = os.path.join(rootDir, '.env')

def get_config_values(section, option):
	"""
	根据传入的section获取对应的value
	:param section: ini配置文件中用[]标识的内容
	:return:
	"""
	config = configparser.ConfigParser()
	config.read(configFilePath)
	return config.get(section=section, option=option)

if __name__ == '__main__':
	result = get_config_values('mysql','DB_HOST')
	print(result)
