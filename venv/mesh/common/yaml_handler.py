# -*- coding: utf-8 -*-
# @Time : 2021/4/19 10:55
# @Author : XXXX
# @Email : XXXX@qq.com
# @File : __init__.py.py
import yaml


def read_yaml(fpath):
    with open(fpath, encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        print(data)
    return data
