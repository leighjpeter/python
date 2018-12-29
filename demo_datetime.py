#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的
from datetime import datetime

i = datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)



# 创建时间
dt = datetime(2017,11,21,16,21)
print(dt) # 2017-11-21 16:21:00

# datetime转换为timestamp
dt.timestamp() # 1511281260.0
# timestamp转换为datetime
t = 1511281260.0
datetime.fromtimestamp(t)
datetime.utcfromtimestamp(t)
# str转换为datetime
datetime.strptime('2017-11-21 16:28:00','%Y-%m-%d %H:%M:%S')
# datetime转换为str
now = datetime.now()
now.strftime('%a, %b %d %H:%M')

# 使用timedelta加减datetime
now = datetime.now()
now + timedelta(hours=10)
now - timedelta(days=1)
now + timedelta(days=2, hours=12)

# 本地时间转换为UTC时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区

# 前提是系统时区恰好是UTC+8:00
# from datetime import datetime, timedelta, timezone
# tz_utc_8 = timezone(timedelta(hours=8))
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8)
# print(dt)

# 时区转换
# 通过utcnow拿到当前时间，再转换
from datetime import datetime,timezone,timedelta
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt) # 2017-11-30 09:12:04.608029+00:00
now = datetime.now()
print(now) # 2017-11-30 09:12:04.608646

# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt) # 2017-11-30 17:13:52.826238+08:00

print(bj_dt.strftime('%Y-%m-%d'))





# 格式化时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 2018-05-30 15:47:24

localtime = time.asctime( time.localtime(time.time()) )
print("本地时间为 :%s" %localtime)
# Wed May 30 15:49:08 2018