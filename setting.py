user_id = "2017152021"

# 用浏览器在登陆的时候抓包
# 登陆成功后查看recommendedCourse.do的报文
# 找到Cookie和vtoken和electiveBatchCode，填写如下变量

cookie = ""
token = ""
electiveBatchCode = ""

# 延迟的单位是ms
delay = 100
# 抢课的次数
count = 3

########## 以上需要用户自行配置 ############

url = "http://bkxk.szu.edu.cn/"
# see recommendedCourse.do
headers =  {
    "Cookie": cookie,
    "token": token,
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
}


