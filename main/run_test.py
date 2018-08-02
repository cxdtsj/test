from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil

class RunTest():

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    # 程序执行
    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            expect = self.data.get_except_data(i)
            header = self.data.get_is_header(i)
            if is_run:
                res = self.run_method.run_main(method,url,data,header)
                if self.com_util.is_contain(expect,res):
                    print(res)
                    #print("测试通过")
                    #self.data.write_result(i,"pass")
                else:
                    print(res)
                    #print("测试失败")
                    #self.data.write_result(i,"fail")

if __name__ == '__main__':
    run = RunTest()
    #print(run.go_on_run())
    run.go_on_run()