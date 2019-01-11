# coding=utf-8
import unittest
from selenium import webdriver

from pageobjects.baidu_homepage import BaiduHome_Page
from framework.base_page import Base_Page

class BadiduHomePage(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Firefox()  # 创建一个火狐浏览器实例

    def test_baidu_search(self):
        baiduhomepage = BaiduHome_Page(self.driver)
        baiduhomepage.get("https://www.baidu.com/")
        baiduhomepage.type_search('selenium')  # 调用页面对象中的方法
        baiduhomepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        try:
            assert 'selenium' in baiduhomepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()




