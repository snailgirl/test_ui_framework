#coding=utf-8
import unittest
import os,ddt

from src.test.page.voince_page import Voince_page
from src.utils.settings import DATA_PATH,Settings
from src.utils.file_reader import ExcelReader
_reader = ExcelReader(os.path.join(DATA_PATH, '测试用例.xlsx'), sheet='case2').data  # 数据路径

@ddt.ddt
class Invoice_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        URL = Settings().get('url',index=0)
        self.driver=Voince_page(browser_type='chrome').get(
            URL,
            maximize_window=False)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_login(self):
        """
        登录
        """
        self.driver.login()

    @ddt.data(*_reader)
    def voince_inspect(self,data):
        """
        case2 测试
        """
        self.driver.voince_inspect(data)

if __name__ == '__main__':
    unittest.main()