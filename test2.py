#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 16:06
# @Author  : 强子
# @File    : test2.py
# @Software: PyCharm
import urllib2
import ssl

headers = {
    'Cookie':'JSESSIONID=ABC514520736B08925B689E5838B1D20; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=401080586.24610.0000; fp_ver=4.5.1; BIGipServerpassport=1005060362.50215.0000; RAIL_EXPIRATION=1505597202418; RAIL_DEVICEID=cukDsy4Tj2_wNhBR-yEOAqPUa3V_kkjd3RsAUGr0xnoculpCkr8AaluSV7HrD-nuR3leDLHJHojZBeHIAhnd_mKrlG5Ixxj-haaPlMR7cIAeHc9ietE9iyGAzgM0Sp5WpDrmRfadEfhPR69nJUR5H0GBsavSXCA-; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u6210%u90FD%2CCDW; _jc_save_fromDate=2017-09-22; _jc_save_toDate=2017-09-13; _jc_save_wfdc_flag=dc'
}

ssl._create_default_https_context = ssl._create_unverified_context

req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2017-09-22&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT')
req.headers = headers
html = urllib2.urlopen(req).read()
print html