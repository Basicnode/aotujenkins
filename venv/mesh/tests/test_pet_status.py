# -*- coding: utf-8 -*-
# @Time : 2021/4/21 11:29
# @Author : XXXX
# @Email : XXXX@qq.com
# @File : test_petstatus.py

import requests
# import json
from faker import Faker, Factory
fake1 = Factory.create()
from requests.packages import urllib3
urllib3.disable_warnings()
from mesh.middleware.handler import Handler

def testpetstatus():
    headers = {"Content-Type": "application/json",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
    payload = {"status": ["available"]}
    env_url = Handler.env_config['env_url']
    url = env_url + "pet/findByStatus"

    with requests.get(url, params=payload,headers=headers, verify=False)as res:
        print(res.status_code)
        assert res.status_code == 200


if __name__ == '__main__':
    testpetstatus()