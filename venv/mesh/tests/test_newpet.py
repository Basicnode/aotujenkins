# -*- coding: utf-8 -*-
# @Time : 2021/4/20 14:03
# @Author : XXXX
# @Email : XXXX@qq.com
# @File : test_newpet.py

import requests
import json
from faker import Faker,Factory
fake1 = Factory.create()
def testaddpet(self):
    headers = {"Content-Type":"application/json"}
    url = "https://petstore.swagger.io/v2/pet"
    data = {
        "id": fake1.random.randint(120,200),
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
            "name": "xitomg"
        }],
        "status": "available"
    }
    # method = post
    with requests.post(url=url,json=data)as res:
        # print(res.status_code)
        # print(res.text)
        d = json.loads(res.text)
        c =res.status_code
        assert c == 200
        # s = d['category']['name']
        assert (s in d)