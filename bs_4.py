#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import requests
import json
import logging
from datetime import datetime,timezone,timedelta

# 获取联系方式
# hotel_url = 'http://inn.ctrip.com/inn/6742823.html?isFull=F'
# hotel_url = urlparse(hotel_url).scheme+"://"+urlparse(hotel_url).netloc+urlparse(hotel_url).path+'?'+urlparse(hotel_url).query
# html = urlopen(hotel_url)
# bsObj = BeautifulSoup(html, 'html.parser')
# p = bsObj.find(id='ctl00_MainContentPlaceHolder_div_inndesc').find('p',{'class':'htl_s_info'})
# time_num = p.get_text(strip=True).split(u'联系方式')
# print(time_num)
# try:
# 	span = bsObj.find(id='ctl00_MainContentPlaceHolder_div_inndesc').find('p',{'class':'htl_s_info'}).span['data-real']
# 	tel = re.split(r'\s\<a',span)
# except Exception as e:
# 	logging.exception(e)
# 	print(hotel_url)
# finally:
# 	time_num = tel = ['0']
# print(tel[0])


def getTel(hotel_url):
	hotel_url = 'http://inn.ctrip.com' + hotel_url
	hotel_url = urlparse(hotel_url).scheme+"://"+urlparse(hotel_url).netloc+urlparse(hotel_url).path+'?'+urlparse(hotel_url).query

	html = urlopen(hotel_url)
	bsObj = BeautifulSoup(html, 'html.parser')
	p = bsObj.find(id='ctl00_MainContentPlaceHolder_div_inndesc').find('p',{'class':'htl_s_info'})
	time_num = p.get_text(strip=True).split(u'联系方式')
	try:
		span = bsObj.find(id='ctl00_MainContentPlaceHolder_div_inndesc').find('p',{'class':'htl_s_info'}).span['data-real']
		tel = re.split(r'\s\<a',span)
	except Exception as e:
		logging.exception(e)
		errLinks.add(hotel_url)
		tel = ['暂无']
	return {'time_num':time_num[0], 'tel':tel[0]}
	
def start_requests(url, tet):
	r = requests.post(url, params=tet)
	hotelPositionJSON =  json.loads(r.text).get('hotelPositionJSON')
	with open('test.txt', 'a',encoding='utf-8') as f:
		str = ''
		for info in hotelPositionJSON:
			hotel_url = info['url']
			time_num_tel = getTel(hotel_url)
			str += info['name']+'	'+info['address']+'	'+time_num_tel['tel']+'	'+time_num_tel['time_num']+'	'+info['dpcount']+'	'+info['score']+'	'+info['stardesc']+'\r\n'
		f.write(str)

import math
def progress(max, current):
	p = 0
	if current:
		p = round(current / max * 100, 2)
	print("progress: [%-50s] %d%%\r" %( '#'[:] * math.ceil(p/2),p ))
	if current == max :
		print("\n")

errLinks = set()

bj_dt_start = str(input('请输入入住日期：'))
bj_dt_end = str(input('请输入退房时间：'))
if bj_dt_start == '':
	utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
	bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
	bj_dt_start = bj_dt.strftime('%Y-%m-%d')
	if bj_dt_end == '':
		bj_dt_end = (bj_dt + timedelta(days=1)).strftime('%Y-%m-%d')


url = 'http://inn.ctrip.com/inn/Tool/AjaxHotelBaseList.aspx'
params = {
		'__VIEWSTATEGENERATOR':'1F7A0693',
		'CorrelationId':'5589071967623096105',
		'cityName':'%E6%9D%AD%E5%B7%9E',
		'StartTime':bj_dt_start,
		'DepTime':bj_dt_end,
		'txtkeyword':'',
		'Resource':'',
		'Room':'',
		'Paymentterm':'',
		'BRev':'',
		'Minstate':'',
		'PromoteType':'',
		'PromoteDate':'',
		'operationtype':'NEWHOTELORDER',
		'PromoteStartDate':'',
		'PromoteEndDate':'',
		'OrderID':'',
		'RoomNum':'',
		'IsOnlyAirHotel':'F',
		'cityId':'17',
		'city':'17',
		'cityPY':'hangzhou',
		'cityCode':'0571',
		'positionArea':'',
		'positionId':'',
		'keyword':'',
		'hotelId':'',
		'htlPageView':'0',
		'hotelType':'F',
		'hasPKGHotel':'F',
		'hotelStar':'',
		'requestTravelMoney':'F',
		'isusergiftcard':'F',
		'useFG':'F',
		'HotelEquipment':'',
		'priceRange':'-2',
		'hotelBrandId':'',
		'promotion':'F',
		'prepay':'F',
		'IsCanReserve':'F',
		'OrderBy':'99',
		'OrderType':'',
		'k1':'',
		'k2':'',
		'CorpPayType':'',
		'viewType':'',
		'checkIn':bj_dt_start,
		'checkOut':bj_dt_end,
		'DealSale':'',
		'ulogin':'',
		'hidTestLat':'0%7C0',
		'AllHotelIds':'',
		'psid':'',
		'HideIsNoneLogin':'T',
		'hotelIds':'',
		'markType':'0',
		'zone':'',
		'location':'',
		'type':'',
		'brand':'',
		'group':'',
		'feature':'',
		'equip':'',
		'star':'',
		'sl':'',
		's':'',
		'l':'',
		'disabledFilter':'{"price":"","star":"","type":"","group":"","brand":"","equip":""}',
		'enabledFilter':'{"feature":""}',
		'price':'',
		'a':'0',
		'page':'1',
	}
r = requests.post(url, params=params)
paging = json.loads(r.text).get('paging')
hotelAmount = json.loads(r.text).get('hotelAmount')
pageTotal = int(re.search('(\d+)\s',paging).group(1))
for page in range(pageTotal):
	page = page + 1
	params['page'] = page
	start_requests(url, params)
	progress(pageTotal,page)

print(hotelAmount,errLinks)

# print(r.text)
# print(r.json) # <bound method Response.json of <Response [200]>>
# print(r.status_code) # 200
# print(r.headers) # {'Server': 'Tengine/2.1.2', 'Date': 'Wed, 29 Nov 2017 02:06:59 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '13977', 'Connection': 'keep-alive', 'Cache-Control': 'private', 'Content-Encoding': 'gzip', 'Vary': 'Accept-Encoding', 'X-AspNet-Version': '4.0.30319', 'X-Powered-By': 'ASP.NET'}
# print(r.cookies)