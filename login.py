#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-12 19:33:33
# @Author  : luckcul (tyfdream@gmail.com)
# @Version : 2.7.12

import os
import urllib
import urllib2
import cookielib
import re
from ocr import ocr
import socket
headers = {
	'Host':"gsmis.graduate.buaa.edu.cn",
	'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
	'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	'Referer':"http://gsmis.graduate.buaa.edu.cn/gsmis/indexAction.do",
	'Connection':"keep-alive",
	'Upgrade-Insecure-Requests':"1", 
	'Cookie' : ''
}
postdata = {
	'id' : '',
	'password' : '',
	'checkcode' : ''
}
#create cookie
cookjar = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cookjar)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

#set socket time
socket.setdefaulttimeout(15)

def login(user, password):
	# print user, password
	hostUrl = r'gsmis.graduate.buaa.edu.cn'
	postUrl = r'http://gsmis.graduate.buaa.edu.cn/gsmis/indexAction.do'
	postdata['id'] = user 
	postdata['password'] = password
	

	url1 = r'http://gsmis.graduate.buaa.edu.cn/gsmis/Image.do'
	req = urllib2.Request(url1)
	res = urllib2.urlopen(req)
	pic = res.read()
	save = open(r'image.jpg', 'wb')
	save.write(pic)
	save.close()
	# os.system('image.jpg')
	# verificationCode = raw_input()
	verificationCode = ocr('image.jpg')
	postdata['checkcode'] = verificationCode
	# print verificationCode
	s = str(cookjar)

	#add cookie to headers
	rule = r'Cookie (.*) for'
	cookieID = re.findall(rule, s)[0]
	headers['Cookie'] = cookieID

	#post data
	POSTDATA = urllib.urlencode(postdata)
	reqq = urllib2.Request(postUrl, POSTDATA, headers)
	ress = urllib2.urlopen(reqq)
	
	wow = r'http://gsmis.graduate.buaa.edu.cn/gsmis/toModule.do?prefix=/py&page=/pySelectCourses.do?do=xsXuanKe'
	req1 = urllib2.Request(wow, None ,headers)
	res1 = urllib2.urlopen(req1)

	

def getScoreHtml():
	url2 = r'http://gsmis.graduate.buaa.edu.cn/gsmis/py/pyYiXuanKeCheng.do'
	req2 = urllib2.Request(url2, None, headers)
	res2 = urllib2.urlopen(req2)
	con =  res2.read()
	con = ''.join(con.split('\n'))
	# print len(con)
	if len(con) < 10000 :
		return False
	handlee = file('a.html', 'w') 
	handlee.write(con)
	handlee.close()
	return True

def getHtml(user, password):
	while getScoreHtml() == False:
		login(user, password)
		print 'x',