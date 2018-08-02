import requests

url = 'http://10.188.2.98:8188/ewap-auth/system/user/getBtn'
data = "Index.html"

header = {
    "Authorization": "55cc63ba-ffe4-42cc-956b-dad10d3a1c40",
    "Content-Type": "application/json",
}

res = requests.post(url=url, data=data, headers=header).json()
print(res)


# def getBtn(url, data, header):
#     res = requests.post(url=url, data=data, headers=header)
#     result = res.json()
#     return result
#
#
# result1 = getBtn(url, data, header)
# print(result1)
