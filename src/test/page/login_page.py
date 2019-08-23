from selenium.webdriver.common.by import By
from src.test.common.page import Page
from utils.settings import Settings
import time


class Login_page(Page):
    username_loc=(By.XPATH,'//input[@name="username"]') #用户名
    password_loc=(By.XPATH,'//input[@name="password"]') #密码
    loginsubmit_loc=(By.XPATH,'//input[@type="submit"]') #提交
    login_valid=(By.XPATH,'//p[contains(.,"实现更便捷")]') #验证登录是否成功
    username=Settings().get('user',index=0)
    password=Settings().get('pwd',index=0)

    def login(self):
        self.find_element(*self.username_loc).send_keys(self.username)
        self.find_element(*self.password_loc).send_keys(self.password)
        self.click(*self.loginsubmit_loc)
        assert '实现更便捷、更准确的沟通' in self.find_element(*self.login_valid).text,'登录失败'
