"""
根据业务逻辑编写，添加断言
通过链式调用更加方便描述业务逻辑
"""
import pytest

from test_wxweb.po.main_page import MainPage


class TestAddMember:
    @pytest.mark.parametrize("name", ["测试账户1"])
    def test_add_member(self, name):
        main_page = MainPage()
        # 1、跳转到add member页面
        # 2、添加成员操作，点击保存跳转到通讯录页面
        # 3、在通讯录页面获取成员信息作为断言
        assert name in main_page.goto_add_member().add_member(name).get_member_list()

    @pytest.mark.parametrize("name", ["测试账户111"])
    def test_add_member_fail(self, name):
        main_page = MainPage()
        # 1、跳转到add member页面
        # 2、添加成员操作，点击保存跳转到通讯录页面
        # 3、在通讯录页面获取成员信息作为断言
        assert name not in main_page.goto_add_member().add_member_fail(name).get_member_list()
