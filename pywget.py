#! /usr/bin/env python3

#import requests
import re
import socket
import time

url = 'neverssl.com/index.html'

# header from Burp suite

path = 'GET {} HTTP/1.1'
domain = 'Host: {}'
cache_c = 'Cache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1'
user_a = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
others = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
#encoding = 'Accept-Encoding: gzip, deflate'
encoding = 'Accept-Encoding: identity'
others2 = 'Accept-Language: en-US,en;q=0.9\r\nConnection: close\r\n\r\n'

class pyreq():
	def __init__(self):
		self.name = 'pyref'
		self.domain = ''
		self.path = ''

	def geturl(self, url):
		a = re.search(r'com', url)
		self.domain = url[:a.end()]
		self.path = url[a.end():]
		d = domain.format(self.domain)
		p = path.format(self.path)
		self.req = '\r\n'.join([p, d, cache_c, user_a, others, encoding, others2])
		return self.req

if __name__ == '__main__':
	req = pyreq()
	a = req.geturl(url)

	ai = socket.getaddrinfo(req.domain, 80, 
		family=socket.AF_INET, 
		type=socket.SOCK_STREAM,
		proto=socket.IPPROTO_TCP)

	if len(ai) == 0:
		print('no valid address info for {}'.format(url))
		exit(-1)

	af, socktype, proto, cannonname, sa = ai[0]

	s = socket.socket(af, socktype, proto)
	s.connect(sa)

	s.send(str.encode(a))

	response = ''
	in_chunk = ''

	while True:
		in_chunk = s.recv(10000).decode('utf-8')
		if not in_chunk:
			break
		response += in_chunk

	a = re.search(r'\r\n\r\n', response)
	print(response[a.end():-1])

