# coding=utf-8
import os
import ConfigParser
from selenium import webdriver


class BrowserEngine(object):
    """os.path.abspath('.') 获取的是 E:\UI003\framework
       os.path.dirname(os.path.abspath('.')) 获取的是E:\UI003
    """
    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def get_driver(self):
        config = ConfigParser.ConfigParser()
        config_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(config_path)

        browser_type = config.get("browserType", "browserName")    # browser_type = 配置文件的Firefox
        url = config.get("testServer", "URL")                      # url = 配置文件的http://19v776387w.iask.in:12648/scm/login

        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Firefox
        :return: driver
        """
        if browser_type == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser_type == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser_type == 'IE':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Firefox()

        return self.driver.get(url)


