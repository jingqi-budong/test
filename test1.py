#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/8 20:19
# @Author  : 强子
# @File    : test1.py
# @Software: PyCharm
import urllib2
import urllib
import cookielib
import damatuWeb
import user_12306
import ssl
from json import loads
from cons import station_name
import time
import re
import gzip,StringIO

# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
#     #'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
#     #'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
# }
city = {}
for i in station_name.split('@'):
    if not i:
        continue
    tmp_list = i.split('|')
    city[tmp_list[1]] = tmp_list[2]
#print city

from_station = city['长沙']
to_station = city['成都']
train_date = '2017-09-21'
seat = '软卧'
ssl._create_default_https_context = ssl._create_unverified_context

c = cookielib.LWPCookieJar()#生成一个储存cookie的对象
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)
urllib2.install_opener(opener)
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
    'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #'Cookie':'JSESSIONID=EB3EB5BDA83EA01D0929B3C86255A1E5; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=1557725450.50210.0000; fp_ver=4.5.1; RAIL_EXPIRATION=1505374443417; RAIL_DEVICEID=HYy9oBR3tgB0uOs08zBXHens300rM5ZM_1NuPo1MJBclDM9cxT6hkolqTn49yd_BSLvQQG62jAtdwoFOYC4Pwy8IL0TwpV-pjybD1P3cqirQffN5Oa0lLc_HC6MX-6RZXm8HQYW6etOWxamweJpAavtmvY3NnRcI; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u6210%u90FD%2CCDW; _jc_save_fromDate=2017-09-12; _jc_save_toDate=2017-09-11; _jc_save_wfdc_flag=dc'
}
# req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/log?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(train_date,from_station,to_station))
# req.headers = getheaders
# html = opener.open(req).read()
# print 118,html
req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(train_date,from_station,to_station))
req.headers = headers
html = opener.open(req)
print html.read()
#print 119,html.read(),html.geturl()
# data = StringIO.StringIO(html.read())#把返回压缩文件作为内存文件对象
# info = gzip.GzipFile(mode='rb',fileobj=data)#解压文件
# print info.read()
print 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(train_date,from_station,to_station)
