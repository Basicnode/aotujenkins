# -*- coding: utf-8 -*-
# @Time : 2021/4/20 14:03
# @Author : XXXX
# @Email : XXXX@qq.com
# @File : test_newpet.py

import requests
import json
from faker import Faker,Factory
fake1 = Factory.create()
from mesh.middleware.handler import Handler
from requests.packages import urllib3
urllib3.disable_warnings()

def testaddpet():
    headers = {"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
    env_url = Handler.env_config['env_url']
    url = env_url + "pet"
    data = {
        "id": fake1.random.randint(120,210),
        "category": {
            "id": 0,
            "name": fake1.name()
        },
        "name": fake1.name(),
        "photoUrls": [
            "string"
        ],
        "tags": [{
            "id": 0,
            "name": "malitomg"
        }],
        "status": "available"
    }

    with requests.post(url=url,headers=headers,json=data,verify=False)as res:
        print(res.status_code)
        print(res.text)
        # d = json.loads(res.text).get('id')
        d = json.loads(res.text).get('category')['name']
        print(d)
        assert res.status_code == 200
    # d = json.loads(res.text)
    # c =res.status_code
    # assert c == 200
    # s = d['category']['name']
    # assert (s in d)
if __name__ == '__main__':
    testaddpet()
