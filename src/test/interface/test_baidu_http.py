import unittest, os, sys,time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_PATH)
from utils.settings import Settings, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils import HTMLTestRunner_jpg
from utils.assertion import assertHTTPCode
from utils.mail import Email


class TestBaiDuHTTP(unittest.TestCase):
    URL = Settings().get('url',index=2) #设置url地址,正式用时去掉
    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET',headers=None,cookies=None)

    def test_baidu_http(self):
        res = self.client.send(
            params='',
            dataType=None,
            data='')
        logger.debug(res.text)
        assertHTTPCode(res, [400]) #断言
        self.assertIn('百度一下，你就知道', res.text)

if __name__ == '__main__':
    logger.info('接口开始测试')
    report_name='report_%s.html'%time.strftime("%Y%m%d_%H%M%S")
    report = os.path.join(REPORT_PATH,report_name)
    runner = HTMLTestRunner_jpg.HTMLTestRunner(
        stream=open(report, 'wb'),
        verbosity=2,
        title='百度接口测试',
        description='接口测试执行情况')
    runner.run(TestBaiDuHTTP('test_baidu_http'))
    # e = Email(title='报备测试报告',    #发送邮件
    #           message='这是今天的测试报告，请查收！',
    #           receiver='aaa@qq.com;ccc@qq.com',
    #           server='服务器地址',
    #           sender='sender@qq.com',
    #           password='88888',
    #           path=report
    #           )
    # e.send()