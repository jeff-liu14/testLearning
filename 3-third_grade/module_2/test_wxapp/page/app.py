import logging

from appium import webdriver

from test_app.page.base_page import BasePage
from test_app.page.main_page import MainPage

# App.py  负责 app的启动，重启，关闭，进入主页等操作
class App(BasePage):
    def start(self):
        if self.driver == None:
            logging.info("driver ==None 创建一个新的driver")
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "emulator-5554"
            caps["noReset"] = "true"
            # 提升自动化测试启动速度的
            caps['skipServerInstallation'] = 'true'
            caps['skipDeviceInitialization'] = 'true'
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            logging.info("复用driver")
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)
