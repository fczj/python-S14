#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time    : 17-8-4 下午5:37
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 002.py
# @Software: PyCharm

'''
=================================================================
1.菜单选择程序
2.用户传入一个字段，需要最后一层为列表,并需要告诉菜单的层数
2.可以后退也可以回到第一层
3.选择完成后打印完整的选择
=================================================================
'''


class Menu():
    def __init__(self):
        self.init_menu()
        self.stack = []
        self.print_menu = []
        self.is_done = False
        self.choose = ''

    def init_menu(self):
        self.menu = {
            '中国': {
                '河北': {'石家庄': ['长安区', '桥东区']},
                '山西': {'太原': ['阳曲县', '清徐县']},
            },
            'USA': {
                'Alaska': {'A': ['A1', 'A2']},
                'Florida': {'B': ['B1', 'B2']},
            },
        }
        self.layer = 4

    def select_one_item_from_list(self):
        self.print_menu.append('back')
        self.print_menu.append('first')
        for num,value in enumerate(self.print_menu):
            print ('{}:{}'.format(num,value))
        in_num = int(input('psl input you choose:'))
        return in_num

    def get_item_from_dict_uselist(self):
        if len(self.stack) == 0:
            return self.menu
        else:
            local_stack = self.stack[:]
        temp = None
        while len(local_stack) >0:
            if temp is None:
                temp = self.menu.get(local_stack[0])
            else:
                temp = temp.get(local_stack[0])
            local_stack.pop(0)
        return temp
    def start(self):
        while not self.is_done:
            self.print_menu = self.get_item_from_dict_uselist()
            if type(self.print_menu) == dict:
                self.print_menu = list(self.print_menu.keys())
            num = self.select_one_item_from_list()
            if self.print_menu[num] == 'back':
                if len(self.stack) > 0:
                    self.stack.pop(-1)
                continue
            if self.print_menu[num] == 'first':
                self.stack = []
                continue
            if len(self.stack) == self.layer - 1:
                self.choose = self.print_menu[num]
                self.is_done = True
                break
            else:
                self.stack.append(self.print_menu[num])

a = Menu()
a.start()
print('-->'.join(a.stack)+'-->'+a.choose)
