import requests

# 测试获取cookie
url = "http://bkxk.szu.edu.cn/xsxkapp/sys/xsxkapp/*default/index.do"
response = requests.get(url)
print(response.headers)