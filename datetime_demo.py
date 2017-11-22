#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# 创建时间
dt = datetime(2017,11,21,16,21)
print(dt) # 2017-11-21 16:21:00

# datetime转换为timestamp
dt.timestamp() # 1511281260.0
# timestamp转换为datetime
t = 1511281260.0
datetime.fromtimestamp(t)
# str转换为datetime
datetime.strptime('2017-11-21 16:28:00','%Y-%m-%d %H:%M:%S')
# datetime转换为str
now = datetime.now()
now.strftime('%a, %b %d %H:%M')



# 本地时间转换为UTC时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区

from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)