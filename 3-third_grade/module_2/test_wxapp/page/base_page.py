import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, value):
        logging.info("find")
        logging.info(by)
        logging.info(value)
        # 查找
        return self.driver.find_element(by, value)

    def find_and_click(self, by, value):
        logging.info("find_and_click")
        self.find(by, value).click()

    def find_and_sendkeys(self, by, value, text):
        logging.info("find_and_sendkeys")
        logging.info(by)
        logging.info(value)
        logging.info(text)
        self.find(by, value).send_keys(text)

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return result

    def back(self, num=5):
        for i in range(num):
            self.driver.back()

    def swipe_find(self, text, num=5):
        for i in range(num):
            if i == num - 1:
                raise NoSuchElementException(f"找了{num - 1} 次，未找到")
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                return element
            except:
                print(f"未找到{text}")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.2

                duration = 200

                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
