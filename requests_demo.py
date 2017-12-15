#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 强大的Requests
import requests

# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# r.url
# r.encoding
# r.content
# r.text
# r.json()
# r.headers
# r.cookies[]
#  r.raise_for_status() 来抛出异常 或者检查 r.status_code 



# api_github = 'https://api.github.com'
# headers = {"Authorization":"token 44ecafe2e4832eb726fa142e85ad42cf5c958ba0"}
# r = requests.get(api_github+'/user', headers=headers,stream=True)
# print(r.raw)



# JSON 响应内容
r.json()
# 原始响应内容
with open('request_read.txt', 'wb') as fd:
	for chunk in r.iter_content(200):
		fd.write(chunk)

# POST 请求
payload = {'key1': 'value1', 'key2': 'value2'}
payload = (('key1', 'value1'), ('key1', 'value2'))  #传入一个元组列表。在表单中多个元素使用同一 key 的时候
r = requests.post("http://httpbin.org/post", data=payload)
payload = {'some': 'data'}
r = requests.post(url, json=payload)
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r = requests.post(url, files=files)
print(r.text)

# 会话对象

s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)

# 方法级别的参数也不会被跨请求保持
r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# '{"cookies": {"from-my": "browser"}}'

r = s.get('http://httpbin.org/cookies')
print(r.text)
# '{"cookies": {}}'

#会话还可以用作前后文管理器：
with requests.Session() as s:
	s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

# 请求与响应对象
r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
r.headers
r.request.headers

# 准备的请求 (Prepared Request)
from requests import Request, Session
s = Session()
req = Request('GET',url,data = data ,headers = header)

prepared = req.prepare()
#
# prepared = req.prepare_request()

resp = s.send(prepared,stream = stream, verify = verify, proxies = proxies, cert = cert, timeout = timeout)
# 上述代码会失去 Requests Session 对象的一些优势， 尤其 Session 级别的状态，例如 cookie 就不会被应用到你的请求上去

# 要获取一个带有状态的 PreparedRequest， 请用 Session.prepare_request() 取代 Request.prepare() 的调用


# 事件挂钩
# 传递一个 {hook_name: callback_function} 字典给 hooks 请求参数

def print_url(r, *args, **kwargs):
	print(r.url)

requests.get(url, hooks=dict(response=print_url))

# 自定义身份验证
from requests.auth import AuthBase
class TokenAuth(AuthBase):
	"""docstring for TokenAuth"""
	def __init__(self, token):
		self.token = token

	def __call__(self,r):
		r.headers['Authorization'] = 'token ' + self.token
		return r
requests.get(url,auth=TokenAuth('44ecafe2e4832eb726fa142e85ad42cf5c958ba0'))















