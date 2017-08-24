#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import socket
pro_path = (os.path.abspath('./../'))
sys.path.append(pro_path)
import json


HOST, PORT = "localhost", 9997          #服务器配置


class FtpClient():
    def __init__(self):
        self.sock = socket.socket()
        self.sock.connect((HOST,PORT))
        self.msg = {}

    def send_msg(self):
        json_msg = json.dumps(self.msg).encode('utf8')
        print (json_msg)
        self.sock.send(json_msg)
        server_ack = self.sock.recv(1024)
        print (server_ack.decode())

    def recive_msg(self):
        msg= json.loads(self.sock.recv(1024).strip().decode())
        return msg


    def put(self,*args):
        put_file = args[0][0]
        if not os.path.isfile(put_file):
            print ('{} is not exsits'.format(put_file))
            return
        self.msg = {}
        self.msg['file_size']   = os.stat(put_file).st_size
        self.msg['action']      = 'put'
        self.msg['file_name']   = put_file

        self.send_msg()
        with open(put_file,'rb') as f:
            for block in iter(lambda :f.read(4096),b''):
                self.sock.send(block)

    def get(self,*args):
        self.msg = {}
        self.msg['file_name']   = args[0][0]
        self.msg['action']      = 'get'
        self.send_msg()
        msg = self.recive_msg()
        print (msg)

    def inactive(self):
        while True:
            user_input = input('>>:')
            cmd,*args = user_input.split(' ')
            if hasattr(self,cmd):
                func = getattr(self,cmd)
                func(args)
            else:
                print ('{} command is not exists'.format(cmd))

if __name__ == "__main__":
    ftp = FtpClient()
    ftp.inactive()


'''
#上传下载功能:
1.客户端输入命令-put
2.客户端发送上传文件信息告诉服务器
3.服务端接受到以后,回复ack
4.客户端开始上传文件
5.完了服务端判断正确性,并发送信息給客户端
6.客户端接受完成信息
'''
