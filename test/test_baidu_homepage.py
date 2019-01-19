# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHome_Page
from framework.base_page import Base_Page


class BaiduHomePageTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUpClass()的代码，主要是测试的前提准备工作
        """
        browser = BrowserEngine()  # browse就是BrowserEngine类的一个实例
        cls.driver = browser.open_browser()  # 将open_browser方法返回值driver（浏览器实例），赋值给cls.driver
        
    def test_print(self):
        print ("执行了测试方法")


    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

if __name__ == '__main__':
    unittest.main()

