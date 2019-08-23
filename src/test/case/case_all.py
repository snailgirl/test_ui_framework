#coding=utf-8
import unittest
import os,sys,time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_PATH)
from utils.log import logger
from utils.settings import Settings, REPORT_PATH,DATA_PATH,CASE_PATH,EXECEL_FILE
from utils import HTMLTestRunner_jpg
import traceback #导入堆栈类
from utils.mail import Email

# python2.7要是报编码问题，就加这三行，python3不用加
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    logger.info('功能开始测试')
    discover=unittest.TestSuite()
    #添加可以测试模块
    for test,yes_no in EXECEL_FILE:
        if yes_no.upper()=='Y':
            discover1 = unittest.defaultTestLoader.discover(CASE_PATH,"test_%s.py"%test)
            discover.addTests(discover1)
    # discover = unittest.defaultTestLoader.discover(CASE_PATH,"test*.py")
    report_name='report_%s.html'%time.strftime("%Y%m%d_%H%M%S")
    report = os.path.join(REPORT_PATH,report_name)
    fp=open(report, 'ab')
    # 生成报告
    runner = HTMLTestRunner_jpg.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title='生成发票',
        description='用例执行情况')
    try:
        runner.run(discover)
    except Exception as e:
        print(traceback.print_exc())
        print(e)
        fp.close()
    # e = Email(title='报备测试报告',    #发送邮件
    #           message='这是今天的测试报告，请查收！',
    #           receiver='aaa@qq.com;ccc@qq.com',
    #           server='服务器地址',
    #           sender='sender@qq.com',
    #           password='88888',
    #           path=report
    #           )
    # e.send()
