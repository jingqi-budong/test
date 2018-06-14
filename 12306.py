# -*- coding: utf-8 -*-
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


headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
    'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
}



ssl._create_default_https_context = ssl._create_unverified_context

c = cookielib.LWPCookieJar()#生成一个储存cookie的对象
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)
urllib2.install_opener(opener)

def make_cookie(name, value):
    return cookielib.Cookie(
        version=0,
        name=name,
        value=value,
        port=None,
        port_specified=False,
        domain="kyfw.12306.cn",
        domain_specified=True,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=False,
        expires=None,
        discard=False,
        comment=None,
        comment_url=None,
        rest=None
    )

#=============================================================

#===============================================================
city = {}
for i in station_name.split('@'):
    if not i:
        continue
    tmp_list = i.split('|')
    city[tmp_list[1]] = tmp_list[2]
#print city

from_station = city['杭州东']
to_station = city['郑州']
train_date = '2018-02-14'
seat = '软卧'


def getCode():
    req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.28303602478997547')
    codeimg = opener.open(req).read()#opener
    fn = open('code/code.png','wb')
    fn.write(codeimg)
    fn.close()

def code():
    print '正在获取验证码'
    getCode()
    req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-check')
    print '正在请求识别验证码'
    code = damatuWeb.calcCode()
    print code
    data = {
        'answer':code,
        'login_site':'E',
        'rand':'sjrand'
    }
    data = urllib.urlencode(data)#把字典类型数据转换成查询字符串
    html = opener.open(req,data=data).read()
    result = loads(html)
    if result['result_code'] == "4":
        print '验证码校验成功!'
        return True
    else:
        print '验证码校验失败!,正在重新执行'
        code()

def login():
    req = urllib2.Request('https://kyfw.12306.cn/passport/web/login')
    data = {
        'username':user_12306.user,
        'password':user_12306.password,
        'appid':'otn'
    }
    data = urllib.urlencode(data)
    html = opener.open(req,data=data).read()
    print 110,html
    result = loads(html)
    req = urllib2.Request('https://kyfw.12306.cn/otn/login/userLogin')
    req.headers = headers
    html = opener.open(req,data='_json_att=').read()
    #print 108,html

    req = urllib2.Request('https://kyfw.12306.cn/passport/web/auth/uamtk')
    req.headers = headers
    html = opener.open(req,data='appid=otn').read()
    print 109,html
    result = loads(html)
    newapptk = result['newapptk']
    req = urllib2.Request('https://kyfw.12306.cn/otn/uamauthclient')
    req.headers = headers
    html = opener.open(req,data='tk=%s' %newapptk).read()
    print 110,html
    req = urllib2.Request('https://kyfw.12306.cn/otn/login/userLogin')
    req.headers = headers
    html = opener.open(req)
    print 111,html.geturl()
    # req = urllib2.Request(html.geturl())
    # req.headers = headers
    # html = opener.open(req).read()
    # print html
    # print html.read()
    # if result['result_code'] == 0:
    #     print '登录成功!'
    #     return True
    # else:
    #     print '登录失败'

def getTrain():
    '''
    req = urllib2.Request('https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=jXTBpKOJH5&hashCode=HdTOPMAUtojwuTvvonMt3bRSNp0ZuGYWKwZqTEp0nRE&FMQw=1&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=27.0%20r0&yD16=0&EOQP=8f58b1186770646318a429cb33977d8c&jp76=e8eea307be405778bd87bbc8fa97b889&hAqN=Win32&platform=WEB&ks0Q=2955119c83077df58dd8bb7832898892&TeRS=680x1280&tOHY=24xx720x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=e2609cc4f0de78d6025fceb84a4b4adf&0aew=Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/60.0.3112.113%20Safari/537.36&E3gR=3fb1a2c60fa52d7ea12bb93631653198&timestamp=1505476340466')
    req.headers = headers
    html = opener.open(req).read()
    reg = r'"exp":"(\w+)","cookieCode":".*?","dfp":"(.*?)"'
    exp,dfp = re.findall(reg,html)[0]
    c.set_cookie(make_cookie('RAIL_EXPIRATION',exp))
    c.set_cookie(make_cookie('RAIL_DEVICEID',dfp))
    '''
    req = urllib2.Request(
        'https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=jXTBpKOJH5&hashCode=HdTOPMAUtojwuTvvonMt3bRSNp0ZuGYWKwZqTEp0nRE&FMQw=1&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=27.0%20r0&yD16=0&EOQP=8f58b1186770646318a429cb33977d8c&jp76=e8eea307be405778bd87bbc8fa97b889&hAqN=Win32&platform=WEB&ks0Q=2955119c83077df58dd8bb7832898892&TeRS=680x1280&tOHY=24xx720x1280&Fvje=i1l1o1s1&q5aJ=-8&wNLf=e2609cc4f0de78d6025fceb84a4b4adf&0aew=Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/60.0.3112.113%20Safari/537.36&E3gR=3fb1a2c60fa52d7ea12bb93631653198&timestamp=1505476340466')

    req.headers = headers
    html = opener.open(req).read()
    reg = r'"exp":"(\w+)","dfp":"(.*?)"'
    print re.findall(reg, html)
    exp, dfp = re.findall(reg, html)[0]
    print
    c.set_cookie(make_cookie('RAIL_EXPIRATION', exp))
    c.set_cookie(make_cookie('RAIL_DEVICEID', dfp))
    #ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/log?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(train_date,from_station,to_station))
    req.headers = headers
    html = opener.open(req).read()
    print 118,html
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(train_date,from_station,to_station))
    req.headers = headers
    res = opener.open(req)
    # data = StringIO.StringIO(res.read())#把返回压缩文件作为内存文件对象
    # info = gzip.GzipFile(mode='rb',fileobj=data)#解压文件
    # print res.geturl()
    # html =  info.read()
    html = res.read()
    #print 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(train_date,from_station,to_station)
    print 119,html,res.geturl()
    try:
        result = loads(html)
        print 220,result['data']['result']
        return result['data']['result']
    except Exception,e:
        time.sleep(2)
        getTrain()

