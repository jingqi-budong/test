#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ jingqi


import urllib2

proxyswitch = True

httpproxy_handler = urllib2.ProxyHandler({"http" : "61.135.217.7:80"})

nullproxy_handler = urllib2.ProxyHandler({})

if proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)
print response.read()