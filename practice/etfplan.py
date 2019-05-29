#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Arnold Huang and Croc He and leighj
# Date: 9/1/2017
# Current Version： 1.0
# Change History: 9/1/2017  Initial draft
#                  9/4/2017  Update according to the Jind's comments except NAV
#                  9/21/2017 Update the script to add nav.
#                  11/7/2017 First release version for share\
#                  5/23/2018 python3 beta
# E-mail: leighj@163.com
# Weixin: Delete
# GitHub: https://github.com/leighj/ETFPlan_FundBuyer
# Comment: 严禁用于商业目的！

# 前提条件
# pip install lxml requests
# 防止提示 ssl warning     pip install pyopenssl ndg-httpsclient pyasn1


import time
import datetime
import re
from urllib import request
import lxml.html

#Croc
import requests
import json
import sys

import hashlib
import random


#get_x_sign， 与时间相关，在调试程序前，请保证宿主机的时间为北京时区的真实当前时间
def get_x_sign(len = 32):
    curtime =  str(time.time()).replace('.', '')[:13]
    target = str("%f")%(float(curtime)*1.01)
    target = target[0:13]
    sha256 = hashlib.sha256()
    sha256.update(target.encode('utf-8'))
    target_sha256 = sha256.hexdigest().upper()
    x_sign = curtime + target_sha256[0:len]
    return x_sign

#下载普通HTML网页
def common_download(url, retry=10):
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    def get_html():
        response = request.urlopen(req)
        time.sleep(1)
        html = response.read().decode('utf-8')
        return html
    for try_times in range(retry):
        try:
            html = get_html()
            break
        except:
            if try_times < retry - 1:
                continue
            else:
                print("Network error!")
                sys.exit()
    return html

#从且慢网站上下载所有的计划内的基金代码清单
def get_funds(retry = 10):
    headers = {"Accept" : "application/json",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        "Connection" : "keep-alive",
        "Host" : "qieman.com",
        "Referer" : "https://qieman.com/longwin/index",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "x-sign" : "",
    }
    headers["x-sign"] = get_x_sign()
    funds_pattern = re.compile('"fund":({.*?})')
    while retry > 0:
        retry -= 1
        headers["x-sign"] = get_x_sign()
        return_data = requests.get("https://qieman.com/pmdj/v2/long-win/plan", headers=headers)
        fundlists = funds_pattern.findall(return_data.text)

        funds = []
        for fund in fundlists:
            myfund = json.loads(fund)
            if len(myfund['fundCode']) == 6:
                funds.append(myfund['fundCode'])
        if len(funds) == 0 and retry !=0:
            time.sleep(1)
            continue
        elif len(funds) == 0 and retry == 0:
            print("无法获取基金列表，请重新运行程序！")
            sys.exit()
        else:
            break
    funds = list(set(funds)) # 去重
    funds.remove("000614")  #德国DAX， 没数据
    funds.remove("501018")  #南方原油，猪队友，不要不要的
    funds.remove("001061")  #华夏海外债券 没数据
    funds.remove("110027")  #易方达安心回报债券A
    return funds

#计算天数差
def cal_time(date1,date2):
    date1 = time.strptime(date1,"%Y-%m-%d %H:%M:%S") # struct_time对象
    date2 = time.strptime(date2,"%Y-%m-%d %H:%M:%S") # struct_time对象
    date1 = datetime.datetime(date1[0], date1[1], date1[2], date1[3], date1[4], date1[5])
    date2 = datetime.datetime(date2[0], date2[1], date2[2], date2[3], date2[4], date2[5])
    return (date2-date1).days

#从天天基金网获得分红信息
def get_fhsp_records(fundid, sdate):
    html = common_download("http://fund.eastmoney.com/f10/fhsp_"+fundid+".html")
    text = "".join(html.split())
    fhsp_pattern = re.compile(r"<td>(\d{4}-\d{2}-\d{2})</td><td>每份派现金(\d*\.\d{4})元</td>")
    tmp = fhsp_pattern.findall(text)
    retval = []
    for i in range(0, len(tmp)):
        delta = cal_time(sdate, tmp[i][0]+" 15:00:00" )
        if delta > 0 :
            retval.append(tmp[i])

    retval.reverse() # 反向排序
    return retval

#从天天基金网获得历史上该基金品种的历史净值清单
def get_history_price_by_fund(fundid, starttime):
    enddate = time.strftime('%Y-%m-%d',  time.localtime(time.time()))
    startdate = starttime.split(" ")[0]
    delta_days = cal_time(startdate+" 00:00:00", enddate+" 00:00:00")
    html = common_download("http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code="+fundid+"&page=1&per="+str(delta_days)+"&sdate=" + startdate+ "&edate=" + enddate)
    html = html.split("<tr>")
    history = []
    history_pattern = re.compile(r"<td>(\d{4}-\d{2}-\d{2})</td><td class='tor bold'>(\d*.\d{4})</td>.*")
    for i in range(2, len(html)):
        history.append( history_pattern.findall(html[i]) )
    return history

