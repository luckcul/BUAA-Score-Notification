#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-12 22:23:17
# @Author  : luckcul (tyfdream@gmail.com)
# @Version : 2.7.12

import os
from login import *
from parseHTML import *
from sendMail import sendMail
import time

if __name__ == '__main__':
	LoginUser, LoginPassword = getConf('conf.ini', 1)
	host, postfix, user, password, to = getConf('conf.ini', 2)
	ans = {}
	while True:
		try:
			getHtml(LoginUser, LoginPassword)
			ans = getScore()
			break
		except Exception, e:
			print '!',
	L = len(ans)
	#输出 第一次登陆时的成绩，认为这些是已知的，不会发邮件通知
	for (course, score) in ans.items():
		print course.encode('utf-8'), score.encode('utf-8')

	while True:
		while True :
			try: 
				#继续不断获取最新成绩
				getHtml(LoginUser, LoginPassword)
				ansNew = getScore()
				break
			except Exception, e:
				print '!',
		for course in ansNew:
			#如果有新成绩出现，发邮件通知
			score = ans.get(course)
			scoreNew = ansNew.get(course)
			if scoreNew != score and score != None and scoreNew != None:
				print 'new!',
				sendMail(host, postfix, user, password, [to], course.encode('utf-8'), scoreNew.encode('utf-8'))
		print '.',
		ans = ansNew
		# 间隔6S
		time.sleep(6)