"""
1、实现页面细节
2、优化测试用例
3、封装BasePage
"""
from selenium.webdriver.common.by import By

from test_wxweb.po.base_page import BasePage


class AddMemberPage(BasePage):
    _username_ele = (By.ID, "username")
    _useraccount_ele = (By.ID, "memberAdd_acctid")
    _userphone_ele = (By.ID, "memberAdd_phone")

    def add_member(self, name):
        """
        添加成员操作
        :return:
        """
        # 导入操作在方法内部，解决循环引用
        # *self.username_ele 解包元组
        from test_wxweb.po.contact_page import ContactPage
        self.find(*self._username_ele).send_keys(name)
        self.find(*self._useraccount_ele).send_keys("110")
        self.find(*self._userphone_ele).send_keys("13087672060")
        # 点击保存
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(base_driver=self.driver)

    def add_member_fail(self, name):
        from test_wxweb.po.contact_page import ContactPage
        # *self.username_ele 解包元组
        self.find(*self._username_ele).send_keys(name)
        self.find(*self._useraccount_ele).send_keys("110")
        self.find(*self._userphone_ele).send_keys("13087672060")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return ContactPage(base_driver=self.driver)
