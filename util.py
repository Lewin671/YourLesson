# -*- coding: utf-8 -*-
# 程序工具

import time
import requests
import setting

session = requests.session()
current_milli_time = lambda: int(round(time.time() * 1000))


# 返回当前时间戳
def get_timestamp():
    return str(current_milli_time())
    
# Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
# 返回session
def get_session():
    return session

# 获取完整路径
def get_url(relavie_path):
    return "{}{}".format(setting.url,relavie_path)
