from base.demo import RunMain


class GetToken:

    run = RunMain()

    # 获取token
    def get_token(self):
        url = 'http://10.188.2.98:8188/ewap-auth/system/user/login'
        data = {
            "no": "CXD001",
            "password": "1",
            "hostType": "WEB"
        }
        res = self.run.run_main(url, 'POST', data)
        token = res['results']['token']
        return token


if __name__ == '__main__':

    token2 = GetToken()
    token3 = token2.get_token()
    print(token3)
