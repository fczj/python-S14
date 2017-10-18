#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-10-13 下午2:46
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : myserver.py
# @Software: PyCharm


import socket
def handle_request(client):
    # buf = client.recv(1024)
    client.send(b'HTTP/1.1 200 ok\r\n\r\n')
    client.send(b'hello,world')
def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('192.168.1.166',8001))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        handle_request(conn)
        conn.close()
if __name__ == '__main__':
    main()
    print('d')