#下单
def order(secretStr,tmp_list):

    #第1个请求
    print 107,secretStr
    req = urllib2.Request('https://kyfw.12306.cn/otn/login/checkUser')
    req.headers = headers
    html = opener.open(req,data='_json_att=').read()
    print 111,html
    #第2个请求
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest')
    print secretStr
    # data = {
    #     'secretStr':secretStr,
    #     'train_date':train_date,
    #     'back_train_date':'2017-09-07',
    #     'tour_flag':'dc',
    #     'purpose_codes':'ADULT',
    #     'query_from_station_name':'长沙',
    #     'query_to_station_name':'成都',
    #     'undefined':''
    # }
    # data = urllib.urlencode(data)
    data = 'secretStr={}&train_date={}&back_train_date={}&tour_flag=dc&purpose_codes=ADULT&query_from_station_name=长沙&query_to_station_name=成都&undefined'.format(secretStr,train_date,time.strftime('%Y-%m-%d'))
    print 11111,data
    req.headers = headers
    html = opener.open(req,data=data)
    print 222,html.read()
    print 333,html.geturl()
    req = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/initDc')
    req.headers = headers
    html = opener.open(req,'_json_att=').read()
    print html,88888
    reg = r"key_check_isChange':'(.*?)'"
    key_check_isChange = re.findall(reg,html)[0]
    # req = urllib2.Request('https://kyfw.12306.cn/otn/index/initMy12306')
    # req.headers = headers
    # html = opener.open(req).read()
    # print html
    req = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/initDc')
    req.headers = headers
    html = opener.open(req,data='_json_att=').read()
    #print 666,html
    reg = r"globalRepeatSubmitToken = '(\w{32})'"
    REPEAT_SUBMIT_TOKEN = re.findall(reg,html)[0]
    req = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs')
    req.headers = headers
    data = {
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
    }
    data = urllib.urlencode(data)
    html = opener.open(req,data=data).read()
    print 667,html
    req = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo')
    req.headers = headers
    data = {
        'cancel_flag':'2',
        'bed_level_order_num':'000000000000000000000000000000',
        'passengerTicketStr':'3,0,1,房志刚,1,412827198903104512,18368180275,N',
        'oldPassengerStr':'房志刚,1,412827198903104512,1_',
        'tour_flag':'dc',
        'randCode':'',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
    }
    data = urllib.urlencode(data)
    html = opener.open(req,data=data).read()
    print 668,html
    req = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount')
    req.headers = headers
    data = {
        'train_date':'Thu Sep 21 2017 00:00:00 GMT+0800 (中国标准时间)',
        'train_no':tmp_list[2],#2
        'stationTrainCode':tmp_list[3],#3
        'seatType':'3',
        'fromStationTelecode':from_station,
        'toStationTelecode':to_station,
        'leftTicket':tmp_list[12],#12
        'purpose_codes':'00',
        'train_location':tmp_list[15],#15
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
    }
    data = urllib.urlencode(data)
    html = opener.open(req,data=data).read()
    print 669,html
    req = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue')
    req.headers = headers
    data = {
        'passengerTicketStr':'3,0,1,房志刚,1,412827198903104512,18173119351,N',
        'oldPassengerStr':'房志刚,1,412827198903104512,1_',
        'randCode':'',
        'purpose_codes':'00',
        'key_check_isChange':key_check_isChange,
        'leftTicketStr':tmp_list[12],
        'train_location':tmp_list[15],
        'choose_seats':'',
        'seatDetailType':'000',
        'roomType':'00',
        'dwAll':'N',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
    }
    data = urllib.urlencode(data)
    html = opener.open(req,data=data).read()
    print html

code()
login()
# if login():
#查票
# print 11111111111111
# time.sleep(10)
for i in getTrain():
    tmp_list = i.split('|')
    #tmp_list[3] = 车次
    #tmp_list[8] = 出发时间
    #tmp_list[9] = 到达时间
    #tmp_list[26] = 无座
    #tmp_list[29] = 硬座
    #tmp_list[25] = 特等座
    #tmp_list[31] = 一等座
    #tmp_list[30] = 二等座
    #tmp_list[23] = 软卧
    # print tmp_list
    # a = 0
    # for n in tmp_list:
    #     print '[%s] %s' %(a,n)
    #     a += 1
    secretStr = tmp_list[0]
    if tmp_list[29] != u'无' and tmp_list[29] != '':
        print '有票'
        print tmp_list[3],tmp_list[8],tmp_list[9]
        break

    if tmp_list[23] != u'无' and tmp_list[23] != '':
        print '有票'
        print tmp_list[3],tmp_list[8],tmp_list[9]
        break
    else:
        print '没票'

order(secretStr=secretStr,tmp_list=tmp_list)