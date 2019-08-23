from src.test.page.login_page import Login_page
from selenium.webdriver.common.by import By
from assertpy import assert_that

# from src.test.common.page import Page

import time
import os

class Voince_page(Login_page):
    # 此处可以设置从文件中读取定位元素
    voincelink_loc=(By.XPATH,'//a[@href="/dc/invoice/invoiceNotice"]//img') #发票核查系统链接

    #正常录入
    def voince_inspect(self,data):
        if not self.tag:
            self.click(*self.voincelink_loc)
            self.tag=True
        if data.get('是否测试').upper()=='Y':
            erro_msg = data.get('验证信息')
            if data.get('用例描述') == '正确输入':
                self.send_value(self, data)
                time.sleep(3)
                assert (self.current_url == erro_msg), '正确数据提交网址%s验证失败' % data.get('验证信息')
            elif '姓名为空' in data.get('用例描述'):
                self.send_value(self, data)
                time.sleep(3)
                assert (self.find_element(*self.name_loc_error).text == erro_msg), '姓名为空验证失败'
        else:
            print('不执行“%s”用例'%data.get('用例描述'))

    #输入数据
    def send_value(self,obj,data):
        self.click(*self.voinceonline_loc)#在线填报链接
        self.click(*self.voinceadd_loc)
        if data.get('姓名'):
            self.select_select(data.get('姓名'), *self.name_loc, tag='text')  # 是否触发事件
        self.find_element(*self.userName_loc).send_keys(data.get('消费者姓名'))
        # .......
        assert '成功' in self.page_source, '执行失败'
















