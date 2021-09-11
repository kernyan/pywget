#! /usr/bin/env python3

#import requests
import re
import struct

url = 'serenityos.org/happy/1st/'

# header from Burp suite

path = 'GET {} HTTP/1.1'
domain = 'Host: {}'
cache_c = 'Cache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1'
user_a = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
others = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nConnection: close'

class pyreq():
	def __init__(self):
		self.name = 'pyref'

	def geturl(self, url):
		a = re.search(r'org', url)
		d = domain.format(url[:a.end()])
		p = path.format(url[a.end():])
		self.req = '\r\n'.join([p, d, cache_c, user_a, others]) + '\r\n\r\n'
		return self.req

if __name__ == '__main__':
	req = pyreq()
	a = req.geturl(url)



