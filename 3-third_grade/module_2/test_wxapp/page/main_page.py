from appium.webdriver.common.mobileby import MobileBy
from test_app.page.base_page import BasePage
from test_app.page.contact_list_page import ContactListPage


class MainPage(BasePage):
    _contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact_list(self):
        # click通讯录
        self.find_and_click(*self._contact_element)
        # 跳转到通讯录列表页
        return ContactListPage(self.driver)