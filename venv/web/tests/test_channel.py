import pytest
@pytest.mark.usefixtures('login')
class TestChannel:

    def test_add_channel_001(self):
        print('添加栏目成功啦')

    def test_add_channel_002(self):
        print('添加栏目失败啦')


if __name__ == '__main__':
    pytest.main(['-s'])