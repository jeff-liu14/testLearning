from appium.webdriver.common.mobileby import MobileBy

from test_app.page.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_contact(self, name, phonenum):
        self.find_and_sendkeys(MobileBy.XPATH,
                               "//*[contains(@text, '姓名')]/../*[@text='必填']",
                               name)

        self.find_and_sendkeys(MobileBy.XPATH,
                               "//*[contains(@text, '手机')]/..//*[@text='必填']",
                               phonenum)

        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

        from test_app.page.add_contact_page import AddContactPage
        return AddContactPage(self.driver)
