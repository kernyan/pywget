# pywget
wget in python using as low-level syscall as possible. Practically useless, just for educational purpose

## restrictions
- tcp only
- no ssl
- no gzip decompression

## outline
1. get available target ip, port, protocol (UDP, TCP), family (IPv4, IPv6)
  underlying syscall - man 3 getaddrinfo
2. open socket with parameters
  underlying syscall - man 2 connect
3. send header to socket
  underlying syscall - write to socket file descriptor - man 2 write (or sendto)
4. keep receiving until no new TCP transmission from server
  underlying syscall - read from socket file descriptor - man 2 read (or recvfrom)

## header format
        GET /chat HTTP/1.1
        Host: server.example.com
        Accept-Encoding: identity
        Accept-Language: en-US
        Connection: close

## run test
compares wget "neverssl.com" output with pywget "neverssl.com"

```bash
./go.sh
```
