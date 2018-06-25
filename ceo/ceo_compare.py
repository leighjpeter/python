#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 每30min获取一次数据
# 写入txt
import requests
import re
import os
from retrying import retry

import pymysql.cursors
import logging
from datetime import datetime
from config_obj import MainConfig
rootDir = os.path.split(os.path.realpath(__file__))[0]

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=rootDir+'/ceo.log',
                filemode='a')

def put_db(data):
	connection = pymysql.connect(host=MainConfig.get_config_values('mysql','DB_HOST'),user=MainConfig.get_config_values('mysql','DB_USER'),password=MainConfig.get_config_values('mysql','DB_PWD'),db=MainConfig.get_config_values('mysql','DB_DATABASE'),charset='utf8',cursorclass=pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			# create new record
			sql = "insert into `coo_costs` (`add_time`,`transaction_volume`,`service_charge`,`cost_current`) values (%s,%s,%s,%s)"
			cursor.execute(sql, ( data['date'],data['transaction_volume'], data['service_charge'], float(data['cost_current']) ))
			connection.commit()
	except Exception as e:
		logging.exception('Error')
		# logging.error('Error', exc_info=True)
	finally:
		connection.close()

@retry(stop_max_attempt_number=20)
def recorg_log():
	url = 'https://ceo.bi/u/ranking.jsp'
	try:
		r = requests.get(url,timeout=60);
		money_pattern = re.compile(r'<p class="money">\¥(\d*\.\d*)</p>')
		time_pattern = re.compile(r'<p class="time">(.*)</p>')

		price = money_pattern.findall(r.text)
		t = time_pattern.search(r.text).group(1)

		data = {'date':t ,'transaction_volume':price[0],'service_charge':price[1] ,'cost_current':price[2]}
		# 写文件
		# with open('/Users/jessica/Dev/python/selenium/ceo_transaction_logs.txt','a+') as f:
		# 	f.write(str(data)+'\n')
		# 写mysql
		put_db(data)
		return
	except Exception as e:
		logging.error('Error', exc_info=True)


if __name__ == '__main__':
	i = datetime.now();
	if i.hour < 13 or i.hour > 18:
		recorg_log()



