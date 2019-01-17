# coding=utf-8
import unittest
from selenium import webdriver
from  framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHome_Page
from framework.base_page import Base_Page

class BadiduHomePageTaseCse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        browser.open_browser()

    # def test_baidu_search(self):
    #
    #     self.baiduhomepage.type_search('selenium')  # 调用页面对象中的方法,传了一个参数，然后
    #     # type_search再调用type方法，传了2个参数input_box元素的定位和元素的值，type再调find_element方法传递元素的定位
    #     self.baiduhomepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
    #
    #     try:
    #         assert 'selenium' in self.baiduhomepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
    #         print('Test Pass.')
    #     except Exception as e:
    #         print('Test Fail.', format(e))
    #
    # def test_title(self):
    #     """验证搜索标题是否正确"""
    #     try:
    #         assert u'selenium_百度搜索' in self.baiduhomepage.get_page_title()
    #         print('Test Pass.')
    #     except Exception as e:
    #         print('Test Fail.', format(e))

    def test_print(self):
        print ("测试test_print")


    @classmethod
    def tearDownClass(cls):
        cls.baiduhomepage.close()

suite = unittest.TestSuite()
suite.addTest(BadiduHomePageTaseCse("test_baidu_search"))
suite.addTest(BadiduHomePageTaseCse("test_title"))

if __name__ == '__main__':
    unittest.main()
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)




