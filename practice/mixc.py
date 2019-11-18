#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import sys
import requests
import re
import logging
import hashlib

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/Users/jessica/Dev/python/practice/mixc.log',
                filemode='a')

MIXC_USERNAME = os.getenv('MIXC_DAILY_USERNAME') or '18072736217' # username or email
MIXC_PASSWORD = os.getenv('MIXC_DAILY_PASSWORD') or 'wxh123456' # password

class MIXCDailyException(Exception):
    def __init__(self, req):
        self.req = req

    def __str__(self):
        return str(self.req)

class MIXCDaily(object):
    BASE_URL = 'https://app.mixcapp.com/mixc' 
    LOGIN_URL = BASE_URL + '/api/v1/login'
    SIGN_URL = 
    # CHECKIN_URL = BASE_URL + '/user/checkin/jsonp_checkin'

    def __init__(self, username, password):
        self.userName = username
        self.password = password
        self.appVersion = '3.3.0'
        self.deviceParams = 'eyJwaG9uZSI6IjE4MDcyNzM2MjE3IiwibG9jYXRpb24iOnsiZ3BzTG9uZ2l0dWRlIjoiMTIwLjI5MzciLCJncHNMYXRpdHVkZSI6IjMwLjE2MDgifSwiZGV2aWNlSWQiOiIyMDE4MTAwNzIxMzAzNWMwNzU5MzM3ODQwZTcxMjY0YTY3NWFiYWFmYjZiNTIwMDEzOWJhNDA5MTdmZWIxYyJ9'
        self.imei = 'D01E1319-6934-45DC-BF84-F407B5585445'
        self.mallNo = '330100A001'
        self.osVersion = 12.2
        self.platform = 'iOS'
        self.sign = '14e35db5c6ad12363020357ff0433cb7'
        self.timestamp = 1560048539584
        self.session = requests.Session()
        self.session.keep_alive = False

    def login(self):
        headers = {
            'User-Agent': 'mixc/3.3.0 (iPhone; iOS 12.2; Scale/3.00)',
            'Host': 'app.mixcapp.com',
            'Connection':'keep-alive',
            'Cookie':'smidV2=2019060414130447624ae87b3ae4396b59e08c22e7ef830069ba244c6dc5040; _fmdata=X38QXtd7aaRje5vxbx2tKRmqx48BHQQLpc9UA4rtSMYU8aNcsytICgjUxobi74aZhz9F4RJgt8OQvFsXURAJ82rn9PLFBVK1geoMzk%2BJDG8%3D; acw_tc=7819730415592704813976880e0c12195204df38a86790d6adfd769adb582c'
        }

        params = {
            'username': self.userName,
            'password': self.password,
        }

        # r = self.session.get(self.BASE_URL, headers=headers, verify=True)
        r = self.session.post(self.LOGIN_URL, headers=headers, verify=True)
        # r = self.session.post(self.CHECKIN_URL, headers=headers, verify=True)
        if r.status_code != 200:
            raise MIXCDailyException(r)

        data = r.text
        jdata = json.loads(data)
        return jdata

if __name__ == '__main__':
    # if SMZDM_USERNAME is '' or SMZDM_PASSWORD is '':
    #     print('SMZDM_USERNAME and SMZDM_PASSWORD required')
    #     sys.exit()
    try:
        smzdm = MIXCDaily(MIXC_USERNAME, MIXC_PASSWORD)
        result = smzdm.login()
    except MIXCDailyException as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    else:
        # if result['error_code'] == 0 :
        #     str = '成功连续签到'+str(result['data']['checkin_num'])+'天，积分'+str(result['data']['point'])+'金币'+str(result['data']['gold'])+'等级'+str(result['data']['rank'])
        # else:
        #     str = '失败：'+result['error_msg']
        # logging.info(str)
        print(result)

