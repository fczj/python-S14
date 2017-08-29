#!/usr/bin/env python
# encoding: utf-8

import os
import sys
pro_path = (os.path.abspath('./../'))
pro_path = (os.path.abspath('./'))
sys.path.append(pro_path)

import socketserver
import time
import json
import hashlib
from tqdm import tqdm

HOST, PORT = "localhost", 9994

class FtpBase():
    #def __init__(self,sock):
    #    self.sock = sock
    #继承者需要设置self.sock变量

    def file_md5(self,fname):
        '''
        获取文件的md5值
        '''
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def send_file(self,file_info):
        '''
        :param file_info:           #要发送的文件
        :return:
        '''
        file_name = file_info['file_name']
        with open(file_name,'rb') as f:
            for block in iter(lambda :f.read(4096),b''):
                self.sock.send(block)
        print ('发送文件{}完成'.format(file_name))

    def recive_file(self,file_info):
        file_name = os.path.basename(file_info['file_name'])
        file_size = file_info['file_size']
        file_md5 = file_info['file_md5']
        recive_size = 0
        with open(file_name,'wb') as f:
            while recive_size < file_size:
                if file_size - recive_size < 1024:
                    size = file_size - recive_size
                else:
                    size = 1024
                recive_data = self.sock.recv(size)
                recive_size += len(recive_data)
                f.write(recive_data)
        if self.file_md5(file_name) == file_md5:
            print('接收完成完成,并且md5正确')

    def send_msg(self,msg):
        '''
        发送消息
        :param msg:   #消息为字典
        :return:
        '''
        json_msg = json.dumps(msg).encode('utf8')
        self.sock.send(json_msg)
        print ('发送消息:',msg)

    def recive_msg(self):
        '''
        接受并返回字典格式消息
        '''
        recive_data = self.sock.recv(1024)
        json_msg = json.loads(recive_data.decode('utf8'))
        print ('收到消息:',json_msg)
        return json_msg

    def send_ack(self,msg):
        '''
        发送接受到msg消息的ack
        :param msg:
        :return:
        '''
        ack_str = 'i have recive msg:'+str(msg)
        self.sock.send(ack_str.encode('utf8'))

    def recive_ack(self):
        recive_ack = self.sock.recv(1024).decode('utf8')
        print ('recive ack:'+recive_ack)

class FtpServer(FtpBase):
    def __init__(self):
        self.tcp = ''
        self.msg = {}

    def start(self,tcp):
        self.sock= tcp.request
        while True:
            print ('开始接受命令:')
            recive_msg = self.recive_msg()
            if hasattr(self,recive_msg['action']):
                func = getattr(self,recive_msg['action'])
                self.send_ack(recive_msg)
                func(recive_msg)
            else:
                print ('没有此操作')
    def get(self,recive_msg):
        #发送文件信息
        file_info = {}
        f_name = recive_msg['file_name']
        file_info['file_name'] = f_name
        file_info['file_size'] = os.stat(f_name).st_size
        file_info['file_md5'] = self.file_md5(f_name)
        self.recive_ack()
        self.send_msg(file_info)
        self.recive_ack()
        #发送文件收到消息: {'run_cmd': 'ls', 'action': 'run_cmd'}
        self.send_file(file_info)

    def put(self,recive_msg):
        f_name = os.path.basename(recive_msg['file_name'])
        file_info = recive_msg
        file_info['file_name'] = f_name
        self.recive_file(file_info)

    def run_cmd(self,recive_msg):
        result = os.popen(recive_msg['run_cmd']).read()
        print (result)
        self.recive_ack()
        self.send_msg(result)


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        ftp = FtpServer()
        ftp.start(self)

if __name__ == "__main__":
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()

