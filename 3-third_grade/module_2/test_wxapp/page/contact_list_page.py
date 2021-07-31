from test_app.page.add_contact_page import AddContactPage
from test_app.page.base_page import BasePage


class ContactListPage(BasePage):

    def click_add_contact(self, num):
        self.swipe_find('添加成员', num).click()
        return AddContactPage(self.driver)
