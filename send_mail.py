#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr


# from_addr = input('From:')
from_addr = 'duang@wansecheng.com'
# pwd = input('Password:')
pwd = 'Hello1234'
# to_addr = input('To:')
to_addr = '308781258@qq.com'
# smtp_server = input('SMTP server:')
smtp_server = 'smtp.exmail.qq.com'


# 设置 邮件主题 收件人 发件人
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(), addr))


# msg = MIMEText('hello,send by Python3','plain','utf-8')
# msg['From'] = _format_addr('Duang Duang Duang <%s>' % from_addr)
# msg['To'] = _format_addr('ET<%s>' % to_addr)
# msg['Subject'] = Header('对方不想和你说话，并向你扔了一个漂流瓶...','utf-8').encode()

# 发送HTML邮件
# 构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8')


# 发送附件
msg = MIMEMultipart()
msg['From'] = _format_addr('Duang Duang Duang <%s>' % from_addr)
msg['To'] = _format_addr('ET<%s>' % to_addr)
msg['Subject'] = Header('对方不想和你说话，并向你扔了一个漂流瓶...','utf-8').encode()
msg.attach(MIMEText('send with file','plain','utf-8'))

with open('/vagrant/demo/a.png','rb') as f:
	 # 设置附件的MIME和文件名，这里是png类型:
	mime = MIMEBase('image', 'png', filename='a.png')
	# 加上必要的头信息:
	mime.add_header('Content-Disposition', 'attachment', filename='a.png')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	# 把附件的内容读进来:
	mime.set_payload(f.read())
	# 用Base64编码:
	encoders.encode_base64(mime)
	# 添加到MIMEMultipart:
	msg.attach(mime)





import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr,pwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()