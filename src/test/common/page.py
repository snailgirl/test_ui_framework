from src.test.common.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

class Page(Browser):

    def __init__(self, page=None, browser_type='firefox'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def get_driver(self):
        return self.driver

    '''1重写元素定位方法'''
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element(*loc))
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未能找到 %s 元素" % (self, loc))

        def find_elements(self, driver, *loc):
            try:
                WebDriverWait(self.driver, 60).until(lambda x: x.find_elements(*loc))
                return self.driver.find_elements(*loc)
            except:
                print("%s 页面中未能找到 %s 元素" % (self, loc))

    '''2 重写switch_frame方法'''
    def switch_frame(self, *loc):
        ele = self.driver.find_element(self, *loc)
        return self.driver.switch_to_frame(ele)


    '''3 执行 javascript脚本'''
    # 定义script方法，用于执行js脚本，范围执行结果
    def execute_script(self, src):
        self.driver.execute_script(src)
        time.sleep(2)

    '''4 重写鼠标事件'''
    #单击
    def click(self,*loc):
        ActionChains(self.driver).click(self.driver.find_element(*loc)).perform()
    # 双击
    def double_click(self,*loc):
        ActionChains(self.driver).double_click(self.driver.find_element(*loc)).perform()

    '''5 下拉框选择'''
    def select_select(self,value,*loc,tag='value'):
        select_element = Select(self.find_element(*loc))
        if tag=='index':  #通过序号选择
            select_element.select_by_index(value)
        elif tag=='value':  #通过value属性选择
            select_element.select_by_value(value)
        elif tag == 'text': #通过显示文本选择
            select_element.select_by_visible_text(value)
        else:
            print('%s 不存在'%(tag))
            return
        # assert (select_element.all_selected_options[0].text == value)

    '''当前网页的网址'''
    @property
    def current_url(self):
        return self.driver.current_url









