# fixture--测试夹具
import pytest
from web.page.login_page import LoginPage
# @pytest.fixture(autouse=True,scope='function')
class TestLogin:
    # @pytest.fixture(autouse=True, scope='function')
    def test_login_success(self,driver):
        login = LoginPage(driver=driver)
        # login.login('admin','huice')
        login.login('testdy@service.aliyun.com','dingyang123')
        # 写检查点


# @pytest.fixture(autouse=True,scope='function')
# def login():
#     print('我登录成功啦')
#
# # 调用测试夹具方式一
# def test_001(login):
#     print('执行到001啦')

# # 调用测试夹具方式二
# @pytest.mark.usefixtures('login')
# def test_002():
#     print('执行到002啦')
#
# # 调用测试夹具当时三
# def test_003():
#     print('执行到003啦')


if __name__ == '__main__':
    pytest.main(['-s'])