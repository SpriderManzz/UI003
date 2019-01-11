# coding=utf-8
from framework.base_page import Base_Page
class BaiduHome_Page(Base_Page):
    """存放百度首页的元素和元素的操作"""
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_search(self, text):  # 调用type_search需要穿一个参数
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)





