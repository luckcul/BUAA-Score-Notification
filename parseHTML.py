#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-12 21:21:04
# @Author  : luckcul (tyfdream@gmail.com)
# @Version : 2.7.12

import os
import sys
from bs4 import BeautifulSoup
import ConfigParser

def getConf(config_file_path, choose):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file_path)
    # s = cf.sections()
    # cf.set('ID', 'user', 'ba')
    # cf.write(open(config_file_path, 'w'))
    #获取 配置中教务处的用户名和密码
    if choose == 1 :
    	return cf.get('ID', 'user'), cf.get('ID', 'password')
    #获取 配置中发邮件的用户名，密码等和收件邮箱
    else :
    	return cf.get('mail', 'host'), cf.get('mail', 'postfix'), cf.get('mail', 'user'), cf.get('mail', 'password'), cf.get('mail', 'to')

def getScore():
	ret = []
	soup = BeautifulSoup(open("a.html"), "lxml")
	tag = soup.tr
	x = soup.find('form').findAll('tr')
	L = len(x)
	for i in range(0, L-1):
		temp = []
		temp.append( x[i].findAll('td')[2].text.strip() )
		temp.append( x[i].findAll('td')[4].text.strip() )
		ret.append(temp)
	return ret


