# -*- coding:utf-8 -*-
import os.path
from configparser import ConfigParser
from selenium import webdriver


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    # def __init__(self, driver):
    #     self.driver = driver    # self.driver指向的是类BaiduSearch，因为传进来的是指向BaiduSearch类的cls

        # read the browser type from config.ini file, return the driver
    def open_browser(self):
        config = ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser_type = config.get("browserType", "browserName")  # browser_type = 配置文件的Firefox
        url = config.get("testServer", "URL")  # url = 配置文件的http://19v776387w.

        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Firefox
        :return: driver
        """
        if browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif browser_type == 'Chrome':
            driver = webdriver.Chrome()
        elif browser_type == 'IE':
            driver = webdriver.Ie()
        else:
            driver = webdriver.Firefox()
        driver.get(url)
        return driver  # 这里的return实际上就是火狐浏览器实例

    def quit_browser(self):
        """没有用到这个方法，日志也没输出"""
        self.driver.quit()
