# coding=utf-8
import os
import time
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
from selenium import webdriver

config = configparser.ConfigParser()
config_path = os.path.dirname(os.path.abspath('.')) + '/config/config.conf'
config.read(config_path)


class BrowserEngine(object):
    def __init__(self):
        browser_type = config.get("browserType", "browserName")  # browser_type = 配置文件的Firefox
        self.driver = getattr(webdriver, browser_type)()

    # read the browser type from config.conf file, return the driver
    def open_browser(self):
        url = config.get("testServer", "URL")                      # url = 配置文件的http://19v776387w.iask.in:12648/scm/login

        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Firefox
        :return: driver
        """
        self.driver.get(url)
        time.sleep(5)

        # return self.driver 思考有没有必要return， 根据业务逻辑


b = BrowserEngine()
b.open_browser()