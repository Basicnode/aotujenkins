# -*- coding: utf-8 -*-
# @Time : 2021/4/20 9:37
# @Author : XXXX
# @Email : XXXX@qq.com
# @File : test_aotujenks.py
import pytest
import allure

@pytest.mark.v2221
# @pytest.mark.usefixtures('test001')
@pytest.fixture(autouse=True)
# @pytest.fixture()
def test001():
    '''newtest workspace'''
    print("我是公共的",end=',')

def test004():
    print('---执行004---啦')

class TestCase:
    def test002(self):
        print("--hello,i know--")

    def test003(self,x='pears',y='nuts'):
        s = x + y
        print(s)
        assert 'u' in s


# if __name__ == '__main__':
# #     pytest.main(['-m','v001','-v', '-s'])
#     pytest.main(['-v', '-s'])