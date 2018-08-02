
from util.operation_excel import OperationExcel
import data.data_config
from util.operation_json import OperationJson


class GetData:

    def __init__(self):
        self.opera_excel = OperationExcel()

    # 去获取excel行数，就是case的个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        self.flag = None
        col = int(data.data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def get_is_header(self, row):
        col = int(data.data_config.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return data.data_config.get_header_value()
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data.data_config.get_request_way())
        rquest_method = self.opera_excel.get_cell_value(row, col)
        return rquest_method

    # 获取url
    def get_request_url(self, row):
        col = int(data.data_config.get_url())
        request_url = self.opera_excel.get_cell_value(row, col)
        return request_url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data.data_config.get_data())
        request_data = self.opera_excel.get_cell_value(row, col)
        if request_data == '':
            return None
        return request_data

    # 通过获取json关键字拿到数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_except_data(self, row):
        col = int(data.data_config.get_expect())
        except_data = self.opera_excel.get_cell_value(row, col)
        if except_data == '':
            return None
        return except_data

    # 写入数据
    def write_result(self,row,value):
        col = int(data.data_config.get_result())
        self.opera_excel.write_value(row,col,value)

if __name__ == '__main__':
    data1 = GetData()
    print(data1.get_request_url(1))
    print(data1.get_case_lines())