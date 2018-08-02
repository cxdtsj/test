import HTMLTestRunner
import unittest
from base.test_method import TestMethod

filepath = "D:\\Testfan\\ImoocInterface\\report\\result.html"
fp = open(filepath, 'wb')
suite = unittest.TestSuite()
suite.addTest(TestMethod('test_01'))
suite.addTest(TestMethod('test_02'))
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="This is first report.")
runner.run(suite)
fp.close()