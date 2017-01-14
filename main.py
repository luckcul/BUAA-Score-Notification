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
	score = []
	while True:
		try:
			getHtml(LoginUser, LoginPassword)
			score = getScore()
			break
		except Exception, e:
			print '!',
	L = len(score)
	#输出 第一次登陆时的成绩，认为这些是已知的，不会发邮件通知
	for x in score:
		print x[0].encode('utf-8'), x[1].encode('utf-8')

	while True:
		while True :
			try: 
				#继续不断获取最新成绩
				getHtml(LoginUser, LoginPassword)
				scoreNew = getScore()
				break
			except Exception, e:
				print '!',
		for i in range(0, L):
			#如果有新成绩出现，发邮件通知
			if score[i][1] != scoreNew[i][1] :
				print 'new!!'
				sendMail(host, postfix, user, password, [to], scoreNew[i][0].encode('utf-8'), scoreNew[i][1].encode('utf-8'))
		print '.',
		score = scoreNew
		# 间隔6S
		time.sleep(6)