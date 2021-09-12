#! /usr/bin/env python3

import re
import socket
import time
import sys

#url = 'neverssl.com/index.html'

# header from Burp suite

path = 'GET {} HTTP/1.1'
domain = 'Host: {}'
encoding = 'Accept-Encoding: identity'
others = 'Accept-Language: en-US\r\nConnection: close\r\n\r\n'

class pyreq():
  def __init__(self):
    self.name = 'pyref'
    self.domain = ''
    self.path = ''

  def geturl(self, url):
    a = re.search(r'com', url)
    self.domain = url[:a.end()]
    self.path = url[a.end():] if url[a.end():] else '/'
    d = domain.format(self.domain)
    p = path.format(self.path)
    self.req = '\r\n'.join([p, d, encoding, others])
    return self.req

if __name__ == '__main__':
  req = pyreq()

  if len(sys.argv) < 2:
    print('usage: pywget "url"')
    exit(0)

  url = sys.argv[1]
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
