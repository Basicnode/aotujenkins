import pytest
from web.common.driver_factory import Driver
from web.page.login_page import LoginPage
@pytest.fixture(autouse=True)
def login(driver):
    log = LoginPage(driver)
    log.open()
    log.login('testdy@service.aliyun.com','dingyang123')
    print('我是通用的，登录成功啦')

@pytest.fixture()
def driver():
    driver = Driver.get_driver()
    yield driver

    driver.close()
