#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import sys
import requests
import re
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/Users/jessica/Dev/python/practice/smzdm.log',
                filemode='a')

SMZDM_USERNAME = os.getenv('SMZDM_DAILY_USERNAME') or '' # username or email
SMZDM_PASSWORD = os.getenv('SMZDM_DAILY_PASSWORD') or '' # password

class SMZDMDailyException(Exception):
    def __init__(self, req):
        self.req = req

    def __str__(self):
        return str(self.req)

class SMZDMDaily(object):
    BASE_URL = 'https://zhiyou.smzdm.com' 
    LOGIN_URL = BASE_URL + '/user/login/ajax_check'
    CHECKIN_URL = BASE_URL + '/user/checkin/jsonp_checkin'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.keep_alive = False

    def checkin(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0',
            'Host': 'zhiyou.smzdm.com',
            'Referer': 'http://www.smzdm.com/',
            'Connection':'close'
        }

        params = {
            'username': self.username,
            'password': self.password,
        }

        r = self.session.get(self.BASE_URL, headers=headers, verify=True)
        r = self.session.post(self.LOGIN_URL, data=params, headers=headers, verify=True)
        r = self.session.get(self.CHECKIN_URL, headers=headers, verify=True)
        if r.status_code != 200:
            raise SMZDMDailyException(r)

        data = r.text
        jdata = json.loads(data)
        return jdata

if __name__ == '__main__':
    if SMZDM_USERNAME is '' or SMZDM_PASSWORD is '':
        print('SMZDM_USERNAME and SMZDM_PASSWORD required')
        sys.exit()
    try:
        smzdm = SMZDMDaily(SMZDM_USERNAME, SMZDM_PASSWORD)
        result = smzdm.checkin()
    except SMZDMDailyException as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    else:
        if result['error_code'] == 0 :
            str = '成功连续签到'+str(result['data']['checkin_num'])+'天，积分'+str(result['data']['point'])+'金币'+str(result['data']['gold'])+'等级'+str(result['data']['rank'])
        else:
            str = '失败：'+result['error_msg']
        logging.info(str)

