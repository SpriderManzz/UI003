# coding=utf-8
from selenium import webdriver
from framework.browser_engine2 import BrowserEngine
driver = webdriver.Firefox()
a = BrowserEngine(driver)
a.get_driver()