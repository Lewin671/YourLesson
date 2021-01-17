# -*- coding: utf-8 -*-
# 程序测试部分

import requests
import setting
import util
import downloads
import choose_course

# 测试获取cookie
url = "http://bkxk.szu.edu.cn/xsxkapp/sys/xsxkapp/*default/index.do"
session = util.get_session()
data = {
    "timeTemp":util.get_timestamp()
}

# 查询志愿
# response = session.post(util.get_url("xsxkapp/sys/xsxkapp/publicinfo/volunteer.do"),headers=setting.headers,data = data)
# print(response.headers)
# print(response.text)
#print(downloads.recommended_course(0))
# downloads.downloads()
