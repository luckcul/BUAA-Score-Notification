#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-12 21:21:04
# @Author  : luckcul (tyfdream@gmail.com)
# @Version : 2.7.12

'''
sendMail.py
用来发送邮件
'''

import smtplib
import time
import sys
from email.mime.text import MIMEText

def sendMail(mail_host, mail_postfix, mail_user, mail_pass, to_list, sub, content):
	me = "Push" + "<" + mail_user + "@" + mail_postfix + ">"
	msg = MIMEText(content, _subtype = 'plain', _charset = 'utf-8')
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	count = 0
	while True : 
		try:
			server = smtplib.SMTP()
			server.connect(mail_host)
			server.login(mail_user, mail_pass)
			server.sendmail(me, to_list, msg.as_string())
			server.close()
			return True
		except Exception , e:
			count += 1
			if cou >= 10 : 
				print 'send mail failed'
				return False
			time.sleep(3)
