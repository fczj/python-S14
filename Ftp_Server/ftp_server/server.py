#!/usr/bin/env python
# encoding: utf-8

import os
import sys
pro_path = (os.path.abspath('./../'))
sys.path.append(pro_path)

import socketserver
import time
import json
import hashlib


class FtpServer():
    def __init__(self):
        self.tcp = ''
        self.pro_msg= {}            #协议信息
    def start(self,tcp):
        self.tcp = tcp.request
        while True:
            self.msg= json.loads(self.tcp.recv(1024).strip().decode())
            print("{} wrote:".format(tcp.client_address[0]))
            print('收到信息:',self.msg)
            self.tcp.sendall(b'OK')
            if hasattr(self,self.msg['action']):
                func = getattr(self,self.msg['action'])
                func()

    def send_msg(self):
        msg = self.pro_msg
        json_msg = json.dumps(msg).encode('utf8')
        print (json_msg)
        self.tcp.send(json_msg)
        server_ack = self.tcp.recv(1024)
        print (server_ack.decode())

    def file_md5(self,fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get(self):
        print ('客户端要下载文件:',self.msg['file_name'])
        print('发送协议信息')
        file_name = self.msg['file_name']
        if not os.path.isfile(file_name):
            self.pro_msg['is_exist'] = False
            self.send_msg()
            return
        self.pro_msg['is_exist'] = True
        self.pro_msg['file_size'] = os.stat(file_name).st_size
        self.pro_msg['file_md5'] = self.file_md5(file_name)
        self.send_msg()

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
            recive_data = self.tcp.recv(size)
            f.write(recive_data)
            recive_size += len(recive_data)
        f.close()

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        ftp = FtpServer()
        ftp.start(self)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9997
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.allow_reuse_address = True
    server.serve_forever()

