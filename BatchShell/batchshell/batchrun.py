#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-26 下午10:08
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : batchrun.py
# @Software: PyCharm


import paramiko
from multiprocessing import Process,Pool,Lock
import yaml
import argparse
import sys
import time




GROUP_CONF = './../conf/group_conf'
HOST_CONF = './../conf/host_conf'

class Conf():
    def __init__(self):
        with open(GROUP_CONF,'r') as f:
            self.groups = yaml.load(f)
        with open(HOST_CONF,'r') as f:
            self.hosts= yaml.load(f)
        self.all_group = self.groups.keys()

    def get_host(self,host_name):
        return self.hosts[host_name]

    def get_group_all_host(self,group_name):
        return self.groups.get(group_name)


class RunCmd():
    def __init__(self,user,host,password,port=22):
        self.user = user
        self.port = port
        self.host = host
        self.password = password

    def run_cmd(self,cmd):
        print ('='*80)
        print ('{}:'.format(self.host))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host, port=self.port,
                    username=self.user,password=self.password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        res,err = stdout.read(),stderr.read()
        result = res if res else err
        ssh.close()
        print(result.decode())


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", "--hostname", nargs='*',dest="host", help="hostname")
    parser.add_argument("-g", "--group", nargs='*',dest="group", help="groupname")
    parser.add_argument("-cmd", "--command", dest="cmd", help="command")
    parser.add_argument("-a", "--action", dest="action", help="action")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    conf = Conf()
    args = parse()
    all_host = []
    if args.host is not None:
        all_host = args.host
    if args.group is not  None:
        groups = args.group
        for i in groups:
            hosts = conf.get_group_all_host(i)
            all_host.extend(hosts)
    if args.host is None and args.group is None:
        print ('没有可操作对象')
        sys.exit(9)

    all_host = list(set(all_host))
    cmd = args.cmd

    pool = Pool(5)
    lock = Lock()
    for host in all_host:
        lock.acquire()
        conn_info = conf.get_host(host)
        cmd_obj = RunCmd(**conn_info)
        pool.apply_async(func=cmd_obj.run_cmd, args=(cmd,))
        lock.release()
    pool.close()
    pool.join()


