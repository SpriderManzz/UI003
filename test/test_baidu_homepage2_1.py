# coding=utf-8
import unittest
from selenium import webdriver
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHome_Page
from framework.base_page import Base_Page

class BadiduHomePageTaseCse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserEngine(cls)
        cls.browser.open_browser()

    def test_print(self):
        print ("执行了测试方法")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main()

