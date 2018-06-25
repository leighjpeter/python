#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取前百CEO地址的持币数量

import requests,re,os
import pymysql.cursors
import logging
from config_obj import MainConfig

url = 'https://ceo.bi/block?qt=CEOcoinBlockchain'

rootDir = os.path.split(os.path.realpath(__file__))[0]

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=rootDir+'/ceo_top.log',
                filemode='a')
data = []
def put_db():
	global data
	connection = pymysql.connect(host=MainConfig.get_config_values('mysql','DB_HOST'),user=MainConfig.get_config_values('mysql','DB_USER'),password=MainConfig.get_config_values('mysql','DB_PWD'),db=MainConfig.get_config_values('mysql','DB_DATABASE'),charset='utf8',cursorclass=pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			# create new record
			sql = "insert into `ceo_address_info` (`rank`,`address`,`hold_num`) values (%s,%s,%s)"
			cursor.executemany(sql, data )
			connection.commit()
	except Exception as e:
		logging.exception('Error')
		# logging.error('Error', exc_info=True)
	finally:
		logging.info('insert successfully')
		connection.close()

def get_info():
	global data
	r = requests.get(url)
	partten = re.compile(r'<td class="text-center">(.*)</td>',re.M)

	l = partten.findall(r.text)
	rank_l = l[::5]
	address_l = l[1::5]
	num_l = l[2::5]

	for x in range(0,len(rank_l)):
		data.append((int(rank_l[x]), str(address_l[x]), float(num_l[x])))

if __name__ == '__main__':
	get_info()
	put_db()