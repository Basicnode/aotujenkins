# -*- coding: utf-8 -*-
# @Time : 2021/4/19 10:55
# @Author : XXXX
# @Email : XXXX@qq.com
# @File : __init__.py.py
"""路径"""

import os

# 动态获取路径
config_path = os.path.dirname(os.path.abspath(__file__))

# 获取项目根目录
root_path = os.path.dirname(config_path)

