#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import socket
pro_path = (os.path.abspath('./../'))
sys.path.append(pro_path)
import json
import hashlib
from tqdm import tqdm
import time

HOST, PORT = "localhost", 9994          #服务器配置


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
        print('接受文件:',file_info)
        file_name = os.path.basename(file_info['file_name'])
        file_size = file_info['file_size']
        file_md5 = file_info['file_md5']
        recive_size = 0
        pbar = tqdm(total=file_size,unit='bytes')
        with open(file_name,'wb') as f:
            while recive_size < file_size:
                if file_size - recive_size < 1024:
                    size = file_size - recive_size
                else:
                    size = 1024
                recive_data = self.sock.recv(size)
                recive_size += len(recive_data)
                pbar.update(size)
                f.write(recive_data)
        pbar.close()
        time.sleep(1)                   #由于进度条还没有打完就会输出其他,所以这儿睡眠1秒
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

class FtpClient(FtpBase):
    def __init__(self):
        self.sock = socket.socket()
        self.sock.connect((HOST,PORT))
        self.msg = {}
        self.all_cmd = ['ls','pwd','cd','ifconfig']

    def put(self,*args):
        put_file = args[0][0]
        if not os.path.isfile(put_file):
            print ('{} is not exsits'.format(put_file))
            return
        self.msg = {}
        self.msg['file_size']   = os.stat(put_file).st_size
        self.msg['action']      = 'put'
        self.msg['file_name']   = put_file
        self.msg['file_md5']    = self.file_md5(put_file)

        #发送文件信息
        self.send_msg(self.msg)
        self.recive_ack()

        #开始发送文件
        self.send_file(self.msg)

    def get(self,*args):
        self.msg = {}
        self.msg['file_name']   = args[0][0]
        self.msg['action']      = 'get'
        self.send_msg(self.msg)
        self.recive_ack()
        self.send_ack('OK')
        #接受文件信息
        file_info = self.recive_msg()
        self.send_ack(file_info)
        self.recive_file(file_info)
    def run_cmd(self,cmd):
        msg = {}
        msg['action'] = 'run_cmd'
        msg['run_cmd'] = cmd
        self.send_msg(msg)
        self.recive_ack()
        self.send_ack('准备接受命令执行结果')
        print (self.recive_msg())


    def inactive(self):
        while True:
            user_input = input('>>:')
            cmd,*args = user_input.split(' ')
            if hasattr(self,cmd):
                func = getattr(self,cmd)
                func(args)
            elif cmd in self.all_cmd:
                self.run_cmd(user_input)
            else:
                print ('{} command is not exists'.format(cmd))

if __name__ == "__main__":
    ftp = FtpClient()
    ftp.inactive()

