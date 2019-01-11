# coding=utf-8
import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException



class Base_Page(object):
    """封装selinumc常用方法"""
    def __init__(self, driver):
        self.driver = driver

    def type(self, selector, text):
        el = self.find_element(selector)
        el.send_keys(text)

    def find_element(self, selector):
        """根据selector才获取元素"""
        selector_by = selector.split('=>')[0]  # 取的是=>左边的值
        selector_value = selector.split('=>')[1]  # 取的是=>右边的值

        if selector_by == "i" or selector_by == "id":
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == "name":
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == "class_name":
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == "link_text":
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == "partial_link_text":
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == "tag_name":
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == "xpath":
            element = self.driver.find_element_by_xpath(selector_value)
        else:
            selector_by == "s" or selector_by == "selector_selector"
            element = self.driver.find_element_by_css_selector(selector_value)
        return element

    # 获取被测网站
    def get(self, url):
        return self.driver.get(url)

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 浏览器前进操作
    def back(self):
        self.driver.forward()

    # 获取浏览器标题
    def get_page_title(self):
        return self.driver.title

    # 浏览器关闭操作
    def close(self):
        return self.driver.close()

    # 截图并保存在根目录下的screenshots文件夹下
    def get_page_img(self):
        current_path = os.path.abspath('..')
        img_path = os.path.join(current_path, 'screenshots')
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        screen_name = os.path.join(img_path, str(time.strftime('%Y-%m-%d%H%M', time.localtime(time.time()))) + '.png')
        self.driver.get_screenshot_as_file(screen_name)
