import unittest
import HTMLTestRunner
from base.gettoken import GetToken
from base.demo import RunMain


# 全局变量
#temp_token = GetToken().get_token()


class TestMethod(unittest.TestCase):

    # 定义基本属性，使每个方法都可以调用token
    temp_token = GetToken().get_token()

    def setUp(self):
        self.run = RunMain()

    # 工厂结果列表查询
    def test_01(self):
        url = 'http://10.188.2.98:8188/ewap-auth/base/plant/querylistByPage'
        data = {
            "plantNo": "",
            "nameCn": "",
            "pageSize": "10",
            "pageIndex": 1
        }

        header = {
            "Authorization": self.temp_token,
            "Content-Type": "application/json",
        }
        res = self.run.run_main(url, 'POST', data, header)
        self.assertEqual(res['code'], '10000', "测试不通过")
        # print(res)
        # print("这是第一个case")

    def test_02(self):
        url = 'http:/ewap-auth/base/plant/querylistByPage'
        data = {
            "plantNo": "",
            "nameCn": "",
            "pageSize": "10",
            "pageIndex": 1
        }

        header = {
            "Authorization": self.temp_token,
            "Content-Type": "application/json",
        }
        res = self.run.run_main(url, 'POST', data, header)
        self.assertEqual(res['code'], '10000', "测试不通过")
        # print(res)
        # print("这是第二个case")


if __name__ == '__main__':
    # unittest.main()
    filepath = "D:\\Testfan\\ImoocInterface\\report\\result.html"
    fp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="This is first report.")
    runner.run(suite)
    fp.close()
    # unittest.TextTestRunner().run(suite)
