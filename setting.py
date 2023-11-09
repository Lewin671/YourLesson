# -*- coding: utf-8 -*-
# 程序设置

'''
这是一个用户配置文档，您只需要在这里进行配置。
需要配置的属性有:
1. user_id: 学号
2. cookie,electiveBatchCode,token这三个字段需要在浏览器登录后，打开开发者工具，选择在network选项卡中选择recommendedCourse.do
   然后再找出相应字段
3. 你要选择的课程，类比相关格式，填写courses
4. 然后设置抢课延迟和选课提交次数
'''

user_id = "2022150091"

cookie = "_WEU=T705A2ZMlmBePuySlyHQQYUo7W9pvr2gmOQe48iwq4NS73qNezsNRIptWb*zwg1D; JSESSIONID=F5B6B297FCD1170DDEC9093426C33BBD; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAyMjE1MDA5MSIsImdyb3VwcyI6WzE1XSwiaWF0IjoxNjk0MzU3MzQ4LCJleHAiOjE2OTQ0NDM3NDh9.H45NeDjltqHKlVBPr6uD-rpDBezfOnFVm4WrH-RynQs; webvpn_username=2022150091%7C1694357348%7Caac656bc6b5f9d1148c269a6ff81f0614b3a4619; insert_cookie=33651787; iPlanetDirectoryPro=3SVxZaH5xCG26vdXYgBMM0; nZUAHEcHJdbMO=60klwG25fxLZsoNwSJhHxXVpzGAz0Iy.1lxdkweF.hwY.aRCoCw.SctwHoNR0aIKs8RFMD18RC.J3ST2d1C9il_q"
electiveBatchCode = "f0af76e1e27f4e9e9a7c4f495aa04655"

token = "29a26510-9fbb-4858-816b-e65771728245"

# 本班课程： 'TJKC'
# 方案内课程: 'FANKC'
# 方案外课程： 'FAWKC'
# 校公选课： 'XGXK'
# 慕课: "ＭOOC"，
# 辅修课程: "FXKC"，
# 体育课程:"TYKC"
# 你要抢的课程，按照如下格式提前先填写好
courses = [
    {'id': '202320241150291000101', 'type': 'FANKC', 'name': "计算机安全导论"},
    {'id': '202320241150061000302', 'type': 'FANKC', 'name': "计算机图形学"},
    {'id': '202320241510003000101', 'type': 'FANKC', 'name': "军事理论"},
]

# 抢课的间隔，单位是毫秒
delay:int = 350

# 抢课的次数
count:int = 1000




########## 以上需要用户自行配置 ############

########## 请不要修改下面的配置  ############

url:str = "http://bkxk.szu.edu.cn/"

headers:map =  {
    "Cookie": cookie.strip(),
    "token": token.strip(),
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "bkxk.szu.edu.cn",
    "Pragma": "no-cache"
}


