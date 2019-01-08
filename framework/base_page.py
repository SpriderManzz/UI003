# coding=utf-8
import os
import time

class Base_Page(object):
    """封装selinumc常用方法"""
    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        return self.driver.get(url)

    def id_(self, id_):
        return self.driver.find_element_by_id(id_)

    def xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 浏览器前进操作
    def back(self):
        self.driver.forward()

    def get_page_title(self):
        return self.driver.title

    def close(self):
        return self.driver.close()


    # 截图并保存在根目录下的Screenshots文件夹下
    def take_screenshot(self):
        file_path = os.path.dirname(os.getcwd()) + '/screenshots/'
        rq = time.strftime('%Y-%m-%d %H %M %S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except Exception as e:
            pass







