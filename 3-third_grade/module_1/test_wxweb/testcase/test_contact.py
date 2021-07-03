from test_wxweb.po.contact_page import ContactPage


class TestContact:
    def test_contact(self):
        contact = ContactPage()
        contact.goto_add_member()
