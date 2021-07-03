"""
编码第一步：构造PO模型，实现设置为空
构造页面相关类和方法
时序图紫色方块代表一个类
每条线代表这个页面提供的操作
箭头的末端为跳转页面，即对应的方法需要返回跳转页面的实例对象
实现暂时设置为空
"""
from selenium.webdriver.common.by import By

from test_wxweb.po.add_member_page import AddMemberPage
from test_wxweb.po.base_page import BasePage
from test_wxweb.po.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        """
        跳转通讯录页面
        :return: 返回通讯录页面的实例对象
        """
        return ContactPage(base_driver=self.driver)

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        # 子类调用父类成员变量
        # 点击添加成员
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()

        return AddMemberPage(base_driver=self.driver)
