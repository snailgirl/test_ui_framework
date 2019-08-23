"""
我们先在ReadMe.md中补上新加的依赖库。

添加用于接口测试的client，对于HTTP接口添加HTTPClient，发送http请求。
还可以封装TCPClient，用来进行tcp链接，测试socket接口等等。
"""

import requests,json
from utils.log import logger

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class UnSupportMethodException(Exception):
    """当传入的method的参数不是支持的类型时抛出此异常。"""
    pass


class HTTPClient(object):
    """
    http请求的client。初始化时传入url、method等，可以添加headers和cookies，但没有auth、proxy。

    >>> HTTPClient('http://www.baidu.com').send()
    <Response [200]>

    """
    def __init__(self, url, method='GET', headers=None, cookies=None):
        """headers: 字典。 例：headers={'Content_Type':'text/html'}，cookies也是字典。"""
        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHODS:
            raise UnSupportMethodException('不支持的method:{0}，请检查传入参数！'.format(self.method))
        self.set_headers(headers)
        self.set_cookies(cookies)

    def set_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, test_data,**kwargs):
        '''封装requests请求
        test_data为字典类型：
        {'params':params,'datatype': datatype,'data':data, 'checkpoint':checkpoint}
        '''
        # url后面的params参数
        try:
            params = eval(test_data.get('params'))
        except:
            params = None

        # test_nub = testdata['id']
        # print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        # print("请求方式：%s, 请求url:%s" % (self.method, self.url))
        # print("请求params：%s" % params)

        # post请求body内容
        try:
            bodydata = eval(test_data.get('data'))
        except:
            bodydata = {}

        # 判断传data数据还是json
        datatype = test_data.get('dataType').lower()
        if type == "data":
            data = bodydata
        elif type == "json":
            data = json.dumps(bodydata)
        else:
            data = bodydata
        # if self.method == "post": print("post请求body类型为：%s ,body内容为：%s" % (type, body))
        verify=False
        res = {}  # 接受返回数据
        try:
            response = self.session.request(method=self.method, url=self.url, params=params, data=data, verify=verify,
                                            **kwargs)
            response.encoding = 'utf-8'
            logger.debug('{0} {1}'.format(self.method, self.url))
            logger.debug('请求成功: {0}\n{1}'.format(response, response.text))

            print("页面返回信息：%s" % response.content.decode("utf-8"))
            # res['id'] = testdata['id']
            # res['rowNum'] = testdata['rowNum']
            res["statuscode"] = str(response.status_code)  # 状态码转成str
            res["text"] = response.content.decode("utf-8")
            res["times"] = str(response.elapsed.total_seconds())  # 接口请求时间转str
            if res["statuscode"] != "200":
                res["error"] = res["text"]
            else:
                res["error"] = ""
            res["msg"] = ""
            if test_data.get('checkpoint') in res["text"]:
                res["result"] = "pass"
                # print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
            else:
                res["result"] = "fail"
            return res
        except Exception as msg:
            res["msg"] = str(msg)
            return res