#从且慢网页获取E大的某品种的购买信息
def get_raw_price(fundid):
    headers = {"Accept" : "application/json",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        "Connection" : "keep-alive",
        "Host" : "qieman.com",
        "Referer" : "",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "x-sign" : ""}
    headers["Referer"] = "https://qieman.com/longwin/funds/" + fundid
    headers["x-sign"] = get_x_sign()
    return_data = requests.get("https://qieman.com/pmdj/v2/long-win/plan/history?fundCode=%s" %(fundid), headers=headers)
    price_pattern = re.compile('"fund":\{(.*?0)\}')
    datalists = price_pattern.findall(return_data.text)

    buyrecord = []
    sellrecord = []
    for datalist in datalists:
        mydata = []
        datalist = '{' + datalist.replace('}','') + '}'
        mydatalist = json.loads(datalist)
        if mydatalist["orderCode"] == '022' and mydatalist["nav"] is not None:
            mynavDate = time.strftime("%Y-%m-%d", time.localtime(mydatalist["adjustTxnDate"]/1000))
            mydata.append(mynavDate)
            mydata.append(mydatalist["nav"])
            mydata.append(mydatalist["tradeUnit"])
            buyrecord.append(mydata)
        elif mydatalist["orderCode"] == '024':
            sellrecord.append(mydatalist["tradeUnit"]) #[1,1]卖出记录
    # print(buyrecord)   # [['2018-04-17', 1.092, 1], ['2018-04-01', 1.116, 1], ['2018-02-28', 1.161, 1], ['2018-02-12', 1.142, 1], ['2017-12-28', 1.328, 1], ['2017-12-13', 1.31, 1], ['2017-05-22', 1.149, 1], ['2017-01-24', 1.107, 1], ['2016-12-29', 1.375, 1], ['2016-12-14', 1.375, 1]]
    prices = []
    if len(buyrecord) != 0:
        firstbuydate = str(buyrecord[-1][0])+" 15:00:00"
        history = get_history_price_by_fund(fundid, firstbuydate)
        fhs = get_fhsp_records(fundid,firstbuydate)
        # print(fhs) # [('2017-01-17', '0.3000'), ('2018-01-18', '0.1880')]
        for item in buyrecord:
            buydate = str(item[0])
            buyprice = float(item[1])
            rate = []
            for fh in fhs:
                fhdate = str(fh[0])
                fhmoney = float(fh[1])

                #if fh date is before buy date, not to cut nav rate
                if cal_time(buydate+" 15:00:00", fhdate+" 15:00:00")  < 0  :
                    continue

                #to find the net on that day
                for net in history:
                    #find it!
                    if net[0][0] == fhdate:
                        net_that_day = float(net[0][1])
                        rate_that_day = (net_that_day + fhmoney)/net_that_day
                        rate.append(rate_that_day)
                        break
            navrate = 1
            if len(fhs) > 0:
                for r in rate:
                    navrate = navrate * r
            prices.append(("%.4f" % buyprice, "%.4f" % navrate))

        prices.sort()

        #sellrecord = re.findall(unicode(r"卖出(\d*)份", 'utf8'),text)
        sellrecordcount = len(sellrecord)
        sellcount = 0
        if(sellrecordcount != 0):
            for i in sellrecord:
                sellcount = sellcount+int(i)
            for i in range(1, sellcount+1):
                prices.pop()
        # print(prices) # [('0.9280', '1.0000'), ('0.9334', '1.0000'), ('0.9354', '1.0000'), ('0.9456', '1.0000'), ('0.9504', '1.0000')]
        return prices
    else:
        return False

#从腾讯财经下载当前估值数据 
#当前没用
#important
def get_current_price_from_tencent(fundid):
    html = common_download("http://gu.qq.com/jj"+fundid+"?pgv_ref=fi_smartbox&_ver=2.0")
    tree = lxml.html.fromstring(html)
    c_price_pattern = re.compile(r"单位净值：<span>(\d*\.\d{4})")
    gu_price_pattern = re.compile("最新估值")
    if len(gu_price_pattern.findall(html))>0:
        span = tree.cssselect('span#main5')[0]
        fundprice = span.text_content()
        if fundprice == "--":
            span = tree.cssselect('span#main0')[0]
            fundprice = span.text_content()
    else:
        span = c_price_pattern.findall(html)
        if len(span) > 0:
           fundprice = "".join(span[0])
        else:
           fundprice = "--"

    span = tree.cssselect('span.col_1')[0]
    fundname = span.text_content()
    return fundname, fundprice

nterval = 60
retry = 10

