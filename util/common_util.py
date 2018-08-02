class CommonUtil:
    def is_contain(self,true_data,except_data):
        '''
        判断一个字符串是否在另一个字符串中
        str_one:查找的字符串
        str_two:被查找的字符串
        '''
        self.flag = None
        if true_data in except_data:
            flag = True
        else:
            flag = False
        return flag