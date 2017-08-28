#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-28 下午11:18
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : gevent协程socket并发服务端.py
# @Software: PyCharm


import sys
import socket
import time
import gevent

from gevent import socket, monkey

monkey.patch_all()


def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)


def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)

    except Exception as  ex:
        print(ex)
    finally:
        conn.close()


if __name__ == '__main__':
    server(8001)