#从天天基金网下载当前估值数据，这是当前使用的估值数据源
#important
def get_current_price_from_em(fundid):
    headers = {
        "Accept" : "*/*",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        "Cache-Control" : "no-cache",
        "Connection" : "keep-alive",
        "Host" : "fundgz.1234567.com.cn",
        "Pragma" : "no-cache",
        "Referer" : "",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    }
    headers["Referer"] = "http://fund.eastmoney.com/%s.html" %fundid
    for retry_times in range(0, retry+1):
        try:
            random_value = random.sample(["0","1","2","3","4","5","6","7","8","9"], 1)
            curtime =  str(time.time()).replace('.', '') + random_value[0]
            return_data = requests.get("http://fundgz.1234567.com.cn/js/%s.js?rt=%s" %(fundid, curtime), headers=headers)
            break
        except:
            if retry_times < retry:
                time.sleep(1)
                continue
            else:
                # print ("\x1b[2J") # 清屏
                print (u"Network error!")
                sys.exit()
    raw_data = re.findall('jsonpgz\((.*)\)', return_data.text)
    try:
        data = json.loads(raw_data[0])
    except Exception as e:
        print(fundid)
        raise e
    return data['name'], data['gsz']

#生成建议信息。
def find_all_funds_prices(retrytimes=3):
    qieman_funds = get_funds()

    prices = []
    suggestion1 = ""
    suggestion2 = ""
    today_nav = 0
    failed_funds= []
    def fund_analyst():
        retry=0
        suggestion1 = ""
        suggestion2 = ""
        for fundid in qieman_funds:
            #fundid = "".join(fund)
            prices_and_rate = get_raw_price(fundid)

            while( prices_and_rate is False and retry < 10):
                prices_and_rate  = get_raw_price(fundid)
                retry = retry+1
            if retry > 10:
                failed_funds.append(fundid)
                countine
            else:
                name, current_price = get_current_price_from_em(fundid)

                if ( re.findall(u"QDII", name)  ):
                    pass
                else:
                    print(u"\n正在分析基金(%s)%s..." % (fundid, name))
                    eda_prices=[]
                    if (current_price != "--"):
                        count = 0
                        price_in_history = []
                        for item in prices_and_rate:
                            price = float(item[0])
                            rate = float(item[1])

                            #########
                            eda_prices.append((price,rate))
                            ########
                            todaynav = float(current_price) * rate
                            if todaynav < price :

                                print(u"%s 当前复权净值%.4f低于历史购入复权净值: %.4f" % (name, todaynav, price) )

                                count = count+1
                            ####
                        #这里其实是调和平均数函数，并不是算术平均数
                        def average(seq):
                            sum = 0
                            # print (seq)                 #这里是打印出每次买入的价格和对应的复权率。调试用
                            for item in seq:
                                sum = sum + float(1/ (item[0]/item[1]) )
                            # print (len(seq)/sum)        #这里是打印出均价，调试用
                            return len(seq)/sum

                        if (len(eda_prices)>0):

                            if (  average(eda_prices) - float(current_price) > 0  ):
                                suggestion1 += (u"梭哈买入(%s) %s %d份\n" % (fundid, name, len(eda_prices) ))

                            if(count>0):
                                suggestion2 += (u"基于空仓买入：(%s) %s %d份\n" % ( fundid, name, count))
        return (suggestion1, suggestion2)
    suggestion1, suggestion2 = fund_analyst()

    if len(failed_funds) != 0:
        print ("因数据异常,以下基金未做分析，如有需要，请重新运行本程序：")
        for fundid in failed_funds:
            fundid = "".join(fund)
            name, current_price = get_current_price(fundid)
            print (u"(%s) %s" %(fundid, name))

    print("================================================\n")
    print(u"\n注意\n    1. 以下建议只做参考，作者Arnold Huang不为任何后果负责!!!")
    print(u"    2. 本程序提供基于空仓情况下的投资建议，已持仓部分基金的同学请检查持仓情况后做相应操作。")
    print(u"    3. QDII种类的基金不排除估值不准确的情况，请自行判断")
    print(u"    4. 投资有风险，买基需谨慎!!!\n")
    print(u"-----------------------------------------------\n")
    print(u"如下品种当前净值估值比E大平均持有成本低，对于零持仓的朋友适用于以下购买策略：\n")
    print(suggestion1)
    print(u"-----------------------------------------------\n")
    print(u"对于部分持有或者倾向于使用阶梯式补仓的朋友，参考如下：\n")
    print(suggestion2)
    print("================================================")


time_start = time.time()
find_all_funds_prices()
# print(get_funds())      # ['003376', '003765', '000614', '270048', '001061', '502010', '110026', '001064', '050027', '004752', '160416', '000478', '001180', '000968', '100032', '501018', '001051', '000051', '162411', '000071', '001052', '000216']

# get_raw_price('100032')

# get_history_price_by_fund('000071','2015-08-31 15:00:00')
# get_fhsp_records('100032','2015-08-31 15:00:00') # [('2016-02-02', '0.3500'), ('2017-01-17', '0.3000'), ('2018-01-18', '0.1880')]
# get_current_price_from_em('001061')
# get_current_price_from_tencent('001061')
time_end = time.time()
print ("运行时间： %.2fsec" %(time_end - time_start))
