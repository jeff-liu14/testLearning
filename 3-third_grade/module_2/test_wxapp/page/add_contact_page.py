from appium.webdriver.common.mobileby import MobileBy

from test_app.page.base_page import BasePage


class AddContactPage(BasePage):

    def click_addmember_menual(self):
        from test_app.page.edit_member_page import EditMemberPage
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return EditMemberPage(self.driver)

    def get_result(self):
        result = self.get_toast_text()
        return result