import requests
import json


class RunMain:

    # def __init__(self, url, method, data=None):
    #     self.res = self.run_main(url, method, data)

    def send_post(self, url, data, header):
        res = requests.post(url=url, json=data, headers=header).json()
        return res
        # return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)

    def send_get(self, url, data, hearder):
        res = requests.get(url=url, json=data, hearders=hearder).json()
        return res
        # return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)

    def run_main(self, url, method, data=None, header=None):
        self.res = None
        if method == 'GET':
            res = self.send_get(url, data, header)
        else:
            res = self.send_post(url, data, header)
        return res


if __name__ == '__main__':

    run = RunMain()
    url = 'http://10.188.2.98:8188/ewap-auth/system/user/login'
    data = {
        "no": "xdchen",
        "password": "11",
        "hostType": "WEB"
    }

    # 未设置构造函数时，运行以下代码
    res = run.run_main(url, 'POST', data)
    # print(res)
    print(type(res))

    # run = RunMain(url, 'POST', data)
    # print(run.res)
