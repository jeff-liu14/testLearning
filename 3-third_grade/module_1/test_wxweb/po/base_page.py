from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    """
    BasePage提供公共方法的封装，即和页面逻辑无关的封装
    比如解决driver初始化的问题
    """
    # 添加base_url，可以支持测试用例灵活起始页
    # basepage完全与业务解耦
    _base_url = ""

    def __init__(self, base_driver=None):
        if base_driver is None:
            # chromdriver地址
            chrome_address = "/Users/moment/software/chromedriver"
            # 通过remote 复用浏览器操作
            chrom_arg = webdriver.ChromeOptions()
            # 加入调试地址
            # mac 启动调试方式 /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome -remote-debugging-port=9222
            chrom_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=chrom_arg, executable_path=chrome_address)
            # 打开首页
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.get(self._base_url)
            # 添加隐式等待
            self.driver.implicitly_wait(3)
        else:
            # 将self.driver 添加一个WebDriver对象注解，解决类型提示问题
            self.driver: WebDriver = base_driver

    def find(self, by, locator=None):
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=locator)
