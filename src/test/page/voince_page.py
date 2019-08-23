from src.test.page.login_page import Login_page
from selenium.webdriver.common.by import By
from assertpy import assert_that

# from src.test.common.page import Page

import time
import os

class Voince_page(Login_page):
    # 此处可以设置从文件中读取定位元素
    voincelink_loc=(By.XPATH,'//a[@href="/dc/invoice/invoiceNotice"]//img') #发票核查系统链接
    voinceonline_loc=(By.XPATH,'//li[@id="invoiceView"]/a/span') #在线填报链接
    voinceadd_loc=(By.XPATH,'//a[@id="goIntegra"]//img') #新增发票
    name_loc=(By.ID,'integralId') #姓名
    userName_loc=(By.XPATH,'//input[@name="userName"]') #消费者姓名
    userPhone_loc=(By.XPATH,'//input[@name="userPhone"]') #消费者手机号
    idCard_loc=(By.XPATH,'//input[@name="idCard"]') #消费者身份证号
    saleTime_loc=(By.ID,'date1') #销售时间(开票时间)
    carName_loc=(By.ID,'carName') #车辆通用名称
    carTypeSfx_loc=(By.ID,'carTypeSfx') #车型SFX
    carIdentify_loc=(By.ID,'carIdentify') #车架号
    mfrprice_loc=(By.ID,'mfrprice') #厂家指导价(元)
    salePrice_loc=(By.ID,'salePrice') #销售价格(元)
    invoiceCode_loc=(By.ID,'invoiceCode') #发票号码
    invoiceReCode_loc=(By.ID,'invoiceReCode') #发票代码
    chk_loc=(By.ID,'chk') #是否公务员购车
    iscmp_loc=(By.ID,'iscmp') #是否企业合作购车
    userConfirm_loc=(By.ID,'userConfirm') #发票文件
    voinsubmit_loc=(By.XPATH,'//button[@onclick="submitForm(2)"]') #提交并返回发票列表

    name_loc_error =(By.XPATH,'//select[@id="integralId"]/following-sibling::span[1]')   #姓名
    tag = False  # 是否点击 发票核查系统链接
    #正常录入
    def voince_post(self,data):
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
        self.find_element(*self.userPhone_loc).send_keys(data.get('消费者手机号'))
        self.find_element(*self.idCard_loc).send_keys(data.get('消费者身份证号'))
        if data.get('销售时间'):
            self.execute_script('document.getElementById("date1").removeAttribute("readonly")')
        self.find_element(*self.saleTime_loc).send_keys(data.get('销售时间'))
        # self.execute_script('document.getElementById("date1").value={0}'.format('2018-04-12'))
        if data.get('车辆通用名称'):
            self.select_select(data.get('车辆通用名称'), *self.carName_loc, tag='text')
        if data.get('型号'):
            self.select_select(data.get('型号'), *self.carTypeSfx_loc, tag='text')
        self.find_element(*self.carIdentify_loc).send_keys(data.get('车架号'))
        if data.get('型号') and data.get('厂家指导价'):
            self.select_select(int(data.get('厂家指导价')), *self.mfrprice_loc, tag='index')
        self.find_element(*self.salePrice_loc).send_keys(data.get('销售价格'))
        self.find_element(*self.invoiceCode_loc).send_keys(data.get('发票号码'))
        self.find_element(*self.invoiceReCode_loc).send_keys(data.get('发票代码'))
        self.click(*self.chk_loc) #是否公务员购车
        self.click(*self.iscmp_loc) #是否企业合作购车
        self.find_element(*self.userConfirm_loc).send_keys(data.get('发票文件'))
        self.click(*self.voinsubmit_loc)
        time.sleep(5)
        assert '成功' in self.page_source, '失败'

















