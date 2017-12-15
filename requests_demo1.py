#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 强大的Requests
import requests
import re
import json
import sys
import time
# 卡思数据
url = 'http://www.caasdata.com/mobile/rank/info.html'

# header = {'User-Agent':'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25','Accept':'application/json, text/javascript, */*; q=0.01'}

# r = requests.get(url, headers=header)

# types =  json.loads(r.text).get('types')
# cpCategorys =  json.loads(r.text).get('cpCategorys')
# programCategorys =  json.loads(r.text).get('programCategorys')
# types =  json.loads(r.text).get('types')
# print(types,cpCategorys)

# papi
papi_id = '5726188736'
nowTime = lambda:int(round(time.time() * 1000))
t = str(nowTime())
pre_url = 'https://www.toutiao.com/api/article/user_log/?c=user_page&sid=gbry4ppek'+t+'&type=pageview&t='+ t
# pre_r = requests.get(pre_url)
# print(pre_r.headers['Set-Cookie'])

# as cp _signature 是js加密出来的
url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id='+papi_id+'&max_behot_time=0&count=20&as=A1350AE3119F702&cp=5A31AFB7F0C23E1&_signature=3fL8GhAVh8sTmXrIa-lj593y.A'
header = {
	'Accept':'application/json, text/javascript',
	# 'Accept-Encoding':'gzip, deflate, br',
	# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
	# 'Cache-Control':'no-cache',
	# 'Connection':'keep-alive',
	# 'Content-Type':'application/x-www-form-urlencoded',
	# 'Cookie':'tt_webid=6499218776868881933; uuid="w:0d3960f5c3534f899e0f5908a5086916"; UM_distinctid=16052c7daf971a-0c615189efdcab-b7a103e-1fa400-16052c7dafa44c; __tasessionId=wsv7widww1513222956706; CNZZDATA1259612802=176969928-1513212352-%7C1513217752',
	# 'Host':'www.toutiao.com',
	# 'Pragma':'no-cache',
	'Referer':'https://www.toutiao.com/c/user/'+papi_id+'/',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest',
}
r = requests.get(url, headers=header)
print(r.json().get('data'))
sys.exit()
