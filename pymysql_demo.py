#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql.cursors

from datetime import datetime

# Connect to the database

connection = pymysql.connect(host='',
							 user='',
							 password='',
							 db='',
							 charset='utf8',
							 cursorclass=pymysql.cursors.DictCursor)

try:
	with connection.cursor() as cursor:
		# create new record
		sql = "insert into `leighj_python` (`add_time`) values (%s)"
		cursor.execute(sql, (datetime.now()))

		connection.commit()

	with connection.cursor() as cursor:
		sql = "select * from leighj_python"
		cursor.execute(sql)
		result = cursor.fetchall()
		for record in result:
			print(record)
except Exception as e:
	raise
finally:
	connection.close()