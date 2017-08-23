#!/usr/bin/env python
# encoding: utf-8

import os
import sys
pro_path = (os.path.abspath('./../'))
sys.path.append(pro_path)

import socketserver
import time
import json

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.msg= json.loads(self.request.recv(1024).strip().decode())
            print("{} wrote:".format(self.client_address[0]))
            self.request.sendall(b'OK')
            if hasattr(self,self.msg['action']):
                func = getattr(self,self.msg['action'])
                func()
    def put(self):
        print('客户端即将上传文件',self.msg['file_name'])
        file_name = os.path.basename(self.msg['file_name'])
        file_size = self.msg['file_size']
        recive_size = 0
        f = open(file_name,'wb')
        while recive_size < file_size:
            if (file_size - recive_size) < 1024:
                size = file_size - recive_size
            else:
                size = 1024
            recive_data = self.request.recv(size)
            f.write(recive_data)
            recive_size += len(recive_data)
        f.close()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.allow_reuse_address = True
    server.serve_forever()

