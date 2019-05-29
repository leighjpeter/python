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
    LOGIN_URL = BASE_URL + '/user/login/jsonp_is_protocol'
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
            'Connection':'close',
            'Cookie':'__ckguid=SFH5XG4UUbxKqBnQoWeFl43; smzdm_user_source=AE1214872282BB4D7A289D1AED648BB2; _ga=GA1.2.69308297.1521736089; device_id=19420365471521736089307441a18e7c0bb9b50cd4157cd9ac8c6d18b6; __jsluid=fd86ba55c7b30717622e0493679f836c; smzdm_user_view=E2AC582906290742C9DBE6D83BB9A9FE; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1548235211; wt3_sid=%3B999768690672041; PHPSESSID=e6aeba5f9b4c6f54af0d7c502ea38803; wt3_eid=%3B999768690672041%7C2152406605500665183%232154823521900676697; zdm_qd=%7B%7D; _gid=GA1.2.1283114500.1548660786; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1548661894; _gat_UA-27058866-1=1; sess=NjlkNGJ8MTU1Mzg0NTk0MXw3OTgxNjYyMTkyfGMzN2ZjNTNmOTg4NjBmZWZmY2ZjOTVlM2I4MzVjZjVl; user=user%3A7981662192%7C7981662192'
        }

        params = {
            'username': self.username,
            'password': self.password,
        }

        # r = self.session.get(self.BASE_URL, headers=headers, verify=True)
        # r = self.session.post(self.LOGIN_URL, headers=headers, verify=True)
        r = self.session.get(self.CHECKIN_URL, headers=headers, verify=True)
        if r.status_code != 200:
            raise SMZDMDailyException(r)

        data = r.text
        jdata = json.loads(data)
        return jdata

if __name__ == '__main__':
    # if SMZDM_USERNAME is '' or SMZDM_PASSWORD is '':
    #     print('SMZDM_USERNAME and SMZDM_PASSWORD required')
    #     sys.exit()
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

