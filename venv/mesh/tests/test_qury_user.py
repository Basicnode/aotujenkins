# -*- coding: utf-8 -*-
# @Time : 2021/4/21 11:29
# @Author : XXXX
# @Email : XXXX@qq.com
# @File : test_petstatus.py
import json
import requests
from faker import Faker, Factory
fake1 = Factory.create()
from requests.packages import urllib3
urllib3.disable_warnings()
from jsonpath import jsonpath
import urllib.parse
from mesh.middleware.handler import Handler

def test_queruser():
    headers = {
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
    payload = "亮黄"
    chinese_str_url = urllib.parse.quote(payload)
    env_url = Handler.env_config['env_url']
    url =  env_url+ f'user/{chinese_str_url}'
    with requests.get(url,headers=headers, verify=False)as res:
        print(res.status_code)
        print(res.text)
        obj = json.loads(res.text)
        email = jsonpath(obj, '$.email')
        firstName = jsonpath(obj,'$.firstName')
        assert res.status_code == 200
        assert email[0] == "fang59@hotmail.com"
        assert firstName[0] == "斌"



if __name__ == '__main__':
    test_queruser()