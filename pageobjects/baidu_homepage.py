# coding=utf-8
from framework.base_page import Base_Page
class Baidu_Homepage(Base_Page):
    """存放百度首页的元素"""

    @property     # 包含了元素的定位 并作为属性调用
    def search_box(self):
        return self.id_("kw")

    @property
    def search_button(self):
        return self.xpath(".//*[@id='su']")


