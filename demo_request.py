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
header = {'User-Agent':'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25','Accept':'application/json, text/javascript, */*; q=0.01'}
r = requests.get(url, headers=header)

types =  json.loads(r.text).get('types')
cpCategorys =  json.loads(r.text).get('cpCategorys')
programCategorys =  json.loads(r.text).get('programCategorys')
types =  json.loads(r.text).get('types')
print(types,cpCategorys)