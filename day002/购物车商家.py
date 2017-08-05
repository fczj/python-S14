#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-5 下午3:38
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : 购物车商家.py
# @Software: PyCharm


class Seller():
    def __init__(self):
        self.is_exit = False
        self.main_menu = ['list','add','delete','exit']
        self.choose_menu = ''
        self.goods = {}
        self.load_goods()

    def print_main_menu(self):
        for k,v in enumerate(self.main_menu):
            print (k,v)
        self.choose_menu = int(input('pls input you choose:'))

    def load_goods(self):
        with open('./goods','r') as f:
            for line in f:
                [k,v] = line.strip().split(':')
                self.goods[k] = v

    def save_goods(self):
        w_str = ''
        for k,v in self.goods.items():
            w_str += k+':'+v+'\n'
        with open('./goods','w') as f:
            f.write(w_str)

    def add_goods(self):
        goods_name = input('pls input goods name:')
        goods_price = input('pls input goods price:')
        self.goods[goods_name] = '$'+goods_price
        self.save_goods()


    def print_list_and_select_one(self):
        menu = list(self.goods.keys())
        for num,value in enumerate(menu):
            print('{}:{}'.format(num,value))

        in_num = int(input('pls input you choose:'))
        return menu[in_num]


    def start(self):
        while not self.is_exit:
            self.load_goods()
            self.print_main_menu()
            if self.main_menu[self.choose_menu] == 'exit':
                self.is_exit = True
                break
            if self.main_menu[self.choose_menu] == 'list':
                self.load_goods()
                print ('#'*80)
                print ('商品：价格')
                for k,v in self.goods.items():
                    print ('{}:{}'.format(k,v))
                print ('#'*80)
                continue
            if self.main_menu[self.choose_menu] == 'delete':
                choose = self.print_list_and_select_one()
                self.goods.pop(choose)
                self.save_goods()
            if self.main_menu[self.choose_menu] == 'add':
                self.add_goods()
a = Seller()
a.start()
