#! /usr/bin/env python3

#import requests
import re
import struct

url = 'serenityos.org/happy/1st/'

# header from Burp suite

temp = 'GET {} HTTP/1.1\r\nHost: {}\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nConnection: close\r\n\r\n'

class pyreq():
	def __init__(self):
		self.name = 'pyref'

	def geturl(self, url):
		a = re.search(r'org', url)
		domain, path = url[:a.end()], url[a.end():]
		self.req = temp.format(path, domain)
		return self.req

if __name__ == '__main__':
	req = pyreq()
	a = req.geturl(url)
	with open('outh.bin', 'w') as f:
		f.write(a)



