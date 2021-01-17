# -*- coding: utf-8 -*-
# 登录相关逻辑

import setting
import util
import json
import os

headers = setting.headers
session = util.get_session()


# 获取coolie值
def get_cookie():
    response = session.get(util.get_url("xsxkapp/sys/xsxkapp/*default/index.do"),headers=headers)
    return response.headers['Set-Cookie']

def set_cookie():
    headers['Cookie'] = get_cookie()

def get_token():
    post_data = {
        "timestamp" : str(util.get_timestamp())
    }
    response = session.post(url=util.get_url("xsxkapp/sys/xsxkapp/student/4/vcode.do"),headers=headers,data=post_data)
    # 注意此时返回的是json数据文本
    # 用json工具转换成对象
    obj = json.loads(response.text)
    return obj['data']['token']

