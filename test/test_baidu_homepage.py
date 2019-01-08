# coding=utf-8
import unittest
from selenium import webdriver
from pageobjects.baidu_homepage import Baidu_Homepage

class BadiduHomePage(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Firefox()  # 创建一个火狐浏览器实例
        self.page = Baidu_Homepage(self.dr)

    def test_search_title(self):
        self.page.get("https://www.baidu.com/")
        self.page.search_box.send_keys("selenium")
        self.page.search_button.click()



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()




