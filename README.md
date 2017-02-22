# BUAA-Score-Notification

考完了，等成绩，每次刷渣渣教务系统也是心累。所以写了一个成绩更新通知，每当成绩跟新的时候，会发给自己指定的邮箱。

## Requirements and Prerequisites:

* Python 2.7.x
  * BeautifulSoup 4.5.1
  * PIL 1.1.7
  * pytesser 0.0.1


## Structure

* login.py 模拟登陆，获得成绩页面html
* ocr.py ：login中用到的验证码识别
* parseHTML.py：从HTML中提取课程名和成绩
* sendMail ： 发邮件
* main.py ：run!


## Tips

* 在`conf.ini`里面填入自己教务处的账号、密码。发邮件的服务器、用户名、密码和收邮件通知的邮件地址。
* 每6s获得一次成绩





