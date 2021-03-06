#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-29 上午9:56
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : select并发服务端.py
# @Software: PyCharm

import socket
import queue
from select import select

SERVER_IP = ('127.0.0.1', 9991)

# 保存客户端发送过来的消息,将消息放入队列中
message_queue = {}
#监测的列表
input_list = []
output_list = []

if __name__ == "__main__":
    server = socket.socket()
    server.bind(SERVER_IP)
    server.listen(10)
    # 设置为非阻塞
    server.setblocking(False)

    # 初始化将服务端加入监听列表
    input_list.append(server)

    while True:
        # 开始 select 监听,对input_list中的服务端server进行监听
        stdinput, stdoutput, stderr = select(input_list, output_list, input_list)
        #select(rlst,wlst,xlst)-->inputlst,outputlst,exception
        #程序读对应socket收到消息
        #程序写对应socket发消息

        #初始化的时候监听套接字,一旦server活动就有新链接--初始化
        #同时监测socket的一链接进来方向的异常--初始化

        #在监测到事件发生前,程序被select阻塞--重点理解


        # 循环判断是否有客户端连接进来,当有客户端连接进来时select将触发
        for obj in stdinput:
            # 判断当前触发的是不是服务端对象, 当触发的对象是服务端对象时,说明有新客户端连接进来了
            if obj == server:
                # 接收客户端的连接, 获取客户端对象和客户端地址信息
                conn, addr = server.accept()
                print("Client {0} connected! ".format(addr))
                # 将客户端对象也加入到监听的列表中, 当客户端发送消息时 select 将触发
                input_list.append(conn)
                # 为连接的客户端单独创建一个消息队列，用来保存客户端发送的消息
                message_queue[conn] = queue.Queue()

            else:
                # 由于客户端连接进来时服务端接收客户端连接请求，将客户端加入到了监听列表中(input_list)，客户端发送消息将触发
                # 所以判断是否是客户端对象触发
                try:
                    recv_data = obj.recv(1024)
                    # 客户端未断开
                    if recv_data:
                        print("received {0} from client {1}".format(recv_data.decode(), addr))
                        # 将收到的消息放入到各客户端的消息队列中
                        message_queue[obj].put(recv_data)

                        # 将回复操作放到output列表中，让select监听
                        if obj not in output_list:
                            output_list.append(obj)

                except ConnectionResetError:
                    # 客户端断开连接了，将客户端的监听从input列表中移除
                    input_list.remove(obj)
                    # 移除客户端对象的消息队列
                    del message_queue[obj]
                    print("\n[input] Client  {0} disconnected".format(addr))

                    # 如果现在没有客户端请求,也没有客户端发送消息时，开始对发送消息列表进行处理，是否需要发送消息
        for sendobj in output_list:
            try:
                # 如果消息队列中有消息,从消息队列中获取要发送的消息
                if not message_queue[sendobj].empty():
                    # 从该客户端对象的消息队列中获取要发送的消息
                    send_data = message_queue[sendobj].get()
                    print ('发送消息:',send_data)
                    sendobj.sendall(send_data)
                else:
                    # 将监听移除等待下一次客户端发送消息
                    output_list.remove(sendobj)

            except ConnectionResetError:
                # 客户端连接断开了
                del message_queue[sendobj]
                output_list.remove(sendobj)
                print("\n[output] Client  {0} disconnected".format(addr))