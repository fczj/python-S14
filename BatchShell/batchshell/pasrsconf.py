#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午4:58
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : pasrsconf.py
# @Software: PyCharm


import yaml
import io

# Define data
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}

# Write YAML file
with io.open('data.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True,indent=4)

# Read YAML file
with open("data.yaml", 'r') as stream:
    data_loaded = yaml.load(stream)

print(data == data_loaded)

