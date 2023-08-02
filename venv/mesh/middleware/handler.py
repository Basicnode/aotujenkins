# -*- coding: utf-8 -*-
# @Time : 2021/4/21 11:29
# @Author : XXXX
# @Email : XXXX@qq.com
# @File : test_petstatus.py
import datetime
import os, re
import time, random
from mesh.common.yaml_handler import read_yaml
from mesh.config import path

# class MidMySQLHandler(MySQLHandler):
#     """连接MySQL数据库"""
#
#     def __init__(self):
#         mysql_path = os.path.join(path.config_path, 'mysql_config.yaml')
#         mysql_config = read_yaml(mysql_path)
#
#         super().__init__(host=mysql_config['db']['host'],
#                          port=mysql_config['db']['port'],
#                          user=mysql_config['db']['user'],
#                          password=mysql_config['db']['password'],
#                          charset=mysql_config['db']['charset'],
#                          # 指定数据库
#                          database=mysql_config['db']['database'],
#                          cursorclass=DictCursor)
#
#
# class MidOracleHandler(OracleHandler):
#     """连接Oracle数据库"""
#
#     def __init__(self):
#         oracle_path = os.path.join(path.config_path, 'oracle_config.yaml')
#         oracle_config = read_yaml(oracle_path)
#         super().__init__(host=oracle_config['db']['host'],
#                          port=oracle_config['db']['port'],
#                          user=oracle_config['db']['user'],
#                          password=oracle_config['db']['password'],
#                          # 指定数据库
#                          database=oracle_config['db']['database'])


class Handler():
    """任务：中间层。 common 和 调用层。
    使用项目的配置数据，填充common模块
    """
    # 环境信息
    env_path = os.path.join(path.config_path, 'env_config.yaml')
    env_config = read_yaml(env_path)

    """
    # 用户信息
    user_path = os.path.join(path.config_path, 'user_config.yaml')
    user_config = read_yaml(user_path)
    # mysql
    mysql_path = os.path.join(path.config_path, 'mysql_config.yaml')
    mysql_config = read_yaml(mysql_path)

    # excel对象-所有接口
    excel_file = os.path.join(path.data_path, 'case_datas.xlsx')
    excel = ExcelHandler(excel_file)

    # excel对象-场景接口
    scene_api_excel_file = os.path.join(path.data_path, 'scene_case_datas.xlsx')
    scene_api_excel = ExcelHandler(scene_api_excel_file)

    # 上传文件路径
    upload_files_path = os.path.join(path.root_path, 'upload_files')

    # 场景用例上传文件路径
    upload_scena_files_path = os.path.join(path.root_path, 'upload_scena_files')

    # MySQL数据库
    # db_class = MidMySQLHandler()

    # 需要动态替换#...# 的数据
    before_day = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")  # 昨天
    now_day = datetime.datetime.now().strftime("%Y-%m-%d")  # 今天
    next_day = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d")  # 明天
    week_day = (datetime.datetime.now() + datetime.timedelta(days=-6)).strftime("%Y-%m-%d")  # 近一周
    month_day = (datetime.datetime.now() + datetime.timedelta(days=-28)).strftime("%Y-%m-%d")  # 近一月
    random_number = random.randint(1000000000, 9999999999)  # 生成随机数

    now_time_stamp = int(time.time())  # 获取当前时间戳，单位：秒
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间
    # P组
    p_numbering = "P-87104"  # P组用户-位号
    p_doc_category_numbers = "D01_炉类采购文档"  # P组用户-分类号
    p_doc_workflow_null = "D02_塔类采购文档"  # P组用户-分类号不存在审批流
    p_category_names = "柱塞泵"  # P组用户-工厂对象分类名称

    # E组/C组
    e_c_numbering = "F-87104"  # E组/C组用户-位号
    e_c_category_names = "管道过滤器"  # E组/C组用户-工厂对象分类名称

    @classmethod
    def replace_data(cls, string, pattern='#(.*?)#'):
    
        '''数据动态替换'''
        # pattern = '#(.*?)#'
        results = re.finditer(pattern=pattern, string=string)
        for result in results:
            old = result.group()
            key = result.group(1)
            new = str(getattr(cls, key, ''))
            string = string.replace(old, new)
        return string
    """
    
handle = Handler()