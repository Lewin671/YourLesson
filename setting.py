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

user_id:str = "2017152021"

cookie = "_WEU=0qMYZBOvtf7Ra6_CfSmbRF2aMOQneYhvisiP*xoZ3lE4usEtfqxDFCGUhdSGrQQw; zg_did=%7B%22did%22%3A%20%221753a037e6b7e6-012d7997d317e2-c781f38-144000-1753a037e6c33e%22%7D; zg_=%7B%22sid%22%3A%201602996108911%2C%22updated%22%3A%201602996161598%2C%22info%22%3A%201602996108914%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22ehall.szu.edu.cn%22%2C%22cuid%22%3A%20%222017152021%22%7D; JSESSIONID=l2gQ1ltJXIp4PolCKhTANC8Nm5HH2kh9xLMRboPPVloYB93KKkTS!-278811102; insert_cookie=33374701"

electiveBatchCode = "b17be93d9658460e93ef557001242982"

token = "663cc520-b499-445a-8ba8-706aa6871d80"


# 你要抢的课程，按照如下格式提前先填写好
courses =[
    {'id':'201920201190114000103','type':'FXKC','name':"解析几何(徐希)"},
    {'id':'201920201990008000101','type':'MOOC','name':"拓展英语词汇"},
    {'id':'201920201990039000101','type':'MOOC','name':"走进性科学"},
]


# 延迟的单位是ms
delay:int = 1000
# 抢课的次数
count:int = 3


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


