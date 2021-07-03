from selenium.webdriver.common.by import By

from test_wxweb.po.add_member_page import AddMemberPage
from test_wxweb.po.base_page import BasePage


class ContactPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        return AddMemberPage(base_driver=self.driver)

    def get_member_list(self):
        """
        获取成员列表
        :return: 返回用于断言的成员列表信息
        """
        ele = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = [i.text for i in ele]
        print(name_list)
        return name_list
