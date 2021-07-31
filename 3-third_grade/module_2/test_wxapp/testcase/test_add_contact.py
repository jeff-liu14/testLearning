from faker import Faker

from test_app.page.app import App


class TestContact:
    def setup_class(self):
        self.app = App()
        self.fake = Faker('zh_CN')

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    def test_add_contact(self):
        for i in range(50):
            name = self.fake.name()
            phonenum = self.fake.phone_number()
            result = self.main.goto_contact_list() \
                .click_add_contact(100) \
                .click_addmember_menual() \
                .edit_contact(name, phonenum) \
                .get_result()
            self.app.back(1)
        assert result == '添加成功'

    # def test_add_contact1(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
    #
    # def test_add_contact2(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
    #
    # def test_add_contact3(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
    #
    # def test_add_contact4(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
    #
    # def test_add_contact5(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
    #
    # def test_add_contact6(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
    #
    # def test_add_contact7(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
    #
    # def test_add_contact8(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
    #
    # def test_add_contact9(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
    #
    # def test_add_contact10(self):
    #     name = self.fake.name()
    #     phonenum = self.fake.phone_number()
    #
    #     result = self.main.goto_contact_list() \
    #         .click_add_contact() \
    #         .click_addmember_menual() \
    #         .edit_contact(name, phonenum) \
    #         .get_result()
    #     assert result == '添加成功'
